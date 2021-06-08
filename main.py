import random
import numpy as np


#def show_matrix_as_image(matrix):
#    image.show(matrix)


def create_random_matrix(width, height):
    matrix = np.random.rand(width, height)
    for x in range(0, width):
        for y in range(0, height):
            matrix[x][y] = random.randint(0, 1)
    return matrix

if __name__ == '__main__':
    init_matrix = create_random_matrix(10, 10)

    print(init_matrix)
    #show_matrix_as_image(init_matrix)