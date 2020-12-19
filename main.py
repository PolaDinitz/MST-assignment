from collections import defaultdict
import heapq
import random

# todo: remove later - when done testing
example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}


# todo: change the graph name you want to use
def generate_weight(frm, to):
    return example_graph[frm][to]


# create clique graph
def generate_graph(num_of_vertexes, num_of_edges):
    graph = defaultdict(dict)

    for i in range(num_of_vertexes):
        for j in range(i+1, num_of_edges):
            first = str(i)
            second = str(j)
            weight = random.randint(1, 101)
            graph[first][second] = weight
            graph[second][first] = weight
    return graph


def prim_mst(graph, weight_func):
    # init mst
    mst = defaultdict(set)
    # choose random starting vertex
    starting_vertex = random.choice(list(graph.keys()))

    visited = {starting_vertex}
    edges = [
        (weight_func(starting_vertex, to), starting_vertex, to)
        for to in graph[starting_vertex]
    ]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight_func(to, to_next), to, to_next))
    return make_undirected_graph(mst)


def make_undirected_graph(g):
    new = g.copy()

    for v, edges in g.items():
        for edge in edges:
            if edge not in new:
                new[edge] = set()
            new[edge].add(v)

    return new

def BFS_SP(graph, start, goal): 
    explored = [] 
    queue = [[start]] 

    if start == goal: 
        print("Same Node") 
        return None
      
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
          
        if node not in explored: 
            neighbours = graph[node] 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
                if neighbour == goal: 
                    return new_path
            explored.append(node) 
  
    return None

def update_mst(graph,edge):
    path = BFS_SP(graph,edge[0],edge[1])
    edge_remove = None
    for e in range(len(path[:-1])):
        if(generate_weight(path[e],path[e+1]) > edge[2]):
            edge_remove = (path[e],path[e+1])
            break
    if(edge_remove == None):
        return graph
    elif(type(edge_remove) == tuple):
        new_neighbors = set()
        for n in graph.get(edge_remove[0]):
            if not(n == edge_remove[1]):
                new_neighbors.add(n)
        new_neighbors.add(edge[1])
        graph.update({edge_remove[0]:new_neighbors})
        new_neighbors = set()
        for n in graph.get(edge_remove[1]):
            if not(n == edge_remove[0]):
                new_neighbors.add(n)
        graph.update({edge_remove[1]:new_neighbors})
        a = graph.get(edge[1])
        a.add(edge[0])
        graph.update({edge[1]:a})
        return graph

def print_mst(mst_tree):
    for k, v in mst_tree.items():
        if isinstance(v, dict):
            print_mst(v)
        else:
            print("{0} : {1}".format(k, v))


def main():
    # todo: use later in "prod"
    # some_graph = generate_graph(20, 50)
    mst = prim_mst(example_graph, generate_weight)
    print(mst)
    print_mst(mst)
    pass


if __name__ == '__main__':
    main()
