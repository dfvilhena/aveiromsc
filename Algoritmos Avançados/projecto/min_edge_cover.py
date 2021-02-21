from copy import deepcopy
from Graph import Graph
import random
import statistics as st

def exhaustive_search(graph):

    edge_list = graph.get_edges()

    n_vertices = graph.get_number_of_vertices()
    n_edges = graph.get_number_of_edges()

    min_edge_cover = n_edges    

    for i in range(0, len(edge_list)):
        edge1 = edge_list[i]
        small_set = []
        small_set.append(edge1)
        for j in range(0, len(edge_list)):
            if edge_list[j] != edge1:
                small_set.append(edge_list[j])

            vertices_in_edges = []
            for edge in small_set:
                for vertix in edge:
                    vertices_in_edges.append(vertix)

            if len(set(vertices_in_edges)) == n_vertices:

                if len(small_set) < min_edge_cover:
                    min_edge_cover = len(small_set)
                    min_edges = deepcopy(small_set)

    return min_edge_cover, min_edges

def vertex_weights(graph):
    graph_dict = graph.get_graph()
    n_edges = len(graph.get_edges())
    v_list = graph.get_vertices()

    for v in v_list:
        graph_dict[v] = [d for d in graph_dict[v] if d > v]

    #print(graph_dict)

    vertex_weight = {}
    for v in v_list:
        vertex_weight[v] = len(graph_dict[v])/n_edges
    #print(vertex_weight)

    vertex_cumulative = {}
    for v in vertex_weight:
        vertex_cumulative[v] = 0
        for u in list(vertex_weight.keys())[:v]:
            vertex_cumulative[v] += vertex_weight[u]

    return vertex_weight, vertex_cumulative

def probabilistic_search(graph):
    
    graph_dict = graph.get_graph()
    v_list = graph.get_vertices()

    for v in v_list:
        graph_dict[v] = [d for d in graph_dict[v] if d > v]

    weights, vertex_cumulative = vertex_weights(graph)
    #print(vertex_cumulative)
    vertices_visited = []

    edge_list = []

    thermalization_steps = 10

    while len(set(vertices_visited)) < len(v_list):

        choice_list = []
        endpoint_list = []
        
        for k in range(0, thermalization_steps):
            random_caller = random.random()
            choice = 0
            for v in vertex_cumulative:
                if random_caller >= vertex_cumulative[v] and random_caller < vertex_cumulative[v+1]:
                    choice = v
            choice_list.append(choice)
        choice = int(st.median(choice_list))
        
        endpoints_from_choice = graph_dict[choice]
        endpoints_from_choice.sort()
        print(endpoints_from_choice)

        endpoint_weights = {}
        for e in endpoints_from_choice:
            endpoint_weights[e] = weights[e]
        endpoint_cumulative = {}
        total_endpoint_weight = 0
        k = 0
        for e in endpoint_weights:
            endpoint_cumulative[e] = 0
            total_endpoint_weight += endpoint_weights[e]
            for u in list(endpoint_weights.keys())[:k]:
                endpoint_cumulative[e] += endpoint_weights[u]
            k+=1
        
        for e in endpoint_cumulative:
            endpoint_cumulative[e] /= total_endpoint_weight


        for k in range(0, thermalization_steps):
            random_caller = random.random()
            endpoint = 0
            for v in range(0, len(vertex_cumulative.keys())):
                key1 = list(vertex_cumulative.keys())[ v]
                key2 = list(vertex_cumulative.keys())[v+1]
                if random_caller >= endpoint_cumulative[key1] and random_caller < endpoint_cumulative[key2]:
                    endpoint = key1
            endpoint_list.append(endpoint)
        endpoint = int(st.median(endpoint_list))







        vertices_visited.append(choice)
        vertices_visited.append(endpoint)
        
        edge_list.append([choice, endpoint])
        graph_dict[choice].remove(endpoint)

        vertex_cumulative = vertex_weights(graph)

        #print(endpoints_from_choice)
        #print(vertex_cumulative)

    return len(edge_list), edge_list



    









def probabilistic_results(graph, N=100):
    
    summ=0
    summ_sq = 0

    for k in range(0, N):
        min_edge_cover,_ = probabilistic_search(graph)
        summ += min_edge_cover
        summ_sq += min_edge_cover**2

    average = summ/N
    variance = summ_sq/(N-1) - summ**2 / (N*(N-1))

    return average, variance

def get_min_edge_cover(graph, method="exhaustive"):

    if method == "exhaustive":
        min_edge_cover, min_edges = exhaustive_search(graph)
    if method == "probabilistic":
        min_edge_cover, min_edges = probabilistic_search(graph)

    return min_edge_cover, min_edges

def get_min_graph(graph, method="exhaustive"):

    min_edge_cover, min_edges = get_min_edge_cover(graph, method=method)

    print("The minimum number of edges needed to cover all vertices is %d and they are:" % min_edge_cover)
    print(min_edges)

    min_graph_dict = {}
    for edge in min_edges:
        for i in range(0, len(edge)):
            if edge[i] not in min_graph_dict.keys():
                min_graph_dict[edge[i]] = []
                min_graph_dict[edge[i]].append(edge[i-1])
            else:
                min_graph_dict[edge[i]].append(edge[i-1])
    
    return Graph(graph_dict=min_graph_dict, position_dict=graph.get_vertices_positions())