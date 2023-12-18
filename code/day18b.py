from helpers.datagetter import aocd_data_in
import tqdm
import numpy as np

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ground = []
at = [0, 0]
perimeter = 0


def shoelace(points):
    # Ripped from skspatial.measurement.area_signed, but with np.int64
    points = np.array(points, dtype=np.int64)
    n_points = points.shape[0]

    X = points[:, 0]
    Y = points[:, 1]

    indices = np.arange(n_points)
    indices_offset = indices - 1

    return 0.5 * np.sum(X[indices_offset] * Y[indices] - X[indices] * Y[indices_offset])


for line in tqdm.tqdm(din):
    color = line.split("(")[1]

    d = int(color[-2])
    n = int(color[1:-2], 16)
    perimeter += n

    if d == 3:
        at[0] -= n
    elif d == 0:
        at[1] += n
    elif d == 1:
        at[0] += n
    else:
        at[1] -= n
    ground.append(at.copy())

aocd_submit(int(abs(shoelace(ground)) + perimeter / 2 + 1))
