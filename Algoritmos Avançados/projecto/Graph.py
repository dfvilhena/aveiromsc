import random as rand
import matplotlib.pyplot as plt

class Graph():

    def __init__(self, graph_dict=None, random=False, n=2, m=1, position_dict=None):
        if graph_dict == None:
            graph_dict = {}

        if random:
            for v in range(0, n):
                graph_dict[v] = []
            edge_list = []
            for k in range(0, m):
                v = rand.choices(list(graph_dict.keys()), k=2)
                while v[0] == v[1] or set(v) in edge_list:
                    v = rand.choices(list(graph_dict.keys()), k=2)
                graph_dict[v[0]].append(v[1])
                graph_dict[v[1]].append(v[0])
                edge_list.append(set(v))

        max_rand = len(list(graph_dict.keys()))

        if position_dict == None:
            v_positions = {}
            if len(list(graph_dict.keys())) > 0:
                for v in list(graph_dict.keys()):
                    pos = [rand.randrange(max_rand), rand.randrange(max_rand)]
                    while pos in v_positions.values():
                        pos = [rand.randrange(max_rand), rand.randrange(max_rand)]
                    v_positions[v] = pos

            self.__v_positions = v_positions

        else:
            self.__v_positions = position_dict

        self.__graph_dict = graph_dict
        

    def get_graph(self):
        return self.__graph_dict

    def get_vertices(self):
        return list(self.__graph_dict.keys())

    def get_number_of_vertices(self):
        return len(list(self.__graph_dict.keys()))

    def get_vertices_positions(self):
        return self.__v_positions

    def generate_edges(self):
        edges = []
        for v in self.__graph_dict:
            for n in self.__graph_dict[v]:
                if {v, n} not in edges:
                    edges.append({v, n})

        return [list(e) for e in edges]

    def get_edges(self):
        return self.generate_edges()

    def get_number_of_edges(self):
        return len(self.generate_edges())

    def show_graph(self, graphcolor="b", textcolor="w", filename="", minimum=False):
        
        fig = plt.figure(num=1)
        a = 0.1
        if minimum:
            a=1

        v_list = list(self.__graph_dict.keys())
        for v in v_list:
            pos = self.__v_positions[v]
            plt.plot(pos[0], pos[1], "o", color=graphcolor, markersize=20)
            plt.text(pos[0], pos[1], str(v), color=textcolor)


        for v in v_list:
            edge_points = self.__graph_dict[v]
            
            if len(edge_points) > 0:
                point1 = self.__v_positions[v]
                for c in self.__graph_dict[v]:
                    point2 = self.__v_positions[c]
                    x = [point1[0], point2[0]]
                    y = [point1[1], point2[1]]
                    plt.plot(x, y, 'k-', color=graphcolor, alpha=a)

        min_x = min([p[0] for p in self.__v_positions.values()])
        max_x = max([p[0] for p in self.__v_positions.values()])

        min_y = min([p[1] for p in self.__v_positions.values()])
        max_y = max([p[1] for p in self.__v_positions.values()])

        plt.xlim([min_x-1, max_x+1])
        plt.ylim([min_y-1, max_y+1])
        plt.axis("off")
        if filename != "":
            plt.savefig(filename, bbox_inches="tight")

        #plt.show()

        return fig