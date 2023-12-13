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

    vertical_reflections = [[0]]
    for k in range(matrix.shape[1] - 1):
        i = k
        j = k + 1
        found = False
        xored = False
        while i >= 0 and j < matrix.shape[1]:
            xor = np.bitwise_xor(matrix[:, i], matrix[:, j])
            if np.array_equal(matrix[:, i], matrix[:, j]):
                found = True
                i -= 1
                j += 1
            elif np.sum(xor) == 1 and not xored:
                xored = True
                found = True
                i -= 1
                j += 1
            else:
                break
        if found and xored and (i == -1 or j == matrix.shape[1]):
            vertical_reflections.append([k - i, k])
    vertical_reflections.sort(key=lambda x: -x[0])

    horizontal_reflections = [[0]]
    for k in range(matrix.shape[0] - 1):
        i = k
        j = k + 1
        found = False
        xored = False
        while i >= 0 and j < matrix.shape[0]:
            xor = np.bitwise_xor(matrix[i, :], matrix[j, :])
            if np.array_equal(matrix[i, :], matrix[j, :]):
                found = True
                i -= 1
                j += 1
            elif np.sum(xor) == 1 and not xored:
                xored = True
                found = True
                i -= 1
                j += 1
            else:
                break
        if found and xored and (i == -1 or j == matrix.shape[0]):
            horizontal_reflections.append([k - i, k])
            break
    horizontal_reflections.sort(key=lambda x: -x[0])

    if vertical_reflections[0][0] > horizontal_reflections[0][0]:
        ans += vertical_reflections[0][1] + 1
    else:
        ans += (horizontal_reflections[0][1] + 1) * 100

aocd_submit(ans)
