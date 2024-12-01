import numpy as np
import random
import math
import matplotlib.pyplot as plt

def total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += np.linalg.norm(np.array(cities[route[i]]) - np.array(cities[route[i+1]]))
    distance += np.linalg.norm(np.array(cities[route[-1]]) - np.array(cities[route[0]]))
    return distance

def swap_two_cities(route):
    new_route = route.copy()
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def simulated_annealing(cities, initial_temp, cooling_rate, max_iter):
    route = list(range(len(cities)))
    random.shuffle(route)
    
    current_distance = total_distance(route, cities)
    best_route = route
    best_distance = current_distance
    temperature = initial_temp
    
    for iteration in range(max_iter):
        new_route = swap_two_cities(route)
        new_distance = total_distance(new_route, cities)
        
        delta_distance = new_distance - current_distance
        
        if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
            route = new_route
            current_distance = new_distance
        
        if current_distance < best_distance:
            best_route = route
            best_distance = current_distance
        
        temperature *= cooling_rate
    
    return best_route, best_distance

def plot_route(cities, best_route):
    best_coords = [cities[i] for i in best_route] + [cities[best_route[0]]]
    best_coords = np.array(best_coords)
    plt.plot(best_coords[:, 0], best_coords[:, 1], 'b-', marker='o')
    plt.scatter(best_coords[:, 0], best_coords[:, 1], color='red')
    plt.title('TSP Solution with Simulated Annealing')
    plt.show()

num_cities = 20
cities = np.random.rand(num_cities, 2) * 100

initial_temp = 1000
cooling_rate = 0.995
max_iter = 10000

best_route, best_distance = simulated_annealing(cities, initial_temp, cooling_rate, max_iter)

print("Best route:", best_route)
print("Best total distance:", best_distance)
print(cities)
plot_route(cities, best_route)