## Dataset AIDS
As an independent experiment, I chose the AIDS dataset: the AIDS data set consists of graphs
representing molecular compounds. Graphs are constructed from the Antiviral Screen Database
of Active Compounds. It consists of 2000 fully connected graphs that we treat as a single,
disconnected, graph. The assortativity is, understandably, -0.395.

#### Graphs
This data set consists of two classes (active and inactive), which represent molecules with activity 
against HIV or not. Since FAGCN performs node classification we do not care about this.

#### Nodes
Nodes represent atoms and are labeled with the number of the corresponding chemical symbol

#### Edges
Edges represent covalent bonds and are labeled by the valence of the linkage.


## Results
The accuracy for the aids dataset was calculated by running the training 5 times and report the mean accuracy: 
in this case with the hyper-parameters used for the disassortative networks, with epsilon search space in {0.3, 0.4, 0.5}\
Epsilon = 0.3, Accuracy = 62.83% \
Epsilon = 0.4, Accuracy = 62.68% \
Epsilon = 0.5, Accuracy = 62.68%
