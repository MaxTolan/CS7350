# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:01:32 2022

@author: Max
"""
import numpy as np

# TODO: Clean up code so that one portion handles the ordering, while the coloringv2 function is its own thing
class SLVO:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        startOfLast = startPoints[-1]
        lastItem = listAsList[-1]
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity

    def minValueFromDict(self, d):
        minValue = min(d.values())
        minList = [key for key, value in d.items() if value == minValue]
        return minList[0] # For multiple acceptable items, just pick the first one 

    def removeMin(self, edgeList, edgeQuantity):
        keyForMinValue = self.minValueFromDict(edgeQuantity)
        smallestVertexEdges = edgeList.pop(keyForMinValue)
        edgeQuantity.pop(keyForMinValue) # Need to update edgeQuantity for next iteration

        for i in smallestVertexEdges:
            vertexEdge = edgeList[int(i)]
            # Is there a way for me to add 1 to the color value each time it is called? 
            if len(vertexEdge)>1:
                vertexEdge.remove(str(keyForMinValue))
            else:
                vertexEdge.pop(0)
        return edgeList, edgeQuantity, keyForMinValue
    
    def keyOrder(self):
        edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity = self.adjacencyListStringToDictAndArray()
        originalEdgesDict = edgesDict
        keyOrderValues = []
        color = {}
        currentColor = 0
        for i in range(numberVertices):
            color[i] = 0
        for i in range(numberVertices):
            edges, edgeQuantity, keyForMinValue = self.removeMin(edgesDict, edgeQuantityDict)
            
            keyOrderValues.insert(0, keyForMinValue)
            
        return keyOrderValues
    
    def edgeListColorOrdering(self, edgesDict):
        keyOrderValues = self.keyOrder()
        keyOrderValues.reverse() #Reverse it because the first one colored is the item in line 0
        edgeListInColorOrdering = []
        count = 0
        indexToKeyValueDict = {}
        for i in keyOrderValues:
            edgeListInColorOrdering.append(edgesDict[i])
            indexToKeyValueDict[count] = i
            count += 1
        return edgeListInColorOrdering, indexToKeyValueDict
    def find_missing(self, lst): # Taken from https://www.geeksforgeeks.org/python-find-missing-numbers-in-a-sorted-list-range/
        return [x for x in range(lst[0], lst[-1]+1) 
                               if x not in lst]
    
    def coloringv2(self, edgesDict, numberVertices, keyOrder):
        result = [-1] * numberVertices
        result[0] = 0 # First item immediately gets color 0
        currentColors = {keyOrder[0]:0}
        for i in range(1, numberVertices):
            forbiddenColors = [] #Set up blank for each vertex
            currentEdges = edgesDict[keyOrder[i]]
            for k in currentEdges:
                forbiddenColors.append(currentColors.get(int(k), -1))
            if not forbiddenColors: # If forbidden colors is empty, then there are no conflicts, so give it 0
                result[i] = 0
                currentColors[keyOrder[i]] = 0
            elif (all(element == -1 for element in forbiddenColors)): # If forbidden colors all equal -1, then give it 0
                result[i] = 0
                currentColors[keyOrder[i]] = 0
            else:
                forbiddenColors.sort()
                availableColors = self.find_missing(forbiddenColors)
                if not availableColors: # If the list has no available numbers, then give it the new max
                    result[i] = forbiddenColors[-1] +1
                    currentColors[keyOrder[i]] = forbiddenColors[-1] +1
                else:
                    result[i] = availableColors[0]
                    currentColors[keyOrder[i]] = availableColors[0]
                
        print(currentColors)
        
    
class SmallestOriginalDegreeLast:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
        # print(edgesDict)
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    def dictionaryKeysToSortedArray(self, d):
        array = []
        for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
            array.append(k)
        return array

class RandomOrder:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    def takeKeysFromDictAndPutInArrayRandomly(self, dictionary):
        array = [-1] # need to insert a -1 into it so that randint doesn't get irritated that it needs to pick a number between 0 and 0 
        for k in dictionary:
            array.insert(np.random.randint(0, len(array)), k)
        array.remove(-1)
        return array
    
class BiggestLastVertexOrdering:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDict(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
        # print(edgesDict)
        return edgesDict, edgeQuantityDict, numberVertices

    def maxValueFromDict(self, d):
        maxValue = max(d.values())
        maxList = [key for key, value in d.items() if value == maxValue]
        return maxList[0] # For multiple acceptable items, just pick the first one 

    def removeMax(self, edgeList, edgeQuantity):
        keyForMaxValue = self.maxValueFromDict(edgeQuantity)
        largestVertexEdges = edgeList.pop(keyForMaxValue)
        edgeQuantity.pop(keyForMaxValue) # Need to update edgeQuantity for next iteration

        for i in largestVertexEdges:
            vertexEdge = edgeList[int(i)]
            # Is there a way for me to add 1 to the color value each time it is called? 
            vertexEdge.remove(str(keyForMaxValue))
        return edgeList, edgeQuantity, keyForMaxValue
    
    def organizeOutput(self):
        edges, edgeQuantity, numberVertices = self.adjacencyListStringToDict()
        originalEdges = edges
        keyOrder = []
        finalColor = {}
        currentColor = 0
        for i in range(numberVertices):
            edges, edgeQuantity, keyForMinValue = self.removeMax(edges, edgeQuantity)
            finalColor[keyForMinValue] = currentColor
            currentColor += 1
            keyOrder.insert(0, keyForMinValue)
            
        return keyOrder, finalColor
class BiggestOriginalDegreeLast:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
   
    def adjacencyListStringToDictAndArray(self): 
        listAsList = self.List.split('\t')
        numberVertices = int(listAsList[0])
        startPoints = listAsList[1 : numberVertices+1]
        edges = []
        edgeQuantity = []
        edgesDict = {}
        edgeQuantityDict = {}
        for i in range(numberVertices -1) : 
            edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
            edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
            edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
        edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
        edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
        # print(edgesDict)
        return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    def dictionaryKeysToSortedArray(self, d):
        array = []
        for k in sorted(d, key=lambda k: len(d[k]), reverse=False):
            array.append(k)
        return array

class VerticesOrganizedAlphabetically:
    def __init__(self, adjacencyList):
        self.List = adjacencyList
    def adjacencyListStringToDictAndArray(self): 
            listAsList = self.List.split('\t')
            numberVertices = int(listAsList[0])
            startPoints = listAsList[1 : numberVertices+1]
            edges = []
            edgeQuantity = []
            edgesDict = {}
            edgeQuantityDict = {}
            for i in range(numberVertices -1) : 
                edges.append(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
                edgeQuantity.append(len(listAsList[int(startPoints[i]) : int(startPoints[i+1])]))
                edgesDict[i] = listAsList[int(startPoints[i]) : int(startPoints[i+1])]
                edgeQuantityDict[i] = len(listAsList[int(startPoints[i]) : int(startPoints[i+1])])
            edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] ) :]
                # edgesDict[numberVertices-1] = listAsList[ int(startPoints[-1] )-1 :-1]
            edgeQuantityDict[numberVertices -1] = len(listAsList[ int(startPoints[-1] ) :])
            # print(edgesDict)
            return edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity
    
    """Given an int32 number, print it in English."""
    def int_to_en(self, num): # Taken from https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
        d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
            6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
            11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
            15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
            19 : 'nineteen', 20 : 'twenty',
            30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
            70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert(0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0: return d[num]
            else: return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < k):
            if num % 100 == 0: return d[num // 100] + ' hundred'
            else: return d[num // 100] + ' hundred and ' + self.int_to_en(num % 100)

        if (num < m):
            if num % k == 0: return self.int_to_en(num // k) + ' thousand'
            else: return self.int_to_en(num // k) + ' thousand, ' + self.int_to_en(num % k)

        if (num < b):
            if (num % m) == 0: return self.int_to_en(num // m) + ' million'
            else: return self.int_to_en(num // m) + ' million, ' + self.int_to_en(num % m)

        if (num < t):
            if (num % b) == 0: return self.int_to_en(num // b) + ' billion'
            else: return self.int_to_en(num // b) + ' billion, ' + self.int_to_en(num % b)

        if (num % t == 0): return self.int_to_en(num // t) + ' trillion'
        else: return self.int_to_en(num // t) + ' trillion, ' + self.int_to_en(num % t)

        raise AssertionError('num is too large: %s' % str(num))
    def dictEnglishToIntegers(self, numberVertices):
        # This function creates a dictionary that reverses the english to integer
        dictionaryValues = {}
        for i in range(numberVertices):
            dictionaryValues[self.int_to_en(i)] = i
        return dictionaryValues

    def dictKeyNumberToEnglish(self, dictionary):
        englishDictionary = {}
        for i in dictionary:
            englishDictionary[self.int_to_en(i)] = dictionary[i]
        return englishDictionary
    def dictionaryKeysToSortedArray(self, d):
        array = d.keys()
        return sorted(array)
    
if __name__ == "__main__": 

    testCase1 = '5	6	9	11	15	19	3	2	4	3	2	0	1	3	4	0	1	4	2	3	0	2'
    testCase2 = '5	6	10	14	17	20	3	2	4	1	4	3	2	0	3	0	1	2	0	1	1	0'
    testCase3 = '5	6	9	13	17	20	1	2	3	4	0	3	2	0	3	4	1	1	2	0	1	2'
    testCase4 = '5	6	8	10	12	14	4	1	2	0	3	1	4	2	0	3'
    testCase5 = '5	6	10	14	18	22	4	3	2	1	4	3	2	0	4	3	1	0	4	2	1	0	3	2	1	0'
    testCase6 = '4	5	8	11	14	3	2	1	3	2	0	3	1	0	2	1	0'
    slvo = SLVO(testCase6)
    edgesDictSLVO, edgeQuantityDictSLVO, numberVerticesSLVO, edgesSLVO, edgeQuantitySLVO = slvo.adjacencyListStringToDictAndArray()
   
    print(edgesDictSLVO)
    keyorderSLVO = slvo.keyOrder()
    print(keyorderSLVO)
    edgeListInColorOrderingSLVO, indexToKeyValueDict = slvo.edgeListColorOrdering(edgesDictSLVO)
    # slvo.greedycoloring(edgeListInColorOrderingSLVO, numberVerticesSLVO, indexToKeyValueDict)
    slvo.coloringv2(edgesDictSLVO, numberVerticesSLVO, keyorderSLVO)
    smallestOriginalDegreeLast = SmallestOriginalDegreeLast(testCase1)
    edgesDictSmallestOriginal, edgesQuantityDictSmallestOriginal, numberVerticesSmallestOriginal, edgesSmallestOriginal, edgeQuantitySmallestOriginal = smallestOriginalDegreeLast.adjacencyListStringToDictAndArray()
    sortedEdges = smallestOriginalDegreeLast.dictionaryKeysToSortedArray(edgesDictSmallestOriginal)
    # print(edgesSmallestOriginal)
    randomOrder = RandomOrder(testCase1)
    edgesDictRandom, edgeQuantityDictRandom, numberVerticesRandom, edgesRandom, edgeQuantityRandom = randomOrder.adjacencyListStringToDictAndArray()
    # print(randomOrder.takeKeysFromDictAndPutInArrayRandomly(edgesDictRandom))

    biggestLastVertexOrder = BiggestLastVertexOrdering(testCase1)
    keyOrderBLVO, finalcolor = biggestLastVertexOrder.organizeOutput()

    verticesOrganizedAlphabetically = VerticesOrganizedAlphabetically(testCase1)
    edgesDict, edgeQuantityDict, numberVertices, edges, edgeQuantity = verticesOrganizedAlphabetically.adjacencyListStringToDictAndArray()
    englishDict = verticesOrganizedAlphabetically.dictKeyNumberToEnglish(edgesDict)
    sortedEnglish = verticesOrganizedAlphabetically.dictionaryKeysToSortedArray(englishDict)
    dictionaryEnglishToInteger = verticesOrganizedAlphabetically.dictEnglishToIntegers(numberVertices)
    
