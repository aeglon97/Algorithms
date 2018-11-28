'''
Created on Nov 8, 2014

@author: Gary
'''
import fileinput
import graph
import matplotlib.pyplot as plt
import random
import math

vertices = []
edges = []

# Parse graph.txt and populate mygraph structure.
mygraph = graph.graph()
isVertices = True
for line in fileinput.input("graph2.txt"):
    if isVertices:
        if "----------" in line:
            isVertices = False
        else: #read vertices in this part
            split = line.split()
            mygraph.addVertex(split[0],float(split[1]),float(split[2]))
            v = split[0]
            vertices.append(v)
    else:     #read    edges in this part
        split = line.split()
        mygraph.addEdge(split[0], split[1], float(split[2]))
        e = (float(split[2]), split[0], split[1])
        edges.append(e)
    #print(line, isVertices)

''' TODO: this is a collection of edges that are displayed in a more emphasized way '''
mst_edges = []#mst_edges = [0,2]

# Display vertices
minX = minY =  1e1000
maxX = maxY = -1e1000
for iV in range (0, mygraph.vCount()):
    x = mygraph.vX(iV)
    y = mygraph.vY(iV)
    plt.plot(x,y,'wo', ms = 15)
    minX = min(minX,x)
    minY = min(minY,y)
    maxX = max(maxX,x)
    maxY = max(maxY,y)
    plt.text(x, y, mygraph.vName(iV), ha = 'center', va = 'center')
    padX = .02*(maxX-minX)+5
    padY = .02*(maxY-minY)+5
    plt.axis([minX-padX, maxX+padX, minY-padY, maxY+padY])

# Display edges
for iE in range (0, mygraph.eCount()):
    x0 = mygraph.eV0X(iE)
    y0 = mygraph.eV0Y(iE)
    x1 = mygraph.eV1X(iE)
    y1 = mygraph.eV1Y(iE)
    xM = (x0+x1)/2
    yM = (y0+y1)/2
    plt.plot([x0,x1],[y0,y1],color='0.8')
    plt.text(xM, yM, mygraph.eWght(iE))

# Display emphasized edges
for iTE in mst_edges:
    x0 = mygraph.eV0X(iTE)
    y0 = mygraph.eV0Y(iTE)
    x1 = mygraph.eV1X(iTE)
    y1 = mygraph.eV1Y(iTE)
    plt.plot([x0,x1],[y0,y1],'r--')
#----------------------------------------------------------------------------
from queue import PriorityQueue


#
def display(vertices, edges):
    print('visited vertices: ' , vertices)
    print('vertex: ', 'connected to', '\t', 'weight')
    for edge in edges:
        print(edge[0], '\t', edge[1], '\t\t', edge[2]) 

def prim():
    #create empty priority queue
    q = PriorityQueue()
    MST = []
    visitedVertices = []
    
    #select random vertex and set as visited
    newVertex = (random.choice(vertices))
    visitedVertices.append(newVertex)
    
    while len(MST) < (len(vertices) - 1):
        
        #put all unvisited edges from newVertex to priority queue
        for weight, v1, v2 in edges:
            #if either vertex not visited
            if v1 not in visitedVertices or v2 not in visitedVertices:
                if newVertex == v1:
                    q.put((weight, v1, v2))
                elif newVertex == v2:
                    q.put((weight, v1, v2))
        #print('unvisited edges including vertex ', newVertex, ': ')

        #pop cheapest edge and add to MST, mark corresponding vertices as visited
        cheapestEdge = q.get()
 
        if cheapestEdge[1] not in visitedVertices and cheapestEdge[2] in visitedVertices:
            visitedVertices.append(cheapestEdge[1])
            newVertex = cheapestEdge[1]
            MST.append(cheapestEdge)
        elif cheapestEdge[2] not in visitedVertices and cheapestEdge[1] in visitedVertices:
            visitedVertices.append(cheapestEdge[2])
            newVertex = cheapestEdge[2]
            MST.append(cheapestEdge)
            
        '''print('cheapest edge: ' , cheapestEdge)
        print('MST: ', MST)
        print('visited vertices: ', visitedVertices)'''
        
    #display results
    print('=========PRIM MST=========')
    for weight, v1, v2 in MST:
        print(weight , '\t' , v1, '\t', v2)
        
    return MST
        
