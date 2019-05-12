import numpy as np
from scipy.spatial.distance import pdist, squareform, cdist

if __name__ == "__main__":
    x1 = np.array([[1, 1]])
    x2 = np.array([[4, 5]])
    # 通过cdist函数，计算两个点之间的距离
    distance = cdist(x1, x2, "euclidean")
    print(distance)  # [[ 5.]]
