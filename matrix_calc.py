# numpyをnpと言うエイリアスをつけてinport
import numpy as np

partition = "====="
# 1次元配列について
print("{0}1次元配列{1}".format(partition, partition))

# まずは１次元配列を普通に作ってみる
print("１次元配列を生成する")
array_1D = np.asanyarray([1, 2, 3])
print("生成した1次元配列 : {0}".format(array_1D))
print("生成した1次元配列の1番目の要素: {0}".format(array_1D[0]))

# 2つの1次元配列の四則演算を行う
a = np.asanyarray([5, 10, 15])
b = np.asanyarray([1, 2, 3])
print("作成した2つの配列: a => {0}, b => {1}".format(a, b))
print("a + b = {0}".format(a + b))
print("a - b = {0}".format(a - b))
print("a * b = {0}".format(a * b))
print("a / b = {0}".format(a / b))
print("a % b = {0}".format(a % b))

# 2次元配列について
print("{0}2次元配列{1}".format(partition, partition))

# 2次元配列を生成
print("2次元配列を生成する")
array_2D = np.asanyarray([[1, 2], [10, 100]])
print("生成した2次元配列 : \n{0}".format(array_2D))
print("生成した2次元配列の1番目の要素: {0}".format(array_2D[0][1]))

# 2つの2次元配列の四則演算を行う
c = np.asanyarray([[5, 10], [7, 14]])
d = np.asanyarray([[1, 2], [5, 6]])
print("作成した2つの配列: a => {0}, b => {1}".format(a, b))
print("a + b = \n{0}".format(c + d))
print("a - b = \n{0}".format(c - d))
print("aのスカラー倍 = \n{0}".format(3 * c))

# 2つの2次元配列の内積
x = np.dot(c, d)
print("行列aと行列bの内積 = \n{0}".format(x))
