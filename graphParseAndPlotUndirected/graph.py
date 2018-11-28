'''
Created on Nov 8, 2014

@author: Gary
'''

class graph:
    def __init__(self):
        self.vertexNameArray       = [] # vertex names in an array
        self.vertexIndexMap        = {} # vertex names to index dictionary
        self.vertexPositionArray   = [] # x,y pair position array
        self.edgeArray             = [] # array of (vertex index pair, weight)
    
    def addVertex(self, name, x, y):
        self.vertexIndexMap[name] = self.vCount()
        self.vertexNameArray.append(name)
        self.vertexPositionArray.append((x,y))
        
    def addEdge(self, vName1, vName2, weight):
        self.edgeArray.append((self.vertexIndexMap[vName1],self.vertexIndexMap[vName2],weight))
        
    def newEdgeWeight(self, i_edge, new_weight):
        self.edgeArray[i_edge][2] = new_weight
        
    def vCount(self): return len(self.vertexNameArray)
    
    def eCount(self): return len(self.edgeArray)
    
    # Access functions for vertex information
    def  vX(   self, i): return self.vertexPositionArray[i][0]
    def  vY(   self, i): return self.vertexPositionArray[i][1]
    def  vName(self, i): return self.vertexNameArray[i]
    def  vIndx(self, v): return self.vertexIndexMap[v]
    
    # Access functions for edge information
    def  eV0X( self, i): return self.vertexPositionArray[self.edgeArray[i][0]][0]
    def  eV0Y( self, i): return self.vertexPositionArray[self.edgeArray[i][0]][1]
    def  eV1X( self, i): return self.vertexPositionArray[self.edgeArray[i][1]][0]
    def  eV1Y( self, i): return self.vertexPositionArray[self.edgeArray[i][1]][1]
    def  eWght(self, i): return self.edgeArray[i][2]