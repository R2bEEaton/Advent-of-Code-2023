from helpers.datagetter import aocd_data_in
import numpy as np

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

matrixes = []
matrix = []
for line in din:
    if len(line) == 0:
        matrixes.append(matrix)
        matrix = []
        continue
    mline = []
    for c in line:
        mline.append(0 if c == "." else 1)
    matrix.append(mline)
matrixes.append(matrix)

for matrix in matrixes:
    matrix = np.array(matrix)

    i = 0
    j = 1
    old_i = i
    old_j = j
    found = False
    vertical_reflections = [[0]]
    while i < matrix.shape[1] and j < matrix.shape[1]:
        if np.array_equal(matrix[:, i], matrix[:, j]):
            if not found:
                old_i = i
                old_j = j
            found = True
            i -= 1
            j += 1
        else:
            if found:
                if i == -1 or j == matrix.shape[1]:
                    vertical_reflections.append([old_i - i, old_i])
                i = old_i
                j = old_j
            found = False
            i += 1
            j += 1
    if found:
        if i == -1 or j == matrix.shape[1]:
            vertical_reflections.append([old_i - i, old_i])
    vertical_reflections.sort(key=lambda x: -x[0])

    i = 0
    j = 1
    old_i = i
    old_j = j
    found = False
    horizontal_reflections = [[0]]
    while i < matrix.shape[0] and j < matrix.shape[0]:
        if np.array_equal(matrix[i, :], matrix[j, :]):
            if not found:
                old_i = i
                old_j = j
            found = True
            i -= 1
            j += 1
        else:
            if found:
                if i == -1 or j == matrix.shape[0]:
                    horizontal_reflections.append([old_i - i, old_i])
                i = old_i
                j = old_j
            found = False
            i += 1
            j += 1
    if found:
        if i == -1 or j == matrix.shape[0]:
            horizontal_reflections.append([old_i - i, old_i])
    horizontal_reflections.sort(key=lambda x: -x[0])

    if vertical_reflections[0][0] > horizontal_reflections[0][0]:
        ans += vertical_reflections[0][1] + 1
    else:
        ans += (horizontal_reflections[0][1] + 1) * 100

aocd_submit(ans)
