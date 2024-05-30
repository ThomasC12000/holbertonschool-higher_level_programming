#!/usr/bin/python3
'''MODULE'''


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for level in range(n):
        if level == 0:
            triangle.append([1])
        else:
            new_row = [1]
            last_row = triangle[level - 1]

            for i in range(1, len(last_row)):
                new_row.append(last_row[i - 1] + last_row[i])

            new_row.append(1)
            triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
