from datagetter import Matrix

mat = Matrix([3, 3], default=".", wrap=False)
print(mat)
mat[1, 1] = 2
print(mat[1, 1])
