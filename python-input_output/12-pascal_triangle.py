#!/usr/bin/python3
'''MODULE'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                val = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(val)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    '''Print the triangle'''
    
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
