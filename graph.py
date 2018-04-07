import pprint
import numpy
from random import randint, choice


class Graph:
    def __init__(self, dic={}):
        if dic is not None:
            self.graph = {}
            for pn, l in dic.items():
                self.graph[pn] = l
                for (node, v) in l:
                    self.graph.setdefault(node, [])
        else:
            self.graph = {}

    def addNode(self, node):
        return self.graph.setdefault(node, [])

    def getNodes(self):
        return list(set(map(lambda x: x, self.graph.keys())))

    def addEdge(self, label1, label2):
        if label1 in self.graph.keys() and label2 in self.graph.keys():
            self.graph[label1].add(label2)

    def removeEdge(self, nodeFrom, nodeTo):
        self.graph[nodeFrom] = list(filter(lambda x: x[0] != nodeTo, self.graph.setdefault(nodeFrom, [])))

    def display(self):
        pprint.pprint(self.graph)

    def children(self, label):
        if label in self.graph.keys():
            return self.graph[label]
        return set()

    def getEdgesFrom(self, node, defaultValue=[]):
        return self.graph.get(node, defaultValue)

    def getEdgesTo(self, node):
        edges = []
        for (key, children) in self.graph.items():
            for (childNode, edgeValue) in children:
                if (childNode == node):
                    edges.append((key, edgeValue))
        return edges

    def getEdgeValue(self, nodeFrom, nodeTo, defaultValue=None):
        children = self.getEdgesFrom(nodeFrom)
        res = list(filter(lambda x: x[0] == nodeTo, children) )
        if res:
            return res[0][1]
        else:
            return defaultValue

    def getAllEdges(self):
        return sum(list(map(lambda x: [(x[0], y[0], y[1] ) for y in x[1]] , self.graph.items())),[])

    def nodeExists(self, node):
        if self.getEdgesFrom(node, None):
            return True
        for (nodeFrom, children) in self.graph.items():
            for (nodeTo,value) in children:
                if nodeTo == node:
                    return True
        return False

    def setEdgeValue(self, nodeFrom, nodeTo, value):
        children = self.getEdgesFrom(nodeFrom, None)
        if children:
            found = False
            for i, edge in enumerate(children):
                if edge[0] == nodeTo:
                    found = True
                    children[i] = (nodeTo, value)
                    break
            if not found:
                children.append((nodeTo, value))
        else:
            self.graph[nodeFrom] = [(nodeTo, value)]
        if not self.nodeExists(nodeTo):
            self.addNode(nodeTo)
        return self

    def nodeNumber(self):
        return len(self.graph)

    def edgeNumber(self):
        return sum(len(x) for x in self.graph.itervalues())

    def getNpMatrix(selfs):
        numpy.matrix

    def fmap(self, f):
        returnedGraph = {}

        for (node, children) in self.graph.items():
            returnedGraph[node] = list(map(lambda x: (x[0], f(x[1])), children))
        return Graph(returnedGraph)





class MatrixGraph(Graph):
    def __init__(self, dic={}):
        if dic is not None:
            self.matrix = {}
        else:
            self.matrix = {}

    def addNode(self, label):
        pass

    def getNodes(self):
        pass

    def addEdge(self, label1, label2):
        pass

    def display(self):
        pprint.pprint(self.matrix)

    def children(self, label):
        pass

    def importCSV(self, path):
        pass

    def random(self, n, q):
        pass