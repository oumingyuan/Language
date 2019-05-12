import numpy as np

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt1 = np.dtype('i4')
print(dt1)

# 字节顺序标注
dt2 = np.dtype('<i4')
print(dt2)

dt3 = np.dtype([('age', np.int8)])
print(dt3)
