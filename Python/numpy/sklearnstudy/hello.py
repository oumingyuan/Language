from sklearn import datasets

import matplotlib.pyplot as plt

iris = datasets.load_iris()

# 获取花卉两列数据集
DD = iris.data
X = [x[0] for x in DD]
print(X)
Y = [x[1] for x in DD]
print(Y)

# plt.scatter(X, Y, c=iris.target, marker='x')
plt.scatter(X[:50], Y[:50], color='red', marker='o', label='setosa')  # 前50个样本
plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor')  # 中间50个
plt.scatter(X[100:], Y[100:], color='green', marker='+', label='Virginica')  # 后50个样本
plt.legend(loc=2)  # loc=1，2，3，4分别表示label在右上角，左上角，左下角，右下角
plt.show()
