"""
Author: Sujayyendhiren RS

Summary: 
    Djikstra's algorithm. Leverages python's heapq implementation.
    Kindly email any suggestion(s) or issue(s) to sujayy1983@gmail.com

Key notables:
 (i) Tested on python 3.6
 (ii) This file includes two testcases. Kindly comment/uncomment the desired Test. 

Steps to create graph and run this algorithm

Step I   - Create a Graph object
           Example: graph = Graph()
          
Step II  - Create a graph edges by repeating the following 
           Example: graph.add_node('A', 'B', 10)

Step III - Run the algorithm by specifying start and end nodes
           Example: graph.dijkstras(start='A', end='F')

Step IV  - Print results (using recursion)
           Example: print_results(start='A', end='F', result=graph.previous)

             
"""

import json
from heapq import heappop, heappush

#---------------------------#
# Global vars for info msgs #
#---------------------------#
width = 80

class Graph(object):
    """ Graph for Djikstra's algorithm"""

    def __init__(self):
        """ Graph initialization """
        
        #-----------------------------------------------#
        # Actual graph links are store in the following #
        #-----------------------------------------------#
        self.graph = {}
        
        self.visited  = []
        self.vertices = []
        
        self.distance = {}
        self.previous = {}

    def add_node(self, elem, neighbor, distance):
        """ 
            Description: Add a node into directed graph
        
            @parameters
            elem     - is source node name in the graph
            neighbor - target node name in the graph
            distance - distance between the nodes
        """
        if elem not in self.vertices:
            self.vertices.append(elem)

        if neighbor not in self.vertices:
            self.vertices.append(neighbor)
        
        if elem not in self.graph:
            self.graph[elem] = {}
        
        if neighbor not in self.graph:
            self.graph[neighbor] = {}
            
        self.graph[elem][neighbor] = distance
        
    def dijkstras(self, start, end):
        """ Djikstra's algorithm implemented based on the pseudocode
            http://www.gitta.info/Accessibiliti/en/html/Dijkstra_learningObject1.html
            
            start - Node name from where we start applying djikstra's algorithm
            end   - Node upto for which we are trying to find shortest path
        """
        #---------------------#
        # initialize distance #
        #---------------------#
        for vertex in self.vertices:
            self.distance[vertex] = 99999999
            if vertex == start:
                self.distance[vertex] = 0

            self.previous[vertex] = None
        
        priorque = []; node = start; dist = 0
        
        while self.vertices:
            
            #---------------------------#
            # Skip already visited node #
            #---------------------------#
            if node in self.visited:
                dist, node = heappop(priorque)
                continue
            
            #------------------------------#
            # Core algorithm logic is here #
            #------------------------------#
            for neighbor in self.graph[node]:
                if self.graph[node][neighbor] + self.distance[node] < self.distance[neighbor]:
                    self.distance[neighbor] = self.graph[node][neighbor] + self.distance[node]
                    self.previous[neighbor] = node
                heappush(priorque, (self.distance[neighbor], neighbor))
            
            #---------------------------#
            # if check is extra caution #
            #---------------------------#
            if node in self.vertices:
                self.vertices.pop(self.vertices.index(node))
                self.visited.append(node)
            
            #--------------------------------#
            # Retrieve next node of interest #
            #--------------------------------#
            if priorque:
                dist, node = heappop(priorque)
            else:
                print("Ideally we shouldnt reach here.")
                print("Debug: {}".format(self.vertices))
                break
            
def print_results(start, end, result):
    """ Print results """
    
    node = end
    
    if node in result and result[node] != None:
        print_results(start, result[node], result)
        print("--> {}".format(node), end='')
    else:
        if result[node] == None and start == node:
            msg = "Result"; line = int((width - len(msg) - 2)/2)*'-'
            print("\n{} {} {}".format(line, msg, line))
            print("{}".format(node), end='')
        else:
            print("Warning: There is a problem - {}".format(node))
        
if __name__ == "__main__":
    
    #--------------#
    # Create Graph #
    #--------------#
    graph = Graph()
    
    #--------#
    # Test 1 #
    #--------#
    # graph.add_node('A', 'B', 10)
    # graph.add_node('A', 'C', 2)
    # graph.add_node('C', 'B', 3)
    # graph.add_node('C', 'E', 1)
    # graph.add_node('B', 'F', 1)
    # graph.add_node('E', 'F', 5)

    #--------#
    # Test 2 #
    #--------#
    graph.add_node('A', 'B', 10)
    graph.add_node('A', 'C', 2)
    graph.add_node('C', 'B', 2)
    graph.add_node('C', 'E', 1)
    graph.add_node('B', 'F', 3)
    graph.add_node('E', 'F', 5)

    #--------------------------#
    # Run dijkstra's algorithm #
    #--------------------------#
    graph.dijkstras(start='A', end='F')

    msg = "Calculated costs for verification"; line = int((width - len(msg) - 2)/2)*'-'
    print("{} {} {}".format(line, msg, line))
    print(graph.distance)
    print('-'*width)
    #------------------------------------------------#
    # Print shortest path from source to destination #
    #------------------------------------------------#
    print_results(start='A', end='F', result=graph.previous)
    
    msg = "Test ends here"; line = int((width - len(msg) - 2)/2)*'-'
    print("\n{} {} {}".format(line, msg, line))
