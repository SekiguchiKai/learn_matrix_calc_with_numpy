# numpyをnpと言うエイリアスをつけてinport
import numpy as np
# 1次元配列
arr = np.array([0, 1, 2, 3, 4])
print("1次元配列arrの値は{0}".format(arr))
max_value = arr.max(0)
print("Maxの値は{0}".format(max_value))
# 書きは当然エラー 1次元配列は、1次元(indexでいうところの0)しかないので
# max_value = arr.max(1)
# print("Maxの値は{0}".format(max_value))
max_index = arr.argmax(0)
print("Maxのindexは{0}".format(max_index))

# 2次元配列を生成
arr2 = np.array([[0, 5, 2], [4, 1, 3]])
print("2次元配列arr2の値は{0}".format(arr2))
max_value = arr2.max(0)
print("axis0(列方向)のMaxの値は{0}".format(max_value))
max_index = arr2.argmax(0)
print("axis0(列方向)Maxのindexは{0}".format(max_index))
max_value = arr2.max(1)
print("axis1(行方向)Maxの値は{0}".format(max_value))
max_index = arr2.argmax(0)
print("axis1(行方向)Maxのindexは{0}".format(max_index))
# 書きは当然エラー 1次元配列は、1次元(indexでいうところの0)しかないので
# max_value = arr.max(2)
# print("Maxの値は{0}".format(max_value))


