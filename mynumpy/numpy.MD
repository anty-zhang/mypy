#############################################################
# numpy 主要功能
#############################################################

1.数据清理与整理、子集构成、过滤、转换等矢量化的数组运算
2.常用数组运算：排序，唯一化，集合运算
3.高效的描述统计和数据聚合/摘要运算
4.异构数据的连接/合并运算的数据对齐和关系型数据运算
5.将条件逻辑表达为数组表达式
6.数据的分组运算（聚合/转换/函数应用）


#############################################################
# ndarray
#############################################################
import numpy as np
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
type(data1)
type(arr1)
arr1
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2
arr2.shape
arr1.shape
arr2.nship
help(arr2)
arr1.dtype
arr2.dtype
hist
arr2.ndim
hist
np.zeros(10,1)
np.zeros(10)
np.zeros((10,5))
np.ones((10,5))
hist
np.empty((2,3))
np.empty((2,3,1))
np.empty((2,3,3))
np.arrange(10)
np.arange(10)
type(np.arange(10))
np.eye(10)
np.identity(10)
np.empty_like(10)
np.empty_like((10,5))
hist
arr = np.array([1,2,3,4,5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype
number_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
number_strings
number_strings.astype(float)
number_strings.astype(float64)
number_strings.astype(npfloat64)
number_strings.astype(np.float64)
hist


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
import numpy as np
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d
arr2d[:2]
arr2d[2:]
arr2d[1]
arr2d[1][2]
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d
old_values = arr3d[0].copy()
old_values
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 布尔型索引
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob' , 'Will', 'Joe', 'Joe'])
names
data = np.randn(7,4)
data = np.random.randn(7,4)
data
names == 'Bob'
data(names == 'Bob')
data[names == 'Bob']
data[names == 'Bob', 2:]
data[names == 'Bob', 3]
data[names != 'Bob']
data[-(names == 'Bob')]
mask = (names == 'Bob') | (names == 'Will')
mast
mask
data[mask]
data[data < 0] = 0
data
data[names == 'Joe'] = 7
data
hist

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 花式索引
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
arr = np.empty((8,4))

arr = np.empty((8,4))
arr
arr.shape
for i in range(8):
    arr[i] = i
arr
arr[[4, 3, 0, 6]]
arr[[-1]]
arr[[-7]]
arr[[-8]]
arr1 = np.arange(32).reshape((8,4))        # reshape
arr1
arr1[[1, 5, 7, 2], [0, 3, 1, 2]]           # 选择特定元素
arr1[[1, 5, 7, 2]]
arr1[[1, 5, 7, 2]][:, [0, 3, 1, 2]]        # 选择正方形索引器
arr1[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]   # 选择正方形索引器
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 数组转置和轴对换
& 高维数组的转置？？？
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

arr = np.arange(15).reshape(3,5)
arr
arr.T
no.dot(arr,arr.T)
np.dot(arr,arr.T)
arr = np.range(16).reshape((2, 2, 4))
arr
arr = np.arange(16).reshape((2, 2, 4))
arr
arr.T
arr.transpose((1, 0, 2))
arr
arr.swapaxes(1,2)
arr.swapaxes(2,1)
arr.swapaxes(0,1)
arr
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 通用函数：元素级别的函数
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

1. 一元func
abs，fabs
sqrt
square
exp
log，log10,log2
sign
ceil
floor
rint
modf
isnan
isfinite，isinf
cos，cosh，sin， sinh
tan， tanh
arccos，arccosh，arcsin


2. 二元func
add
subtract
multiply
divide，floor_divid  
power
maximum，fmax
minimum，fmin
mod
copysin
greater， greater_equal
less
logical_and, loggical_or,logical_xor


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 利用数组进行数据处理
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
points = np.arange(-5, 5, 0.01)
points
help(np.meshgrid)
xs, ys = np.meshgrid(points, points)   # 数据网格
xs
ys
xs.shape
ys.shape
import matplotlib.pyplot as plt
z = np.sqrt(xs**2, ys**2)
z
z = np.sqrt(xs**2 + ys**2)
z
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid values")
plt.imshow(z)



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 将条件逻辑表达为数组表达式
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
xarr
yarr
cond = np.array([True, False, True, True, False])
cond
result = np.where(cond, xarr, yarr)   # 条件转为数组表达式
result
arr = np.random.randn(4,4)
arr
np.where(arr > 0, 2, -2)
np.where(arr > 0, 2, arr)
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 数学和统计方法
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
arr = np.random.randn(5,4)
arr
arr.mean()                                         #
np.mean(arr)					   #
arr.sum()
arr.mean(asis=1)
arr.mean(axis=1)
arr.sum(0)
arr.sum(1)
arr = np.array([[0,1,2], [3,4,5], [6,7,8]])
arr
arr.cumsum(0)                                     # 所有元素累计和
arr.cumprod(1)                                    # 所有元素累计积
hist

std，var
min，max
argmin，argmax				# 最大最小元素索引






&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 用户布尔型数组的方法
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import numpy as np
arr = np.random.randn(100)
arr
(arr > 0).sum()                            # True = 1 ，False = 0
(arr < 0).sum()
bools = np.array([False, False, True, False])
bools.any()                                # 
bools.all()                                #
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 排序
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import numpy as np
arr = np.random.randn(8)
arr
arr.sort(0)
arr
arr.sort(reverse=True)        # error
help(arr.sort)
arr = np.random.randn(5,4)
arr
np.sort(arr(1)
)
np.sort(arr(1))
np.sort(arr)


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 唯一化及其他集合运算
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
In [1]: import numpy as np

In [2]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

In [3]: np.uni
np.unicode   np.unicode0  np.unicode_  np.union1d   np.unique    

In [3]: np.unique(names)                # 唯一化
Out[3]: 
array(['Bob', 'Joe', 'Will'], 
      dtype='|S4')

In [4]: ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

In [5]: np.unique(ints)
Out[5]: array([1, 2, 3, 4])

In [6]: ints1 = np.array([1, 2, 3, 4, 5])

In [7]: ints2 = np.array([4, 5, 6, 7, 8])

In [8]: ints1
Out[8]: array([1, 2, 3, 4, 5])

In [9]: ints2
Out[9]: array([4, 5, 6, 7, 8])

In [10]: np.inter
np.interp       np.intersect1d  

In [10]: np.intersect1d(ints1, ints2)       # 交集
Out[10]: array([4, 5])

In [11]: np.uni
np.unicode   np.unicode0  np.unicode_  np.union1d   np.unique    

In [11]: np.union1d(ints1, ints2)           # 并集
Out[11]: array([1, 2, 3, 4, 5, 6, 7, 8])

In [12]: np.setdiff1d(ints1, ints2)         # 差集
Out[12]: array([1, 2, 3])

In [13]: np.setxor1d(ints1, ints2)          # 交差集
Out[13]: array([1, 2, 3, 6, 7, 8])

In [14]: values = np.array([1, 2, 0, 0, 4, 2, 6, 7])

In [15]: np.in1d(values, [0, 2, 6])         # ”x元素是否包含于y“的布尔型数组
Out[15]: array([False,  True,  True,  True, False,  True,  True, False], 
dtype=bool)


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 将数组以二进制的形式保存到磁盘
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
In [1]: import numpy as np

In [2]: arr = np.array([0, 1, 2, 3, 4, 5])

In [3]: np.save('some_array', arr)          # 非压缩的二进制

In [4]: np.load
np.load     np.loads    np.loadtxt 

In [5]: np.load('some_array.npy')
Out[5]: array([0, 1, 2, 3, 4, 5])

In [6]: np.savez('array.npz', a=arr, b=arr)   # 压缩的二进制

In [7]: arch = np.load('array.npz')

In [8]: arch
Out[8]: <numpy.lib.npyio.NpzFile at 0x9aac62c>

In [9]: arch['a']
Out[9]: array([0, 1, 2, 3, 4, 5])

In [10]: arch['b']
Out[10]: array([0, 1, 2, 3, 4, 5])


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 存取文本文件
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
np.loadtxt('array_ex.txt', delimiter=',')
np.savetxt()
np.genfromtxt()


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 线性代数
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 'diag'             	# 以一维数组的方式返回方阵的对角线元素
 'bench',
 'cholesky',
 'cond',
 'det',			# 计算矩阵行列式
 'division',
 'eig',
 'eigh',
 'eigvals',
 'eigvalsh',
 'info',
 'inv',			# 求逆
 'lapack_lite',
 'linalg',
 'lstsq',		# 计算Ax=b的最小二乘解
 'matrix_power',
 'matrix_rank',
 'norm',
 'pinv',		# 计算矩阵的Moore-Penrose伪逆
 'print_function',
 'qr',          	# 计算QR分解
 'slogdet',
 'solve',		# 解线性方程组Ax=b
 'svd',         	# 奇异值分解
 'trace',		# 计算对角线元素的和
 'tensorinv',
 'tensorsolve',
 'test']


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 随机数生成
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
In [13]: dir(np.random)
Out[13]: 
[
 'absolute_import',
 'bench',
 'beta',
 'binomial',			#
 'bytes',
 'chisquare',
 'choice',
 'dirichlet',
 'division',
 'exponential',
 'f',
 'gamma',
 'geometric',
 'get_state',
 'gumbel',
 'hypergeometric',
 'info',
 'laplace',
 'logistic',
 'lognormal',
 'logseries',
 'mtrand',
 'multinomial',
 'multivariate_normal',
 'negative_binomial',
 'noncentral_chisquare',
 'noncentral_f',
 'normal',
 'np',
 'operator',
 'pareto',
 'permutation',			
 'poisson',
 'power',
 'print_function',
 'rand',			#
 'randint',
 'randn',			#
 'random',
 'random_integers',
 'random_sample',
 'ranf',
 'rayleigh',
 'sample',
 'seed',              		#
 'set_state',
 'shuffle',
 'standard_cauchy',
 'standard_exponential',
 'standard_gamma',
 'standard_normal',
 'standard_t',
 'test',
 'triangular',
 'uniform',
 'vonmises',
 'wald',
 'warnings',
 'weibull',
 'zipf']


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 简单随机漫步实例
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import numpy as np
help(np.random.randint)
nsteps = 1000
draws = np.random.randint(0, 2, size = nsteps)
draws
steps = np.where(draws > 0, 1, -1)
steps
walk = steps.cumsum()
walk
walk.min()
walk.max()
(np.abs(walk) >= 10).argmax()
help(np.random.randint)
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&




&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



















