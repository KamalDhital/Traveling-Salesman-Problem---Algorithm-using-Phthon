# Library used on this project are:
      1.import random
      2.import math
      3.import csv


# Description of project program code:
 -The class TourProgam initialize the program with n cities, load_cities, calculate_distance, and find_shortest_tour.
 -Method load_cities reads the cities from csv file(csv file MUST be place at same location as phyton source code file) and selects n cities randomly by using the random.sample function, skipping header row, and then prints the randomly selected cities with their respective latitude and lognitude.
 -Method calculate_distances computes the distance between each pair of cities using the Euclidean distance formula in miles.
 -Method find_shortest_tour applies the TSP algorithm to find the shortest tour by iterating over all possible swaps of two cities in the tour, compute the length of the tour with the two cities swapped, and update the tour if the new tour is shorter.
 -Method  get_tour_length clacualtes the total distance travelled.
 -Method test_tour_program test the program with 5 cities selected randomly.



