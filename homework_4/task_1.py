"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matrix, target):

    x = len(matrix)
    y = len(matrix[0])

    if x == 0:
        return False
    if y == 0:
        return False

    i = 0
    j = y - 1

    while i < x and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] < target:
            i = i + 1
        else:
            j = j - 1
    return [-1, -1]



# x = len(matrix[0])  # to find the x coordinate
# y = len(matrix[-1])  # to find the y coordinate
#
# if x == 0:
#     return False
# if y == 0:
#     return False
#
# while x in matrix and y in matrix:
#     if target in matrix:
#         position = matrix.index(target)
#         return position
# return [-1, -1]


matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

print(search_in_matrix(matrix, target))
