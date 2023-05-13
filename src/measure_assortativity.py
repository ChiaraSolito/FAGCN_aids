import numpy as np
import dgl
import torch

import matplotlib.pyplot as plt
import networkx as nx
from utils import normalize_features

#Hardcoded
dataset = 'aids'
train_ratio = 0.6

edge = np.loadtxt('./high_freq/{}/edges.txt'.format(dataset), dtype=int)
edge = edge[edge[:, 0].argsort()]
labels = np.loadtxt('./high_freq/{}/labels.txt'.format(dataset), dtype=int).tolist()
features = np.loadtxt('./high_freq/{}/features.txt'.format(dataset), dtype=float)

U = [e[0]-1 for e in edge]
V = [e[1]-1 for e in edge]
g = dgl.graph((U, V))
g = dgl.to_simple(g)
g = dgl.to_bidirected(g)
g = dgl.remove_self_loop(g)

n = len(labels)
idx = [i for i in range(n)]
r0 = int(n * train_ratio)
r1 = int(n * 0.6)
r2 = int(n * 0.8)
train = np.array(idx[:r0])
val = np.array(idx[r1:r2])
test = np.array(idx[r2:])

features = normalize_features(features)
features = torch.FloatTensor(features)

nclass = 37
labels = torch.LongTensor(labels)
train = torch.LongTensor(train)
val = torch.LongTensor(val)
test = torch.LongTensor(test)


#### PRINT INFO ABOUT THE GRAPH ####
print("Name of dataset: %s"%dataset)
print("Number of classes for node classification: %i"%nclass)
print("Number of nodes: %i"%g.number_of_nodes())
print("Length of labels: %i"%len(labels))
print("Length of features: %i\n"%len(features))


#### Calculate assortativity ####
G = dgl.to_networkx(g)
r=nx.degree_assortativity_coefficient(G)
print("Assortativity is %f"%r)


