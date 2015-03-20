import argparse
import networkx as nx
import itertools
import operator
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser(description='Parsing Arguments for getting sample columns')

parser.add_argument('--inputdlm','-d',default=',',help='default delimiter of the input file to use')
parser.add_argument('--outputdlm','-od',default='|',help='default delimiter of the output')
parser.add_argument('--includecols','-i',action='store_true',help='whether to include or ignore the columns')
parser.add_argument('inputfile',help='input file')
parser.add_argument('cols',help='cols to include or ignore')

args=parser.parse_args()


#filein="/home/loq/sunil/hdfc/onezeros/epcp_1412_noid.csv"
filein=args.inputfile
#ignorecols="1,2,10,45,51,52,44,23,3,7,35,11,5,4,6,8"
includecols=args.includecols
dlm=args.inputdlm

def getcolslist(inputstr):
    '''get the list of columns from the string'''
    outlist=inputstr.split(',')
    outlist=[int(elem)-1 for elem in outlist]
    return outlist

def makehead(linein,indlm=","):
    '''makes the head dict for a file'''
    linelist=linein.strip().split(indlm)
    outhead={}
    for ind,elem in enumerate(linelist):
        outhead[elem]=ind
    return outhead,linelist

def getproducts(holdboolean,ignores,prodnames):
    '''gets the list of products the person holds'''
    products=[]
    for num,elem in enumerate(holdboolean):
        if num not in ignores and elem=="1":
            products.append(prodnames[num])
    return products

def add_nodes(prods,gr):
    '''adds the nodes prods in to the gr'''
    for products in prods:
        if gr.has_node(products):
            continue
        else:
            gr.add_node(products)
    return True

def add_edges(products,grap,stringname):
    '''adds the edge to the stringname of the grap for all combinations of products'''
    add_nodes(products,grap)
    mypermuts=itertools.permutations(products,2)
    for tupl in mypermuts:
        if grap.has_edge(tupl[0],tupl[1]):
            grap[tupl[0]][tupl[1]]['weight']+=1
        else:
            grap.add_edge(tupl[0],tupl[1],weight=1)
    return True

def getinversepop(graphin):
    '''get the inverse of popularity as the personalization weight'''
    Gweights=graphin.out_degree(graphin.nodes(),'weight')
    print "Gweights,",sorted(Gweights.items(), key=operator.itemgetter(1))
    for key in Gweights:
        Gweights[key]=1.0/(0.1+Gweights[key])
        #Gweights[key]=1.0
    return Gweights

def normalizenodes(graphin):
    '''normalizes the outgoing nodes in the graphin'''
    Gweights=graphin.out_degree(graphin.nodes(),'weight')
    edges=graphin.edges()
    for u,v in edges:
        graphin[u][v]['weight']=graphin[u][v]['weight']*1.0/Gweights[u]
        print u,v,graphin[u][v]['weight']


G=nx.DiGraph()
fin=open(filein)
for linenum,line in enumerate(fin):
    if linenum==0:
        print "linenum is",linenum
        headdict,headlist=makehead(line)
        allcols=range(len(headlist))
        cols=getcolslist(args.cols)
        if includecols:
            igcols=list(set(allcols).difference(set(cols)))
        else:
            igcols=cols
        print 'ignoring,',igcols
    else:
        linesplit=line.strip().split(dlm)
        productsholding=getproducts(linesplit,igcols,headlist)
        #print 'productholding is',productsholding
        add_edges(productsholding,G,'weight')
        if linenum==-1:
            break

'''
normalizenodes(G)
nx.draw(G)
plt.draw()
plt.show()
'''
invpersonalization=getinversepop(G)
print "inverse personalization is,",invpersonalization
#pagedict=nx.pagerank(G,personalization=invpersonalization,nstart=invpersonalization)
pagedict=nx.pagerank(G,nstart=invpersonalization)
sorted_x = sorted(pagedict.items(), key=operator.itemgetter(1))
print sorted_x
