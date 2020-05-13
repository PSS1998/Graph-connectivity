import networkx as nx
import math  
import random
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import Axes3D

def distance(point1, point2):
	return math.sqrt((point2[1]-point1[1])**2+(point2[0]-point1[0])**2)

def random_graph_model(num_nodes, Area, signal_radius):
	G = nx.Graph()
	d = defaultdict()

	for i in range(num_nodes):
		side = math.sqrt(Area)
		x = random.random()*side
		y = random.random()*side
		G.add_node(i)
		d[i] = (x,y)
	for i in range(num_nodes):
		for j in range(i+1, num_nodes):
			if(distance(d[i], d[j]) < signal_radius):
				G.add_edge(i, j)

	return G, d

def print_graph(Graph, coordinates, name):
	fig, ax = plt.subplots()
	nx.draw(Graph, coordinates, node_size=20, ax=ax)
	limits=plt.axis('on')
	ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
	fig = plt.gcf()
	fig.set_size_inches(16, 12)
	plt.savefig(name+'.png', bbox_inches='tight', dpi=100)	

def average_largest_connected_component():
	x=[]
	y=[]
	for i in range(1,1000,10):
		lcc_size = 0
		for j in range(5):
			G, d = random_graph_model(i, 100, 1)
			lcc_size += len(sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0].nodes())
		lcc_size /= 5
		x.append(i)
		y.append(lcc_size)
	plt.xlabel('Number of Nodes')
	plt.ylabel('Average number of Largest Connected Component Nodes')
	plt.scatter(x,y)
	fig = plt.gcf()
	fig.set_size_inches(16, 12)
	plt.savefig('Average number of Largest Connected Component Nodes with variable Number of Nodes.png', bbox_inches='tight', dpi=100)
	plt.clf()

def average_second_largest_connected_component():
	x=[]
	y=[]
	end_count = 0
	for i in range(10,1000,1):
		lcc_size = 0
		lcc_num = 0
		for j in range(50):
			G, d = random_graph_model(i, 100, 1)
			lcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
			if len(lcc)>1:
				lcc_num += 1
				lcc_size += len(lcc[1].nodes())
		if lcc_num != 0:
			lcc_size /= lcc_num
		else:
			end_count += 1
		if end_count>5:
			break
		x.append(i)
		y.append(lcc_size)
	plt.xlabel('Number of Nodes')
	plt.ylabel('Average number of Second Largest Connected Component Nodes')
	plt.scatter(x,y)
	fig = plt.gcf()
	fig.set_size_inches(16, 12)
	plt.savefig('Average number of Second Largest Connected Component Nodes with variable Number of Nodes.png', bbox_inches='tight', dpi=100)
	plt.clf()

def average_isolated_nodes():
	x=[]
	y=[]
	end_count = 0
	for i in range(10,1000,2):
		lcc_size = 0
		lcc_num = 0
		for j in range(10):
			G, d = random_graph_model(i, 100, 1)
			isolated_list = list(nx.isolates(G))
			if len(isolated_list)>0:
				lcc_num += 1
				lcc_size += len(isolated_list)
		if lcc_num != 0:
			lcc_size /= lcc_num
		else:
			end_count += 1
		if end_count>5:
			break
		x.append(i)
		y.append(lcc_size)
	plt.xlabel('Number of Nodes')
	plt.ylabel('Average number of Isolated Nodes')
	plt.scatter(x,y)
	fig = plt.gcf()
	fig.set_size_inches(16, 12)
	plt.savefig('Average number of Isolated Nodes with variable Number of Nodes.png', bbox_inches='tight', dpi=100)
	plt.clf()

def alpha_connected_probability(num_nodes, Area, alpha):
	if num_nodes==100:
		start=85
		end=175
		step=1
		decimal=100
		if alpha==0.8:
			name="Probability of 0.8-connected with 100 Nodes and Area of 100 and variable of Radius"
		elif alpha==0.5:
			name="Probability of 0.5-connected with 100 Nodes and Area of 100 and variable of Radius"
	elif num_nodes==1000:
		start=1150
		end=1450
		step=4
		decimal=1000
		name="Probability of 0.8-connected with 1000 Nodes and Area of 1000 and variable of Radius"
	x=[]
	y=[]
	end_count = 0
	for i in range(start,end,step):
		lcc_size = 0
		lcc_num = 0
		for j in range(100):
			G, d = random_graph_model(num_nodes, Area, i/decimal)
			largest_lcc = len(sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0].nodes())
			n = alpha*num_nodes
			if largest_lcc>=n:
				lcc_num += 1
		x.append(i/decimal)
		y.append(lcc_num)
	plt.xlabel('Radius')
	plt.ylabel('Probability')
	plt.scatter(x,y)
	fig = plt.gcf()
	fig.set_size_inches(16, 12)
	plt.savefig(name+'.png', bbox_inches='tight', dpi=100)
	plt.clf()


		




#part1
G, d = random_graph_model(10, 100, 1)
print_graph(G, d, "Random Graph with number of Nodes 10, Area 100, Radius 1")
G, d = random_graph_model(50, 100, 1)
print_graph(G, d, "Random Graph with number of Nodes 50, Area 100, Radius 1")
G, d = random_graph_model(100, 100, 1)
print_graph(G, d, "Random Graph with number of Nodes 100, Area 100, Radius 1")
G, d = random_graph_model(300, 100, 1)
print_graph(G, d, "Random Graph with number of Nodes 300, Area 100, Radius 1")
G, d = random_graph_model(1000, 100, 1)
print_graph(G, d, "Random Graph with number of Nodes 1000, Area 100, Radius 1")

average_largest_connected_component()
average_second_largest_connected_component()
average_isolated_nodes()


# part2
alpha_connected_probability(100, 100, 0.8)
alpha_connected_probability(100, 100, 0.5)
alpha_connected_probability(1000, 1000, 0.8)