def kruskal():
    #create empty priority queue
    q = PriorityQueue()
    
    #add edges in p_que sorted by weight
    for e in edges:
        q.put(e)    
    
    #put each vertex in its own set
    vSets = []
    #key = vertex, value = set
    for v in vertices:
        vSets.append([v])
        
    print(vSets)
        
    MST = []
    
    while len(MST) < len(vertices) - 1:
        print('---------------------------------')
        print(vSets)
        cheapestEdge = q.get()
        print('cheapest edge: ', cheapestEdge)
        
        firstV = cheapestEdge[1]
        secondV = cheapestEdge[2]
        print(firstV, secondV)
        
        for v in vSets:
            for w in vSets:
                if firstV in v and secondV in w and firstV not in w and secondV not in v:
                    MST.append(cheapestEdge)
                    v += w
                    vSets.pop(vSets.index(w))
        print(vSets)

        cheapestEdge = q.get()
        print('cheapest edge: ', cheapestEdge)
        
        firstV = cheapestEdge[1]
        secondV = cheapestEdge[2]
        print(firstV, secondV)
        
        for v in vSets:
            for w in vSets:
                #if both vertices not in the same set
                if firstV in v and secondV in w:
                    if firstV not in w and secondV not in v:
                        MST.append(cheapestEdge)
                        v += w
                        vSets.pop(vSets.index(w))
        print(vSets)
                   
    print('=========KRUSKAL MST=========')
    for weight, e1, e2 in MST:
        print(weight , '\t' , e1, '\t', e2)

    return MST
        
    #display results
from collections import defaultdict
import heapq as hp

def dijkstra(sourceVertex, destination):
    shortestPath = []
    dist_edges = {}
    q = []
    hp.heapify(q)
    
    #initialize source
    visitedVertices = []
    dist_edges[sourceVertex] = [0, sourceVertex]
    
    #initialize distances and Q
    for i in range (len(vertices)):
        if vertices[i] != vertices[0]:
            dist_edges[vertices[i]] = [math.inf, vertices[i]]
    print(dist_edges)
    
    while sourceVertex != destination:
        print("----------------------------")
        visitedVertices.append(sourceVertex)
        #add all adjacent edges to queue
        print("adjacent unvisited vertices to " , sourceVertex)
        
        for e in edges:
            if e[1] == sourceVertex and e[2] not in visitedVertices:
                #if current distance + edge < neighbor distance
                current_dist = dist_edges[sourceVertex][0]
                edge_dist = e[0]
                neighbor_dist = dist_edges[e[2]][0]
                
                if current_dist + edge_dist < neighbor_dist:
                    hp.heappush(q, [e[0], e[2]])
                    #update distance of neighbor
                    dist_edges[e[2]][0] = current_dist + edge_dist
                    #update neighbor's source node
                    dist_edges[e[2]][1] = sourceVertex
                    #change priority value
                    
                    k = 0
                    for i in range (len(q)):
                        if q[i] == [e[0], e[2]]:
                            k = i
                    q[k] = q[k-1]
                    q.pop()
                    hp.heapify(q)
                    hp.heappush(q, [dist_edges[e[2]][0], e[2]])
                
            elif e[2] == sourceVertex and e[1] not in visitedVertices:
                #if current distance + edge < neighbor distance
                current_dist = dist_edges[sourceVertex][0]
                edge_dist = e[0]
                neighbor_dist = dist_edges[e[1]][0]
                
                if current_dist + edge_dist < neighbor_dist:
                    hp.heappush(q, [e[0], e[1]])
                    #update distance of neighbor
                    dist_edges[e[1]][0] = current_dist + edge_dist
                    #update neighbor's source node
                    dist_edges[e[1]][1] = sourceVertex
                    #change priority value
                    
                    k = 0
                    for i in range (len(q)):
                        if q[i] == [e[0], e[1]]:
                            k = i
                    q[k] = q[k-1]
                    q.pop()
                    hp.heapify(q)
                    hp.heappush(q, [dist_edges[e[1]][0], e[1]])
        
        print("queue:")
        print(list(q))
        print("visited:")
        print(visitedVertices)
        
        print("updated costs:")
        print(dist_edges)
        min_q = hp.heappop(q)
        minKey = min_q[1]
        
        sourceVertex = minKey
        print("new vertex: " , sourceVertex)

    #display lines
    for key, value in dist_edges.items():
        if (key != value[1]):
            shortestPath.append((value[0], key, value[1]))
         
    return shortestPath

dijkstraPath = dijkstra('a', 'g')     
#kruskalMST = kruskal()       
#primMST = prim()

# Display emphasized edges
def displayMST(MST):
    for w,v1,v2 in MST:
        i1 = mygraph.vIndx(v1)
        x0 = mygraph.vX(i1)
        y0 = mygraph.vY(i1)
        i2 = mygraph.vIndx(v2)
        x1 = mygraph.vX(i2)
        y1 = mygraph.vY(i2)
        plt.plot([x0,x1],[y0,y1],'r--')
       
displayMST(dijkstraPath)
#displayMST(kruskalMST)
#displayMST(primMST)

#plt.show()
