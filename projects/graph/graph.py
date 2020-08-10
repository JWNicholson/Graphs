"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
          # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.add_vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertext doesn't exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
                # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex_id)

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
       # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        #crate an empty stack and push starting vertex
        s = Stack()
        s.push(starting_vertex)

        #create a a set to store visited vertices
        visited = set()

        #while stack is not empty
        while s.size > 0:
            #pop first vertex
            v = s.pop()

            #if v not in visited:
            #mark vertext as visited
            visited.add(v)

            #print for debugging
            print(v)

            #add all neighbors to the top of the stack
            for next_vertex in self.get_neighbors(v):
                s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        # create an empty queue and enqueue PATH To the Starting Vertex ID
        q = Queue()
        # q.enqueue([starting_vertex_id])
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
             # dequeue the first PATH
            current_path = q.dequeue()
            # grab the last vertex from the Path
            current_node = current_path[-1]
            
            # check if the vertex has not been visited
            if current_node not in visited:
                # mark it as visited
                visited.add(current_node)
                # then add A Path to its neighbors to the back of the queue
            neighborhood = self.get_neighbors(current_node)

            for neighbor in neighborhood:
                 # make a copy of the path
                next_path = current_path.copy()
                # append the neighbor to the back of the path
                next_path.append(neighbor)

                # is this vertex the target?
                if neighbor == destination_vertex:
                    # return the path
                    return next_path
                # enqueue out new path
                q.enqueue(next_path)    
            
        # return none

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
