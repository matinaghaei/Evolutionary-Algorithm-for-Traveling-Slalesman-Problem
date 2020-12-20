import random
import math
import matplotlib.pyplot as plt


class Chromosome:
    coordinates = []

    @staticmethod
    def calculate_distance(coordinate1, coordinate2):
        distance_x = coordinate1[1] - coordinate2[1]
        distance_y = coordinate1[2] - coordinate2[2]
        return math.sqrt(distance_x * distance_x + distance_y * distance_y)

    @classmethod
    def set_coordinates(cls, coordinates):
        cls.coordinates = coordinates

    @classmethod
    def crossover(cls, chr1, chr2):
        parent = [chr1.path, chr2.path]
        new_path = [0] * len(cls.coordinates)
        visited = [0] * len(cls.coordinates)
        copied = 0
        turn = 0
        while copied < len(cls.coordinates):
            current = 0
            while visited[current] == 1:
                current += 1
            while visited[current] == 0:
                visited[current] = 1
                new_path[current] = parent[turn][current]
                copied += 1
                current = parent[turn].index(parent[1 - turn][current])
            turn = 1 - turn

        return cls(new_path)

    def __init__(self, path=None):
        if path is None:
            self.path = []
            self.visited = [0] * len(self.coordinates)
            current = random.randrange(0, len(self.coordinates))
            self.path.append(current)
            self.visited[current] = 1
            for i in range(0, len(self.coordinates) - 1):
                current = self.nearest_neighbour(current)
                self.path.append(current)
                self.visited[current] = 1
        else:
            self.path = path

    def nearest_neighbour(self, index):
        nearest = None
        distance = None
        for i in range(0, len(self.coordinates)):
            if self.visited[i] == 0:
                new_distance = self.calculate_distance(self.coordinates[index], self.coordinates[i])
                if nearest is None or new_distance < distance:
                    nearest = i
                    distance = new_distance
        return nearest

    def get_fitness(self):
        distance = 0
        for i in range(len(self.path)):
            current = self.path[i]
            next_one = self.path[(i + 1) % len(self.path)]
            distance += self.calculate_distance(self.coordinates[current], self.coordinates[next_one])
        return -distance

    def mutate(self, number_of_mutations):
        for counter in range(number_of_mutations):
            i, j = random.sample(range(0, len(self.path)), 2)
            l, r = min(i, j), max(i, j)
            temp = self.path[l:r+1]
            for k in range(l, r + 1):
                self.path[k] = temp[r - k]

    def draw_path(self):
        for i in range(len(self.path)):
            current = self.path[i]
            next_one = self.path[(i + 1) % len(self.path)]
            x = [self.coordinates[current][1], self.coordinates[next_one][1]]
            y = [self.coordinates[current][2], self.coordinates[next_one][2]]
            plt.plot(x, y)
        plt.show()
