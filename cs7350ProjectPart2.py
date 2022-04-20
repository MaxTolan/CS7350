# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:01:32 2022

@author: Max
"""
class SLVO:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
    
   
    def adjacencyListStringToArrays(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edgesDict = {}
        # edges = []
        # edgeQuantity = []
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            # edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            # edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        # edges.append(listAsList[ int(startPoints[-1] )-1 :-1])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] )-1 :-1])
        # edgeQuantity.append(len(listAsList[int(startPoints[-1])-1 : -1]))
        print(edgesDict)
        print(edgeQuantityDict)
        
        return edgesDict, edgeQuantityDict
    
    def getMinValue(self, inputlist):
        minValue = min(inputlist)
        minIndex=inputlist.index(minValue)
        return minIndex
    
    # TODO: Switch it so that it takes a dictionary instead
    def removeMin(self, edgeList, edgeQuantity, vertexList):
        minValue = self.getMinValue(edgeQuantity)
        # TODO: Figure out how to get the original index of the list. If I insert min value, then I risk duplicate indexes
        edgeQuantity.clear()
        smallestVertex = edges.pop(minValue)
        for i in smallestVertex:
            if int(i) > minValue:
                connectedVertex = edges[int(i)-1]
            else:
                connectedVertex = edges[int(i)]
            connectedVertex.remove(str(minValue))
        
        for i in range(len(edges)):
            edgeQuantity.append(len(edges[i]))
        return edgeList, edgeQuantity, vertexList
if __name__ == "__main__": 

    testCase1 = '5	6	9	11	15	19	3	2	4	3	2	0	1	3	4	0	1	4	2	3	0	2'
    testCase2 = '5	6	10	14	17	20	3	2	4	1	4	3	2	0	3	0	1	2	0	1	1	0'
    testCase3 = '5	6	9	13	17	20	1	2	3	4	0	3	2	0	3	4	1	1	2	0	1	2'
    testCase4 = '5	6	8	10	12	14	4	1	2	0	3	1	4	2	0	3'
    testCase5 = '5	6	10	14	18	22	4	3	2	1	4	3	2	0	4	3	1	0	4	2	1	0	3	2	1	0'
    
    slvo = SLVO(testCase1)
    edges, edgeQuantity = slvo.adjacencyListStringToArrays()

    edges, edgeQuantity, vertexList = slvo.removeMin(edges, edgeQuantity, [])
    print(edges)
    print(edgeQuantity)
    # print(edges)
    # print(edgeQuantity)