import math
import random
import visualize_tsp
import matplotlib.pyplot as plt


class SimAnneal(object):
    def __init__(self, coords, city_distance, cities, T=-1, alpha=-1, stopping_T=-1, stopping_iter=-1):
        self.coords = coords
        self.cities = cities
        self.city_distance = city_distance
        self.N = len(coords)
        self.T = math.sqrt(self.N) if T == -1 else T
        self.T_save = self.T  # save inital T to reset if batch annealing is used
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temperature = 1e-8 if stopping_T == -1 else stopping_T
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1

        self.nodes = [i for i in range(self.N)]

        self.best_solution = None
        self.best_distance = float("Inf")
        self.distance_list = []

    def initial_solution(self):
        """
        Greedy algorithm to get an initial solution (closest-neighbour).
        """
        cur_node = random.choice(self.nodes)  # start from a random node
        solution = [cur_node]

        free_nodes = set(self.nodes)
        free_nodes.remove(cur_node)
        while free_nodes:
            next_node = min(free_nodes, key=lambda x: self.dist(cur_node, x))  # nearest neighbour
            free_nodes.remove(next_node)
            solution.append(next_node)
            cur_node = next_node

        cur_dist = self.distance(solution)
        if cur_dist < self.best_distance:  # If best found so far, update best Distance
            self.best_distance = cur_dist
            self.best_solution = solution
        self.distance_list.append(cur_dist)
        return solution, cur_dist

    def dist(self, node_0, node_1):
        # """
        # Euclidean distance between two nodes.
        # """
        return self.city_distance[node_0][node_1]


    def distance(self, solution):
        """
        Total distance of the current solution path.
        """
        cur_dist = 0
        for i in range(self.N):
            cur_dist += self.dist(solution[i % self.N], solution[(i + 1) % self.N])
        return cur_dist

    def p_accept(self, candidate_distance):
        """
        Probability of accepting if the candidate is worse than current.
        Depends on the current temperature and difference between candidate and current.
        """
        return math.exp(-abs(candidate_distance - self.cur_distance) / self.T)

    def accept(self, candidate):
        """
        Accept with probability 1 if candidate is better than current.
        Accept with probabilty p_accept(..) if candidate is worse.
        """
        candidate_distance = self.distance(candidate)
        if candidate_distance < self.cur_distance:
            self.cur_distance, self.cur_solution = candidate_distance, candidate
            if candidate_distance < self.best_distance:
                self.best_distance, self.best_solution = candidate_distance, candidate
        else:
            if random.random() < self.p_accept(candidate_distance):
                self.cur_distance, self.cur_solution = candidate_distance, candidate

    def anneal(self):
        """
        Execute simulated annealing algorithm.
        """
        # Initialize with the greedy solution.
        self.cur_solution, self.cur_distance = self.initial_solution()

        print("Starting Annealing...")
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            l = random.randint(2, self.N - 1)
            i = random.randint(0, self.N - l)
            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])
            self.accept(candidate)
            self.T *= self.alpha
            self.iteration += 1

            self.distance_list.append(self.cur_distance)

        print("Best Route Distance obtained: ", self.best_distance)
        improvement = 100 * (self.distance_list[0] - self.best_distance) / (self.distance_list[0])
        # print(f"Improvement over greedy heuristic: {improvement : .2f}%")
        i = 0
        while True:
            if self.cities[i % self.N] == 'اصفهان':
                break
            i += 1
        print(self.cities[i % self.N])
        i += 1
        while True:
            if self.cities[i % self.N] == 'اصفهان':
                break
            print(self.cities[i % self.N])
            i += 1
        print('')
        print("Annealing Finished!")

    def batch_anneal(self, times=10):
        """
        Execute simulated annealing algorithm `times` times, with random initial solutions.
        """
        for i in range(1, times + 1):
            print(f"Iteration {i}/{times} -------------------------------")
            self.T = self.T_save
            self.iteration = 1
            self.cur_solution, self.cur_distance = self.initial_solution()
            self.anneal()

    def visualize_routes(self):
        """
        Visualize the TSP route with matplotlib.
        """
        visualize_tsp.plotTSP([self.best_solution], self.coords)

    def plot_learning(self):
        """
        Plot the fitness through iterations.
        """
        plt.plot([i for i in range(len(self.distance_list))], self.distance_list)
        plt.ylabel("Distance")
        plt.xlabel("Iteration")
        plt.show()
