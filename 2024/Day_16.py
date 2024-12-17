import heapq
from collections import defaultdict
import math

# Leer el archivo de entrada
with open('16.txt') as file:
    maze = file.read().splitlines()

# Direcciones posibles: arriba, izquierda, derecha, abajo
movement_directions = {(-1, 0), (0, -1), (0, 1), (1, 0)}

# Identificar paredes, posición inicial y posición objetivo
wall_positions = {(row, col) for row, line in enumerate(maze) for col, char in enumerate(line) if char == '#'}
start_position = next((row, col) for row, line in enumerate(maze) for col, char in enumerate(line) if char == 'S') + (0, 1)
goal_position = next((row, col) for row, line in enumerate(maze) for col, char in enumerate(line) if char == 'E')
goal_positions = [(goal_position[0], goal_position[1], move_x, move_y) for move_x, move_y in movement_directions]

# Algoritmo para encontrar el tiempo mínimo hacia el objetivo
def shortest_path(start, goals, neighbor_distance_func):
    visited_nodes, priority_queue = {}, [(0, start)]
    min_distances = defaultdict(lambda: math.inf, {start: 0})

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)
        if current_node in visited_nodes:
            continue
        visited_nodes[current_node] = True

        if current_node in goals:
            return current_time

        for (next_node, distance) in neighbor_distance_func(current_node):
            new_time = current_time + distance
            if next_node not in visited_nodes and new_time < min_distances[next_node]:
                min_distances[next_node] = new_time
                heapq.heappush(priority_queue, (new_time, next_node))

# Algoritmo desde múltiples posiciones iniciales
def multi_source_path(start_positions, neighbor_distance_func):
    visited_nodes = {}
    priority_queue = [(0, position) for position in start_positions]
    min_distances = defaultdict(lambda: math.inf, {position: 0 for position in start_positions})
    output_distances = {}

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)
        if current_node in visited_nodes:
            continue
        visited_nodes[current_node] = True
        output_distances[current_node] = current_time

        for (next_node, distance) in neighbor_distance_func(current_node):
            new_time = current_time + distance
            if next_node not in visited_nodes and new_time < min_distances[next_node]:
                min_distances[next_node] = new_time
                heapq.heappush(priority_queue, (new_time, next_node))
    return output_distances

# Función para determinar vecinos y sus costos de viaje
def neighbor_distance_function(current_position):
    row, col, move_x, move_y = current_position
    neighbors = []

    # Movimiento hacia adelante
    if (row + move_x, col + move_y) not in wall_positions:
        neighbors.append(((row + move_x, col + move_y, move_x, move_y), 1))

    # Movimientos de giro con alto costo
    neighbors.extend([((row, col, new_move_x, new_move_y), 1000) 
                      for new_move_x, new_move_y in movement_directions 
                      if (new_move_x, new_move_y) != (move_x, move_y)])
    return neighbors

# Calcular el tiempo mínimo para llegar al objetivo
minimum_time = shortest_path(start_position, goal_positions, neighbor_distance_function)
print(minimum_time)

# Calcular distancias desde el inicio y desde los objetivos
distances_from_start = multi_source_path([start_position], neighbor_distance_function)
distances_from_goal = multi_source_path(goal_positions, neighbor_distance_function)

# Encontrar posiciones que cumplen la condición de tiempo mínimo
reachable_coordinates = {(row, col) 
                         for (row, col, move_x, move_y) in distances_from_start 
                         if distances_from_start[(row, col, move_x, move_y)] + 
                            distances_from_goal[(row, col, -move_x, -move_y)] == minimum_time}

print(len(reachable_coordinates))