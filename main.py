from population import Population
from chromosome import Chromosome

if __name__ == '__main__':

    file = open("tsp_data.txt", "r")
    coordinates = []
    while True:
        line = file.readline()
        if not line:
            break
        coordinates.append(list(map(float, line.split())))

    number_of_generations = 1000
    population_size = 500
    children_size = 1000
    tournament_size = 10
    mutation_rate = 0.01

    Chromosome.set_coordinates(coordinates)
    population = Population(population_size, children_size, tournament_size, mutation_rate)
    population.generate(number_of_generations)
    population.print_answer()
    population.show_statistics()
