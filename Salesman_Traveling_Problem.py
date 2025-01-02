                       # CS 5007 HW5
                   #Name: KAMAL DHITAL
                       # Email:kkdhital@wpi.edu


import csv
import random
import math

class TourProgram:
    def __init__(self, n):
        self.n = n
        self.cities = self.load_cities()
        self.distances = self.calculate_distances()
        self.tour = self.find_shortest_tour()

    def load_cities(self):
        with open('uscities.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            cities = []
            for row in reader:
                cities.append((row[0], float(row[6]), float(row[7])))
            select_cities = random.sample(cities,self.n)
            print('Selected Cities :',select_cities,'\n------------------------')
        
        return select_cities

    def calculate_distances(self):
        distances = {}
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    distances[(i, j)] = 0
                elif (j, i) in distances:
                    distances[(i, j)] = distances[(j, i)]
                else:
                    xi, yi = self.cities[i][1], self.cities[i][2]
                    xj, yj = self.cities[j][1], self.cities[j][2]
                    distance = math.sqrt((xi - xj)**2 + (yi - yj)**2)
                    distances[(i, j)] = distance
        return distances

    def find_shortest_tour(self):
        # Initialize the tour to visit cities in the order they appear in the list
        tour = list(range(self.n))
        # Iterate over all possible swaps of two cities in the tour
        for i in range(self.n):
            for j in range(i+1, self.n):
                # Compute the length of the tour with the two cities swapped
                new_tour = tour.copy()
                new_tour[i:j+1] = reversed(new_tour[i:j+1])
                new_length = sum(self.distances[(new_tour[k], new_tour[k+1])] for k in range(self.n-1))
                new_length += self.distances[(new_tour[-1], new_tour[0])]
                # Update the tour if the new tour is shorter
                if new_length < sum(self.distances[(tour[k], tour[k+1])] for k in range(self.n-1)) + self.distances[(tour[-1], tour[0])]:
                    tour = new_tour
        return tour

    def get_tour_length(self):
        return sum(self.distances[(self.tour[k], self.tour[k+1])] for k in range(self.n-1)) + self.distances[(self.tour[-1], self.tour[0])]

def test_tour_program():
    # Test with n=5, five cities
    n = 5
    program = TourProgram(n)
    print(f'Tour: {program.tour}')
    print(f'Tour length: {program.get_tour_length()}')

test_tour_program()
