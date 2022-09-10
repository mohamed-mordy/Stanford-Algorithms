#!/usr/bin/env python3

import collections


Edge = collections.namedtuple('Edge', ['tail', 'head'])


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def __repr__(self):
        return str(self.name) + " --> " + str(self.neighbors)

    def add_neighbor(self, edge):
        """ Add a neighbor to this Vertex,
        the input argument should be a literal"""
        if isinstance(edge, Edge):
            self.neighbors.add(edge)


class Graph:

    def __init__(self, directed=False):
        """ The Graph class: """
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """ Add New Vertex to the current this Graph"""
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, edge):
        """ Add and edge to this Graph,
         tail & head are vertex names used as keys in the (key, value) map representing the graph"""
        if edge.tail in self.vertices and edge.head in self.vertices:
            self.vertices[edge.tail].add_neighbor(edge)
            if self.directed:
                self.vertices[edge.head].add_neighbor(edge)
            else:
                self.vertices[edge.head].add_neighbor(Edge(edge.head, edge.tail))
            return True
        else:
            return False

    def print(self):
        for key in sorted(list(self.vertices.keys())):
            print(self.vertices[key])
