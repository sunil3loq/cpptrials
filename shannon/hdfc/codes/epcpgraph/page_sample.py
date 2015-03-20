
import networkx as nx
import itertools
import operator
import matplotlib.pyplot as plt
'''
normalizenodes(G)
nx.draw(G)
plt.draw()
plt.show()
invpersonalization=getinversepop(G)
print "inverse personalization is,",invpersonalization
'''

G=nx.DiGraph()
G.add_node("SA")
G.add_node("CC")
G.add_node("Loan")
G.add_node("Ins")
G.add_edge("SA","CC",weight=30)
G.add_edge("SA","Loan",weight=10)
G.add_edge("SA","Ins",weight=20)
G.add_edge("CC","SA",weight=30)
G.add_edge("CC","Loan",weight=8)
G.add_edge("CC","Ins",weight=3)
G.add_edge("Ins","SA",weight=20)
G.add_edge("Ins","CC",weight=3)
G.add_edge("Ins","Loan",weight=2)
G.add_edge("Loan","SA",weight=10)
G.add_edge("Loan","CC",weight=8)
G.add_edge("Loan","Ins",weight=2)
pagedict=nx.pagerank(G,alpha=1)
sorted_x = sorted(pagedict.items(), key=operator.itemgetter(1))
print sorted_x
