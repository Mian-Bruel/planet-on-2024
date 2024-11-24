import numpy as np


class PathFinder:
    def __init__(self, p, c, d, target=3000, s=0, precision=100):
        self.points = p
        self.connections = c
        self.distances = d
        self.target = target
        self.start = s
        self.precision = precision

        self.best_solution = None
        self.best_abs_distance = None

    def get_closest_path(self):
        solution = [self.start]
        edges_used = {}
        nodes_used = {}
        current_distance = 0

        for p in range(len(self.points)):
            nodes_used[p] = 0

        nodes_used[self.start] += 1

        self.best_solution = None
        self.best_abs_distance = None

        self.get_closest_path_recursive(solution, edges_used, nodes_used, current_distance)

        return self.best_solution

    def get_closest_path_recursive(self, solution, edges_used, nodes_used, current_distance):
        current_edge = solution[-1]

        if self.best_abs_distance is not None and self.best_abs_distance < self.precision:
            return

        if current_edge == self.start and len(solution) > 1:

            abs_distance = abs(self.target - current_distance)

            if self.best_abs_distance is None or abs_distance < self.best_abs_distance:
                self.best_abs_distance = abs_distance
                self.best_solution = solution.copy()

            return

        closest_edges = list(np.where(self.connections[current_edge, :])[0])
        closest_edges.sort(key=lambda x: (edges_used.get(x, 0), nodes_used.get(x, 0)))

        for closest_edge in closest_edges:
            edge_representation = self.get_edge_representation(current_edge, closest_edge)

            used_count = edges_used.get(edge_representation, 0)

            if used_count >= 2:
                continue

            new_distance = current_distance + self.distances[current_edge][closest_edge]
            min_distance = new_distance + self.distances[closest_edge][self.start]

            if self.best_abs_distance is not None and min_distance - self.target > self.best_abs_distance:
                continue

            edges_used[edge_representation] = used_count + 1
            nodes_used[closest_edge] += 1
            solution.append(closest_edge)

            self.get_closest_path_recursive(solution, edges_used, nodes_used, new_distance)

            del solution[-1]
            edges_used[edge_representation] -= 1
            nodes_used[closest_edge] -= 1

    @staticmethod
    def get_edge_representation(p1, p2):
        if p1 > p2:
            return p1, p2
        else:
            return p2, p1
