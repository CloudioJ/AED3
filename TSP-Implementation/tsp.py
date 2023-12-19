import sys
from itertools import permutations
import re
import time
from scipy.sparse.csgraph import minimum_spanning_tree
import math

def brute_force(graph, src, v_num):

    vertex = []
    min_path = sys.maxsize

    for i in range(v_num):
        if i != src:
            vertex.append(i)

    perms = permutations(vertex)

    for perm in perms:

        k = src
        
        weight = 0

        for n in perm:
            weight += graph[k][n]
            k = n
        
        weight += graph[k][src]

        min_path = min(min_path, weight)
    return min_path

def approximation(matrix, src):
    MST = minimum_spanning_tree(matrix)
    MST = MST.toarray().astype(int)

    nodes = list(range(len(MST)))

    path = [src]
    current_node = src
    previous_node = -1

    while set(path) != set(nodes):
        for connected_node in nodes:
            if not MST[current_node, connected_node] and not MST[connected_node, current_node]:
                continue

            elif connected_node in path:
                continue

            else:
                path.append(connected_node)
                current_node = connected_node
                previous_node = -1
                break
        else:
            current_node = path[previous_node]
            previous_node -= 1

    path.append(src)

    tsp_cost = calculate_path_cost(matrix, path)

    return tsp_cost, path

def calculate_path_cost(matrix, path):
    tsp_cost = 0
    nodes = range(len(matrix))

    for index in nodes:
        line = path[index]
        column = path[index + 1]

        edge_weight = matrix[line][column]

        tsp_cost += edge_weight

    return tsp_cost

def number_from_file(file_name):
    return re.search(r'\d+(?!\_)', file_name).group(0)

if __name__ == "__main__":
    start_time = time.time()

    matrix_file = sys.argv[1]
    src = int(sys.argv[2])
    method = sys.argv[3]

    answer = int(number_from_file(matrix_file))

    with open(matrix_file, "r") as file:
        matrix = []
        for line in file:
            numbers = [int(x) for x in line.split()]
            matrix.append(numbers)
    
    file.close()
    vertices = len(matrix)

    match method:
        case 'b':
            algo = 'bruteforce'
            min_value = brute_force(matrix, src, vertices)

        case 'a':
            algo = 'approx'
            min_value, path = approximation(matrix, src)
            print(path)

    result_file = open(f'results_{answer}_{algo}.txt', 'w')

    print(f'Minimal value: {min_value}')
    print("Execution time: %s seconds" % (time.time() - start_time))
    
    result_file.write(f'Mininum weight: {min_value} - Execution time: {(time.time() - start_time)}\n{math.trunc((min_value/answer) * 100)}% worse than optimal solution on average.')
    result_file.close()