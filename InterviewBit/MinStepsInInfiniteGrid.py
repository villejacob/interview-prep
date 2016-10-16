'''
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps
in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''


X = [0, 1, 1]
Y = [0, 1, 2]


def cover_points(X, Y):
    moves = 0
    for i, x in enumerate(X):
        if i == len(X) - 1:
            return moves
        xdiff = abs(X[i] - X[i + 1])
        ydiff = abs(Y[i] - Y[i + 1])
        moves += max(xdiff, ydiff)

print cover_points(X, Y)