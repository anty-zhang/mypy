#############################################################
# pandas 数据结构介绍
#############################################################

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& Series
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
1.Series 由一组索引和一组Numpy的数据组成
2.索引：obj.index
  1）默认索引
  2）指定索引
  3）通过字典创建
  4）通过赋值的方式就地修改
3.通过索引取一个值或者几个值
4.numpy运算都会保留索引和数值之间的连接
5.pd.isnull pd.notnull
  obj.isnull obj.notnull
  obj.name = ''
  obj.index.name = ''
  

from pandas as pd
import pandas as pd
from pandas import Series, DataFrame
obj = Series([4, 7, -5, 3])
obj
obj.values
obj.index
obj = Series([4, 7, -5, 3], index = ['a', 'b', 'c', 'd'])
obj
help(Series)
obj['a']
obj[['a','c']]
obj
obj > 0
obj[obj > 0]
obj * 2
np.exp(obj)
import numpy as np
np.exp(obj)
'b' in obj
'e' in obj
obj.index
obj.values
sdata = {"Ohio":35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
sdata
obj3 = Series(sdata)
obj3
obj3.index
obj3.values
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4
pd.isnull(obj4)
pd.notnull(obj4)
obj4.notnull()
obj4.isnull()
obj3
obj3 + ojb4
obj3 + obj4
obj4.name
obj4.index
obj4.index.name
obj4
obj.index
obj
obj4.index.name
obj4.name = 'population'
obj4
obj4.index.name = 'state'
obj4
obj
obj.index = ['Bob', 'Steven', 'Jeff', 'Ryan']
obj
hist


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& DataFrame
& 表格型数据结构
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
1.构建DataFrame
  传入一个等长列表或者Numpy数组组成的字典

In [1]: %log
%logoff    %logon     %logstart  %logstate  %logstop   

In [1]: %logst
%logstart  %logstate  %logstop   

In [1]: %logsta
%logstart  %logstate  

In [1]: %logstart
Activating auto-logging. Current session state plus future input saved.
Filename       : ipython_log.py
Mode           : rotate
Output logging : False
Raw input log  : False
Timestamping   : False
State          : active

In [2]: from pandas import Series, DataFrame

In [3]: import pandas as pd

In [4]: data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year':[2000, 2001, 2002, 2001, 2002], 'pop':[1.5, 1.7, 3.6, 4.8, 5.0]}

In [5]: frame = DataFrame(data)   # 字典列表类型

In [6]: frame
Out[6]: 
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  4.8  Nevada  2001
4  5.0  Nevada  2002

In [7]: DataFrame(data, columns=['year', 'state', 'pop'])      # 指定columns
Out[7]: 
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  4.8
4  2002  Nevada  5.0

In [8]: frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], 
index=['one', 'two', 'three', 'four', 'five'])   # 默认值NaN

In [9]: fram
frame   frame2  

In [9]: frame2
Out[9]: 
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  4.8  NaN
five   2002  Nevada  5.0  NaN

In [10]: frame
frame   frame2  


In [11]: frame2.columns           # 列
Out[11]: Index([u'year', u'state', u'pop', u'debt'], dtype='object')

In [12]: frame2.in
frame2.index        frame2.info         frame2.insert       frame2.interpolate  

In [12]: frame2.index             # 行
Out[12]: Index([u'one', u'two', u'three', u'four', u'five'], dtype='object')

In [13]: fram
frame   frame2  

In [13]: frame2['state']         # 取列
Out[13]: 
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object

In [14]: frame2.state		# 取列
Out[14]: 
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object

In [15]: 

In [15]: frame
frame   frame2  

In [15]: frame2.ix('one')
Out[15]: <pandas.core.indexing._IXIndexer at 0xa9b142c>

In [16]: frame2.ix['one']            # 取行
Out[16]: 
year     2000
state    Ohio
pop       1.5
debt      NaN
Name: one, dtype: object

In [17]: frame2
Out[17]: 
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  4.8  NaN
five   2002  Nevada  5.0  NaN

In [18]: fram
frame   frame2  

In [18]: frame2.de
frame2.debt      frame2.describe  

In [18]: frame2.debt = 18.9               # 赋值

In [19]: frame2
Out[19]: 
       year   state  pop  debt
one    2000    Ohio  1.5  18.9
two    2001    Ohio  1.7  18.9
three  2002    Ohio  3.6  18.9
four   2001  Nevada  4.8  18.9
five   2002  Nevada  5.0  18.9

In [20]: np.arange(5.0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-5f7e7ae8cba6> in <module>()
----> 1 np.arange(5.0)

NameError: name 'np' is not defined

In [21]: import numpy as np

In [22]: np.arange(5.0)    
Out[22]: array([ 0.,  1.,  2.,  3.,  4.])

In [23]: frame2.de
frame2.debt      frame2.describe  

In [23]: frame2.debt = np.arange(5.0)        # 赋值

In [24]: frame2
Out[24]: 
       year   state  pop  debt
one    2000    Ohio  1.5     0
two    2001    Ohio  1.7     1
three  2002    Ohio  3.6     2
four   2001  Nevada  4.8     3
five   2002  Nevada  5.0     4

In [25]: val = Series([-1.2, -3.5, 4.0], index = ['two', 'four', 'five'])

In [26]: frame2.de
frame2.debt      frame2.describe  

In [26]: frame2.debt = val                 # 赋值

In [27]: frame2
Out[27]: 
       year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  4.8  -3.5
five   2002  Nevada  5.0   4.0


In [1]: from pandas import Series,DataFrame

In [2]: import pandas as pd

In [3]: data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year':[2000, 2001, 2002, 2001, 2002], 'pop':[1.5, 1.7, 3.6, 4.8, 5.0]}

In [4]: frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], 
index=['one', 'two', 'three', 'four', 'five'])

In [5]: frame2
Out[5]: 
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  4.8  NaN
five   2002  Nevada  5.0  NaN

In [6]: frame2['eastern'] = frame2.state == 'Ohio'    # 赋Bluean 值

In [7]: frame2
Out[7]: 
       year   state  pop debt eastern
one    2000    Ohio  1.5  NaN    True
two    2001    Ohio  1.7  NaN    True
three  2002    Ohio  3.6  NaN    True
four   2001  Nevada  4.8  NaN   False
five   2002  Nevada  5.0  NaN   False


In [8]: pop = {"Nevada": {2001: 2.4, 2002: 2.9}, "Ohio": {2000: 1.5, 2001: 1.7, 
2002: 3.7}}

In [9]: pop
Out[9]: {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 
3.7}}

In [10]: frame3 = DataFrame(pop)      	# 嵌套字典（外层键作为列，内层键作为行，内层字典的键会自动合并）

In [11]: frame3
Out[11]: 
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.7

In [12]: frame3.T                  		# 转置
Out[12]: 
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.7


In [13]: DataFrame(pop, index=[2001,2002,2003])   # 显示指定索引，则内存字典的键不会合并
Out[13]: 
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.7
2003     NaN   NaN


In [14]: frame3
Out[14]: 
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.7

In [16]: pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}

In [17]: pdata
Out[17]: 
{'Nevada': 2000    NaN
 2001    2.4
 Name: Nevada, dtype: float64, 'Ohio': 2000    1.5
 2001    1.7
 Name: Ohio, dtype: float64}

In [18]: DataFrame(pdata)				# 由Series组成的的字典创建
Out[18]: 
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7


In [21]: frame3.index.name = 'year' 			# 设置行索引

In [22]: frame3.index.name
Out[22]: 'year'

In [23]: frame3
Out[23]: 
      Nevada  Ohio
year              
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.7

In [24]: frame3.columns.name = 'state'			# 设置列索引

In [25]: frame3
Out[25]: 
state  Nevada  Ohio
year               
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   3.7

In [26]: frame3.values					# 查看值
Out[26]: 
array([[ nan,  1.5],
       [ 2.4,  1.7],
       [ 2.9,  3.7]])

In [27]: frame3.columns					# 产看行/列值
Out[27]: Index([u'Nevada', u'Ohio'], dtype='object')



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 索引对象
& pandas索引对象负责管理轴标签和其他数据(比如轴名称)
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
1. 主要索引对象
In [42]: pd.I					# pandas主要index对象
pd.Index       pd.IndexSlice  pd.Int64Index
In [42]: pd.MultiIndex				# pandas主要index对象
In [42]: pd.DatetimeIndex			# pandas主要index对象
pd.DatetimeIndex
In [42]: pd.Period				# pandas主要index对象
pd.Period       pd.PeriodIndex


2. Index的属性和方法
append						# 连接另一个Index对象
diff
intersection
union
isin						# 一个指示各值是否包含在参数集合中的布尔数组
delete
drop
insert
is_monotonic
is_unique
unique

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 基本功能
& 
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
============ 1. 重新索引（reindex）===========================

In [1]: from pandas import Series, DataFrame

In [2]: import pandas as pd

In [3]: obj = Series([4.5, 7.2, -2.1, 9.0], index=['d', 'b', 'a', 'c'])

In [4]: obj
Out[4]: 
d    4.5
b    7.2
a   -2.1
c    9.0
dtype: float64

In [5]: obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])		# 重新索引

In [6]: obj2							# 重新索引后值不变
Out[6]: 
a   -2.1
b    7.2
c    9.0
d    4.5
e    NaN							# 默认值
dtype: float64


In [7]: obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)    # 引入默认值
Out[7]: 
a   -2.1
b    7.2
c    9.0
d    4.5
e    0.0
dtype: float64


In [9]: obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

In [10]: obj3
Out[10]: 
0      blue
2    purple
4    yellow
dtype: object

In [11]: obj3.reindex(range(6))
Out[11]: 
0      blue
1       NaN
2    purple
3       NaN
4    yellow
5       NaN
dtype: object

In [12]: obj3.reindex(range(6), method='ffill')		# 向前填充值
Out[12]: 
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object

In [13]: obj3.reindex(range(6), method='bfill')		# 向后填充值
Out[13]: 
0      blue
1    purple
2    purple
3    yellow
4    yellow
5       NaN
dtype: object



In [15]: frame = DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'], 
columns=['Ohio', 'Texas', 'California'])		# 矩阵创建DataFrame

In [16]: frame
Out[16]: 
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8

In [17]: frame2  = frame.reindex(['a', 'b', 'c', 'd'])	# 行索引

In [18]: frame2
Out[18]: 
   Ohio  Texas  California
a     0      1           2
b   NaN    NaN         NaN
c     3      4           5
d     6      7           8

In [19]: frame.reindex(columns=['Texas', 'Ohio', 'California'])	# 列索引
Out[19]: 
   Texas  Ohio  California
a      1     0           2
c      4     3           5
d      7     6           8

In [20]: frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', 
columns=['Texas', 'Ohio', 'California'])		# 行/列索引，默认值
Out[20]: 
   Texas  Ohio  California
a      1     0           2
b      1     0           2
c      4     3           5
d      7     6           8

In [21]: frame.reindex(index=['a', 'b', 'c', 'd'], columns=['Texas', 'Ohio', 
'California'])
Out[21]: 
   Texas  Ohio  California
a      1     0           2
b    NaN   NaN         NaN
c      4     3           5
d      7     6           8
						      # ix标签索引功能
In [22]: frame.ix[['a', 'b', 'c', 'd'], ['Texas', 'Ohio', 'California']]   	
Out[22]: 
   Texas  Ohio  California
a      1     0           2
b    NaN   NaN         NaN
c      4     3           5
d      7     6           8



=====================2. 丢弃指定轴上的项=======================================

In [23]: obj = Series(np.arange(5.0), index=['a', 'b', 'c', 'd', 'e'])

In [24]: obj
Out[24]: 
a    0
b    1
c    2
d    3
e    4
dtype: float64

In [25]: new_obj = obj.drop('c')			# 删除指定项，返回新对象

In [26]: obj
Out[26]: 
a    0
b    1
c    2
d    3
e    4
dtype: float64

In [27]: new_obj
Out[27]: 
a    0
b    1
d    3
e    4
dtype: float64

In [28]: obj.drop(['d', 'c'])				# 删除指定项，返回新对象
Out[28]: 
a    0
b    1
e    4
dtype: float64



In [29]: data = DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 
'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])

In [30]: data
Out[30]: 
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

In [31]: data.drop(['Ohio', 'Colorado'])		# 删除行
Out[31]: 
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15

In [32]: data.drop(['one', 'four'])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-32-0425ea037fff> in <module>()
----> 1 data.drop(['one', 'four'])

/usr/lib/python2.7/site-packages/pandas/core/generic.pyc in drop(self, labels, 
axis, level, inplace)
   1584                 new_axis = axis.drop(labels, level=level)
   1585             else:
-> 1586                 new_axis = axis.drop(labels)
   1587             dropped = self.reindex(**{axis_name: new_axis})
   1588             try:

/usr/lib/python2.7/site-packages/pandas/core/index.pyc in drop(self, labels)
   2342         mask = indexer == -1
   2343         if mask.any():
-> 2344             raise ValueError('labels %s not contained in axis' % 
labels[mask])
   2345         return self.delete(indexer)
   2346 

ValueError: labels ['one' 'four'] not contained in axis

In [33]: data.drop(['one', 'four'], axis=1)		# 删除列
Out[33]: 
          two  three
Ohio        1      2
Colorado    5      6
Utah        9     10
New York   13     14



======================3. 索引，选取和过滤====================================
Series 索引包括整数和字符串
DataFrame
obj[val]		选取单个列或者一组列
obj.ix[val]		选取单个行或者一组行
obj.ix[:, val]		选取单个列或者子集
obj.ix[val, val]	同时选取行和列
reindex			将一个或者多个轴匹配到新索引
icol，irow		根据整数位置，选取单列或者单行，并返回一个Series
xs
get_value, set_value



In [1]: from pandas import Series, DataFrame

In [2]: import pandas as pd

In [3]: import numpy as np

In [4]: obj = Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])

In [5]: obj
Out[5]: 
a    0
b    1
c    2
d    3
dtype: float64

In [6]: obj['b']		# 方式1
Out[6]: 1.0

In [7]: obj[1]			# 方式2
Out[7]: 1.0

In [8]: obj[2:4]		# 方式3
Out[8]: 
c    2
d    3
dtype: float64

In [10]: obj[['b', 'a']]	# 方式4
Out[10]: 
b    1
a    0
dtype: float64

In [11]: obj[[2, 1]]		# 方式5
Out[11]: 
c    2
b    1
dtype: float64

In [12]: obj[obj < 2]		# 方式6
Out[12]: 
a    0
b    1
dtype: float64


In [14]: data = DataFrame(np.arange(16.).reshape((4,4)), index=['Ohio', 
'Colorado', 'Utah', 'NewYork'], columns=['one', 'two', 'three', 'four'])  

In [15]: data
Out[15]: 
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
NewYork    12   13     14    15

In [16]: data['two']			# 方式1
Out[16]: 
Ohio         1
Colorado     5
Utah         9
NewYork     13
Name: two, dtype: float64

In [17]: data[['two', 'three']]		#方式2
Out[17]: 
          two  three
Ohio        1      2
Colorado    5      6
Utah        9     10
NewYork    13     14

In [18]: data[:2]			# 方式3
Out[18]: 
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7

In [19]: data[data['three'] > 5]	# 方式4
Out[19]: 
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
NewYork    12   13     14    15

In [20]: data < 5			# 方式5
Out[20]: 
            one    two  three   four
Ohio       True   True   True   True
Colorado   True  False  False  False
Utah      False  False  False  False
NewYork   False  False  False  False

In [21]: data[data<5] = 0	

In [22]: data
Out[22]: 
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
NewYork    12   13     14    15

In [23]: data
Out[23]: 
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
NewYork    12   13     14    15

In [24]: data.ix['Colorado', ['two', 'three']]	# 方式6
Out[24]: 
two      5
three    6
Name: Colorado, dtype: float64

In [25]: data.ix[['Ohio', 'Utah'], [3, 0, 1]]	# 方式7
Out[25]: 
      four  one  two
Ohio     0    0    0
Utah    11    8    9

In [26]: data.ix[2]				# 方式8
Out[26]: 
one       8
two       9
three    10
four     11
Name: Utah, dtype: float64

In [27]: data.ix[[:'Utah'], 'two']
  File "<ipython-input-27-593ec215343b>", line 1
    data.ix[[:'Utah'], 'two']
             ^
SyntaxError: invalid syntax


In [28]: data.ix[:'Utah', 'two']		# 方式9
Out[28]: 
Ohio        0
Colorado    5
Utah        9
Name: two, dtype: float64

In [29]: data.ix[data.three > 5, :3]		# 方式10
Out[29]: 
          one  two  three
Colorado    0    5      6
Utah        8    9     10
NewYork    12   13     14


=======================4. 算数运算与数据对齐=====================================

In [30]: s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
In [31]: s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

In [32]: s1
Out[32]: 
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64

In [33]: s2
Out[33]: 
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64

In [34]: s1 + s2 		# Series加法
Out[34]: 
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64



In [35]: df1 = DataFrame(np.argange(9.).reshape((3, 3)), columns=list('bcd'), 
index=['Ohio', 'Texas', 'Colorado']) 

In [37]: df2 = DataFrame(np.arange(12.0).reshape((4,3)), columns=list('bde'), 
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

In [38]: df1
Out[38]: 
          b  c  d
Ohio      0  1  2
Texas     3  4  5
Colorado  6  7  8

In [39]: df2
Out[39]: 
        b   d   e
Utah    0   1   2
Ohio    3   4   5
Texas   6   7   8
Oregon  9  10  11

In [40]: df1 + df2			# 索引为原来的并集，值为两者相加，无对应则为NaN
Out[40]: 
           b   c   d   e
Colorado NaN NaN NaN NaN
Ohio       3 NaN   6 NaN
Oregon   NaN NaN NaN NaN
Texas      9 NaN  12 NaN
Utah     NaN NaN NaN NaN


=========================5. 在算数方法中填充=====================
add
sub
div
mul


In [41]: df1.add(df2, fill_value=0)
Out[41]: 
          b   c   d   e
Colorado  6   7   8 NaN
Ohio      3   1   6   5
Oregon    9 NaN  10  11
Texas     9   4  12   8
Utah      0 NaN   1   2



=========================6. DataFrame 和Series之间运算==========================

In [42]: arr = np.arange(12.).reshape((3, 4))

In [43]: arr
Out[43]: 
array([[  0.,   1.,   2.,   3.],
       [  4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.]])

In [44]: arr[0]
Out[44]: array([ 0.,  1.,  2.,  3.])

In [45]: arr - arr[0]				# 广播
Out[45]: 
array([[ 0.,  0.,  0.,  0.],
       [ 4.,  4.,  4.,  4.],
       [ 8.,  8.,  8.,  8.]])



In [48]: frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), 
index=['Utah', 'Ohio', 'Texas', 'Colorado'])

In [49]: series = frame.ix[0]

In [50]: frame
Out[50]: 
          b   d   e
Utah      0   1   2
Ohio      3   4   5
Texas     6   7   8
Colorado  9  10  11

In [51]: se
%set_env         series           set              setattr          
settings-dev.py  

In [51]: series
Out[51]: 
b    0
d    1
e    2
Name: Utah, dtype: float64

In [52]: frame-series		# 默认，DataFrame和Series之间算数运算
				# 会将Series的索引匹配到DataFrame的列，
				# 然后沿着行一直向下广播
Out[52]: 
          b  d  e
Utah      0  0  0
Ohio      3  3  3
Texas     6  6  6
Colorado  9  9  9


In [58]: series2 = Series(range(3), index=['b', 'e', 'f'])

In [59]: frame
Out[59]: 
          b   d   e
Utah      0   1   2
Ohio      3   4   5
Texas     6   7   8
Colorado  9  10  11

In [60]: series2
Out[60]: 
b    0
e    1
f    2
dtype: int64

In [61]: frame + seri
series   series2  

In [61]: frame + series2		# 默认值
Out[61]: 
          b   d   e   f
Utah      0 NaN   3 NaN
Ohio      3 NaN   6 NaN
Texas     6 NaN   9 NaN
Colorado  9 NaN  12 NaN



In [62]: series3 = frame['d']

In [63]: frame
Out[63]: 
          b   d   e
Utah      0   1   2
Ohio      3   4   5
Texas     6   7   8
Colorado  9  10  11

In [64]: series3
Out[64]: 
Utah         1
Ohio         4
Texas        7
Colorado    10
Name: d, dtype: float64

In [65]: frame.sub(ser
series   series2  series3  

In [65]: frame.sub(series3, axis=0)	# 行匹配且在列上广播，必须使用算数运算方法
					# axis传入的轴号是希望匹配的轴
Out[65]: 
          b  d  e
Utah     -1  0  1
Ohio     -1  0  1
Texas    -1  0  1
Colorado -1  0  1

=========================7. 函数应用和映射=======================================

In [1]: from pandas import Series, DataFrame

In [2]: import pandas as pd

In [3]: import numpy as np

In [5]: frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), 
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

In [6]: frame
Out[6]: 
               b         d         e
Utah    0.095311 -0.474109  1.011295
Ohio   -1.437453 -1.879776 -0.685842
Texas   0.598684 -0.371974 -0.163844
Oregon -0.582684 -0.297039  0.133416


In [8]: np.abs(frame) 					# numpy适合DataFrame绝对值
Out[8]: 
               b         d         e
Utah    0.095311  0.474109  1.011295
Ohio    1.437453  1.879776  0.685842
Texas   0.598684  0.371974  0.163844
Oregon  0.582684  0.297039  0.133416

In [12]: frame = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), 
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

In [13]: frame
Out[13]: 
        b   d   e
Utah    0   1   2
Ohio    3   4   5
Texas   6   7   8
Oregon  9  10  11

In [14]: f = lambda x: x.max() - x.min()

In [15]: frame.apply(f)					# 函数映射
Out[15]: 
b    9
d    9
e    9
dtype: float64

In [16]: frame.apply(f, axis=1)				# 函数映射
Out[16]: 
Utah      2
Ohio      2
Texas     2
Oregon    2
dtype: float64


In [17]: frame1 = DataFrame(np.random.randn(4, 3), columns=list('bde'), 
index=['Utah', 'Ohio', 'Texas', 'Oregon']) 

In [18]: frame1
Out[18]: 
               b         d         e
Utah   -1.637270 -0.946841 -0.203747
Ohio   -0.651850 -0.144194 -0.516369
Texas   0.170670  0.948518  0.751367
Oregon -0.119071 -1.714624 -0.054608

In [19]: def f(x):
   ....:     return Series([x.min(), x.max()], index=['min', 'max'])


In [20]: frame1.apply(f)				# func返回多个值
Out[20]: 
           b         d         e
min -1.63727 -1.714624 -0.516369
max  0.17067  0.948518  0.751367

In [21]: format = lambda x: '%.2f' % x

In [22]: frame1.applymap(format)			# 格式化
Out[22]: 
            b      d      e
Utah    -1.64  -0.95  -0.20
Ohio    -0.65  -0.14  -0.52
Texas    0.17   0.95   0.75
Oregon  -0.12  -1.71  -0.05

In [23]: frame1['e'].map(format)			# Series有一个用于应用元素级的函数map
Out[23]: 
Utah      -0.20
Ohio      -0.52
Texas      0.75
Oregon    -0.05
Name: e, dtype: object


=========================8. 排序和排名============================================
In [1]: from pandas import Series, DataFrame

In [2]: import numpy as np

In [3]: import pandas as pd

In [4]: 

In [4]: obj = Series(range(4), index=['d', 'a', 'b', 'c'])

In [5]: obj
Out[5]: 
d    0
a    1
b    2
c    3
dtype: int64

In [6]: obj.sort_index()			# 按索引进行排序
Out[6]: 
a    1
b    2
c    3
d    0
dtype: int64

In [7]: frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], 
columns=['d', 'a', 'b', 'c'])

In [8]: frame
Out[8]: 
       d  a  b  c
three  0  1  2  3
one    4  5  6  7

In [9]: frame.sort_index()			# 默认对行轴索引进行排序
Out[9]: 
       d  a  b  c
one    4  5  6  7
three  0  1  2  3

In [10]: frame.sort_index(axis=1)		# axis=1对列轴索引进行排序
Out[10]: 
       a  b  c  d
three  1  2  3  0
one    5  6  7  4
  

In [11]: frame.sort_index(axis=1, ascending=False)	# 逆序
Out[11]: 
       d  c  b  a
three  0  3  2  1
one    4  7  6  5

In [12]: 

In [12]: obj
Out[12]: 
d    0
a    1
b    2
c    3
dtype: int64

In [13]: obj.order()					# 对值进行排序
Out[13]: 
d    0
a    1
b    2
c    3
dtype: int64

In [14]: obj = Series([4, -7, 3, 2])

In [15]: obj.order()
Out[15]: 
1   -7
3    2
2    3
0    4
dtype: int64

In [16]: obj = Series([4, np.nan, -7, np.nan, 3, 2])    

In [17]: obj
Out[17]: 
0     4
1   NaN
2    -7
3   NaN
4     3
5     2
dtype: float64

In [18]: obj.order()				# NaN排对最后
Out[18]: 
2    -7
5     2
4     3
0     4
1   NaN
3   NaN
dtype: float64

In [19]: help(frame.sort_index)


In [20]: frame = DataFrame({'b': [4, 7, -3 , 2], 'a': [0, 1, 0, 1]})

In [21]: frame
Out[21]: 
   a  b
0  0  4
1  1  7
2  0 -3
3  1  2


In [22]: frame.sort_index(by='b') 		# DataFrame对单列值进行排序
Out[22]: 
   a  b
2  0 -3
3  1  2
0  0  4
1  1  7

In [23]: frame.sort_index(by=['a', 'b'])	# DataFrame对多列值进行排序
Out[23]: 
   a  b
2  0 -3
0  0  4
3  1  2
1  1  7

In [24]: obj = Series([7, -5, 7, 4, 2, 0, 4])

In [25]: obj
Out[25]: 
0    7
1   -5
2    7
3    4
4    2
5    0
6    4
dtype: int64

In [26]: obj.rank()					# 排名：默认为各组分配一个平均排名
Out[26]: 
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64

In [27]: help(obj.rank())


In [28]: help(obj.rank) 


In [29]: obj.rank(method='first')	# 按值在原始数据中出现的顺序进行排名
Out[29]: 
0    6
1    1
2    7
3    4
4    3
5    2
6    5
dtype: float64

In [31]: obj.rank(method='max')
Out[31]: 
0    7
1    1
2    7
3    5
4    3
5    2
6    5
dtype: float64

In [32]: obj
Out[32]: 
0    7
1   -5
2    7
3    4
4    2
5    0
6    4
dtype: int64

In [33]: obj.rank(method='max', ascending=False)
Out[33]: 
0    2
1    7
2    2
3    4
4    5
5    6
6    4
dtype: float64

In [34]: frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 
5, 8, -2.5]})

In [35]: frame
Out[35]: 
   a    b    c
0  0  4.3 -2.0
1  1  7.0  5.0
2  0 -3.0  8.0
3  1  2.0 -2.5

In [36]: frame.rank(axis=1)	# 默认
Out[36]: 
   a  b  c
0  2  3  1
1  1  3  2
2  2  1  3
3  2  3  1


=========================9. 带有重复值的轴索引==================================
In [1]: from pandas import Series, DataFrame

In [2]: import numpy as np

In [3]: obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

In [4]: obj
Out[4]: 
a    0
a    1
b    2
b    3
c    4
dtype: int64

In [5]: obj.index.is_unique		# 索引是否唯一
Out[5]: False

In [7]: obj['a']
Out[7]: 
a    0
a    1
dtype: int64

In [8]: obj['c']
Out[8]: 4

In [9]: df = DataFrame(np.random.randn(4,3), index = ['a', 'a', 'b', 'b'])

In [10]: df
Out[10]: 
          0         1         2
a  0.114722  0.162901 -0.854571
a -0.239694 -2.651558  2.098905
b  0.496036 -1.614260  0.232271
b -2.565416  0.653180 -1.764811

In [11]: df
Out[11]: 
          0         1         2
a  0.114722  0.162901 -0.854571
a -0.239694 -2.651558  2.098905
b  0.496036 -1.614260  0.232271
b -2.565416  0.653180 -1.764811

In [13]: df.ix['b']			# 选择行
Out[13]: 
          0        1         2
b  0.496036 -1.61426  0.232271
b -2.565416  0.65318 -1.764811


=========================10 汇总和统计================================

1. 用axis，skinpa，level 约简
2.idxmax，idxmin
3.累计型
  cumsum
4. 常用方法
  count		（非NA值）
  describe	（对Series，DataFrame按列进行统计， 非NA）
  argmin
  argmax
  quantile
  skew
  kurt
  
  

In [15]: df = DataFrame([[1.5, np.nan], [2.0, -1.0], [np.nan, np.nan], [0.1, 
-0.2]], columns = ['one', 'two'], index = ['a', 'b', 'c', 'd'])

In [16]: df
Out[16]: 
   one  two
a  1.5  NaN
b  2.0 -1.0
c  NaN  NaN
d  0.1 -0.2

In [17]: df.sum()		# 默认按列
Out[17]: 
one    3.6
two   -1.2
dtype: float64

In [18]: df.sum(axis=0)		# axis  按列
Out[18]: 
one    3.6
two   -1.2
dtype: float64

In [19]: df.sum(axis=1)        # axis  按行
Out[19]: 
a    1.5
b    1.0
c    NaN
d   -0.1
dtype: float64

In [20]: df.mean()
Out[20]: 
one    1.2
two   -0.6
dtype: float64

In [21]: df.mean(axis=1)
Out[21]: 
a    1.50
b    0.50
c     NaN
d   -0.05
dtype: float64

In [22]: df.mean(axis=1, skipna=False)		# skipna 排除确实值
Out[22]: 
a     NaN
b    0.50
c     NaN
d   -0.05
dtype: float64


In [23]: df.id
df.idxmax  df.idxmin  

In [23]: df.idxmax
Out[23]: 
<bound method DataFrame.idxmax of    one  two
a  1.5  NaN
b  2.0 -1.0
c  NaN  NaN
d  0.1 -0.2>

In [24]: df.idxmax()			# 通过值取索引
Out[24]: 
one    b
two    d
dtype: object

In [25]: df
Out[25]: 
   one  two
a  1.5  NaN
b  2.0 -1.0
c  NaN  NaN
d  0.1 -0.2

In [26]: df.idxmin()			# 通过值取索引
Out[26]: 
one    d
two    b
dtype: object

In [27]: 

In [27]: 

In [27]: df.cu
df.cummax   df.cummin   df.cumprod  df.cumsum   

In [27]: df.cumsum()			# 累计和
Out[27]: 
   one  two
a  1.5  NaN
b  3.5 -1.0
c  NaN  NaN
d  3.6 -1.2

In [28]: df.describe()			# 统计
Out[28]: 
            one       two
count  3.000000  2.000000
mean   1.200000 -0.600000
std    0.984886  0.565685
min    0.100000 -1.000000
25%    0.800000 -0.800000
50%    1.500000 -0.600000
75%    1.750000 -0.400000
max    2.000000 -0.200000

In [29]: df
Out[29]: 
   one  two
a  1.5  NaN
b  2.0 -1.0
c  NaN  NaN
d  0.1 -0.2

In [30]: obj = Series(['a', 'a', 'b', 'c'] * 4)

In [31]: obj
Out[31]: 
0     a
1     a
2     b
3     c
4     a
5     a
6     b
7     c
8     a
9     a
10    b
11    c
12    a
13    a
14    b
15    c
dtype: object

In [32]: obj.describe()				# 非数值统计
Out[32]: 
count     16
unique     3
top        a
freq       8
dtype: object


=========================11相关系数，协防差==============================



=========================12唯一值，值计算，成员资格=======================
In [36]: obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

In [37]: obj
Out[37]: 
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object

In [38]: unqiue = obj.unique()			# 唯一值

In [39]: unqiue
Out[39]: array(['c', 'a', 'd', 'b'], dtype=object)

In [40]: uniques = obj.unique()      

In [41]: uniques
Out[41]: array(['c', 'a', 'd', 'b'], dtype=object)

In [42]: uniques.sort()

In [43]: uniques
Out[43]: array(['a', 'b', 'c', 'd'], dtype=object)

In [44]: obj.valu
obj.value_counts  obj.values        

In [44]: obj.value_counts()			# 统计个数
Out[44]: 
c    3
a    3
b    2
d    1
dtype: int64

In [45]: obj
Out[45]: 
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object

In [47]: obj.values				# obj值
Out[47]: array(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'], dtype=object)

In [49]: 

In [49]: import pandas as pd

In [51]: pd.value_counts(obj.values, sort=False)     # pandas中的value_counts  
Out[51]: 
a    3
c    3
b    2
d    1
dtype: int64

In [52]: mask = obj.isin(['b', 'c'])		# 判断矢量化的成员资格

In [54]: mask
Out[54]: 
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
dtype: bool

In [56]: obj[mask]  
Out[56]: 
0    c
5    b
6    b
7    c
8    c
dtype: object

In [57]: data = DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 
'Qu3': [1, 5, 2, 4, 4]})

In [58]: data
Out[58]: 
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4

In [59]: result = data.app
data.append    data.apply     data.applymap  

In [59]: result = data.appl
data.apply     data.applymap  

In [59]: result = data.apply(pd.value_counts)	# apply应用pd.value_counts函数

In [60]: result
Out[60]: 
   Qu1  Qu2  Qu3
1    1    1    1
2  NaN    2    1
3    2    2  NaN
4    2  NaN    2
5  NaN  NaN    1

In [61]: result = data.apply(pd.value_counts).fillna(0)

In [62]: result
Out[62]: 
   Qu1  Qu2  Qu3
1    1    1    1
2    0    2    1
3    2    2    0
4    2    0    2
5    0    0    1


=========================13 处理缺失数据============================
1.fillna      ＃填充数据，返回副本（inplace）
2.isnull
3.notnull
4.dropna      ＃对轴标签进行过滤,会产生副本,不会对原始数据进行修改（inplace）


In [1]: from pandas import Series, DataFrame

In [2]: import pandas as pd

In [3]: import numpy as np

In [4]: string_data = Series(['andy', 'love', 'you', np.nan])

In [5]: str
str          string_data  

In [5]: string_data
Out[5]: 
0    andy
1    love
2     you
3     NaN
dtype: object

In [6]: string_data.isnull()          ＃ isnull
Out[6]: 
0    False
1    False
2    False
3     True
dtype: bool

In [7]: string_data.notnull()         ＃notnull
Out[7]: 
0     True
1     True
2     True
3    False
dtype: bool

In [8]: from numpy import nan as NA

In [9]: data = Series([1, NA, 3.4, NA, 8])

In [10]: data
Out[10]: 
0    1.0
1    NaN
2    3.4
3    NaN
4    8.0
dtype: float64

In [11]: data.drop
data.drop             data.drop_duplicates  data.dropna           

In [11]: data.dropna()                ＃ 过滤NaN方式1
Out[11]: 
0    1.0
2    3.4
4    8.0
dtype: float64

In [12]: data[data.notnull()]         ＃ 过滤NaN方式2
Out[12]: 
0    1.0
2    3.4
4    8.0
dtype: float64

In [13]: df = DataFrame([[1, 6.5, 3], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3]])

In [14]: df
Out[14]: 
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3

In [15]: cleaned = df.drop
df.drop             df.drop_duplicates  df.dropna           

In [15]: cleaned = df.dropna()                ＃ 过滤所有的行和列，并且返回副本

In [16]: data
Out[16]: 
0    1.0
1    NaN
2    3.4
3    NaN
4    8.0
dtype: float64

In [18]: df
Out[18]: 
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3

In [19]: cleaned
Out[19]: 
   0    1  2
0  1  6.5  3

In [20]: df.dropna(how='all')               ＃ dropna 参数how
Out[20]: 
    0    1   2
0   1  6.5   3
1   1  NaN NaN
3 NaN  6.5   3

In [21]: df[4] = NA

In [22]: df
Out[22]: 
    0    1   2   4
0   1  6.5   3 NaN
1   1  NaN NaN NaN
2 NaN  NaN NaN NaN
3 NaN  6.5   3 NaN

In [23]: df.dropna(how='all', axis=1)                 ＃ dropna how axis
Out[23]: 
    0    1   2
0   1  6.5   3
1   1  NaN NaN
2 NaN  NaN NaN
3 NaN  6.5   3

In [24]: df
Out[24]: 
    0    1   2   4
0   1  6.5   3 NaN
1   1  NaN NaN NaN
2 NaN  NaN NaN NaN
3 NaN  6.5   3 NaN

In [25]: 

In [25]: 

In [25]: df = DataFrame(np.random.randn(7,5))

In [26]: df
Out[26]: 
          0         1         2         3         4
0 -1.216127 -0.603912 -0.042822  0.565946  2.206131
1 -0.097543 -0.457036  2.095455  0.470992 -0.128991
2  1.588960 -0.481922  0.954697  0.903250  1.639174
3  0.791613  1.739681 -0.333015  0.613277  1.602593
4 -0.990649  0.238119 -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [27]: df.ix[:4, 1] = NA;

In [28]: df.ix[:2, 2] = NA

In [29]: df
Out[29]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [30]: 

In [30]: 

In [30]: df.dropna(thresh=2)
Out[30]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [31]: df.dropna(thresh=3)
Out[31]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [32]: df.dropna(thresh=4)                          ＃ 只保留每列中NaN大于4个的数据
Out[32]: 
          0         1         2         3         4
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195



In [33]: 

In [33]: df
Out[33]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [34]: df.fillna(0)
Out[34]: 
          0         1         2         3         4
0 -1.216127  0.000000  0.000000  0.565946  2.206131
1 -0.097543  0.000000  0.000000  0.470992 -0.128991
2  1.588960  0.000000  0.000000  0.903250  1.639174
3  0.791613  0.000000 -0.333015  0.613277  1.602593
4 -0.990649  0.000000 -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [35]: df
Out[35]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [36]: df.fillna({1: 0.5, 2: 10})                       ＃ 按列字典的方式填充
Out[36]: 
          0         1          2         3         4
0 -1.216127  0.500000  10.000000  0.565946  2.206131
1 -0.097543  0.500000  10.000000  0.470992 -0.128991
2  1.588960  0.500000  10.000000  0.903250  1.639174
3  0.791613  0.500000  -0.333015  0.613277  1.602593
4 -0.990649  0.500000  -1.845738  0.999692  0.742633
5 -1.239701 -0.189727  -0.681514  0.164561  0.353365
6 -1.063661 -1.294236  -0.596899  1.245942 -1.082195

In [37]: 

In [37]: df
Out[37]: 
          0         1         2         3         4
0 -1.216127       NaN       NaN  0.565946  2.206131
1 -0.097543       NaN       NaN  0.470992 -0.128991
2  1.588960       NaN       NaN  0.903250  1.639174
3  0.791613       NaN -0.333015  0.613277  1.602593
4 -0.990649       NaN -1.845738  0.999692  0.742633
5 -1.239701 -0.189727 -0.681514  0.164561  0.353365
6 -1.063661 -1.294236 -0.596899  1.245942 -1.082195

In [38]: df.fillna({1: 0.5, 2: 10}, inplace=True)           ＃ 修改对象本身的值
Out[38]: 
          0         1          2         3         4
0 -1.216127  0.500000  10.000000  0.565946  2.206131
1 -0.097543  0.500000  10.000000  0.470992 -0.128991
2  1.588960  0.500000  10.000000  0.903250  1.639174
3  0.791613  0.500000  -0.333015  0.613277  1.602593
4 -0.990649  0.500000  -1.845738  0.999692  0.742633
5 -1.239701 -0.189727  -0.681514  0.164561  0.353365
6 -1.063661 -1.294236  -0.596899  1.245942 -1.082195

In [39]: df
Out[39]: 
          0         1          2         3         4
0 -1.216127  0.500000  10.000000  0.565946  2.206131
1 -0.097543  0.500000  10.000000  0.470992 -0.128991
2  1.588960  0.500000  10.000000  0.903250  1.639174
3  0.791613  0.500000  -0.333015  0.613277  1.602593
4 -0.990649  0.500000  -1.845738  0.999692  0.742633
5 -1.239701 -0.189727  -0.681514  0.164561  0.353365
6 -1.063661 -1.294236  -0.596899  1.245942 -1.082195

In [40]: 

In [40]: 

In [40]: 

In [40]: df = DataFrame(np.random.randn(6,3))

In [41]: df
Out[41]: 
          0         1         2
0  0.749667 -1.693472  0.350689
1 -0.495699  2.948116  1.239965
2 -2.117049  0.445181 -0.911898
3 -1.545899  2.628588  0.359061
4  0.654106 -1.151214 -0.725765
5  0.552225 -0.344756 -0.675617

In [42]: df.ix[2:, 1] = NA

In [43]: df.ix[4:, 2] = NA

In [44]: df
Out[44]: 
          0         1         2
0  0.749667 -1.693472  0.350689
1 -0.495699  2.948116  1.239965
2 -2.117049       NaN -0.911898
3 -1.545899       NaN  0.359061
4  0.654106       NaN       NaN
5  0.552225       NaN       NaN

In [45]: df.fillna(method='ffill')          ＃ fillna  method
Out[45]: 
          0         1         2
0  0.749667 -1.693472  0.350689
1 -0.495699  2.948116  1.239965
2 -2.117049  2.948116 -0.911898
3 -1.545899  2.948116  0.359061
4  0.654106  2.948116  0.359061
5  0.552225  2.948116  0.359061

In [46]: 

In [46]: df.fillna(method='ffill', limit=1)  ＃ fillna method limit（前向或后向连续填充的最大数量）
Out[46]: 
          0         1         2
0  0.749667 -1.693472  0.350689
1 -0.495699  2.948116  1.239965
2 -2.117049  2.948116 -0.911898
3 -1.545899       NaN  0.359061
4  0.654106       NaN  0.359061
5  0.552225       NaN       NaN



=========================14 层次化索引==============================
In [49]: data = Series(np.random.randn(10), index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

In [50]: data
Out[50]: 
a  1    0.583802
   2   -0.239605
   3    0.033435
b  1   -0.661445
   2   -0.334582
   3   -2.317539
c  1   -0.801222
   2   -0.072100
d  2    0.750577
   3   -0.304849
dtype: float64

In [51]: data.index
Out[51]: 
MultiIndex(levels=[[u'a', u'b', u'c', u'd'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])

In [52]: data
Out[52]: 
a  1    0.583802
   2   -0.239605
   3    0.033435
b  1   -0.661445
   2   -0.334582
   3   -2.317539
c  1   -0.801222
   2   -0.072100
d  2    0.750577
   3   -0.304849
dtype: float64

In [53]: data['b']                          ＃ 选择方式1
Out[53]: 
1   -0.661445
2   -0.334582
3   -2.317539
dtype: float64

In [54]: data['b':'c']                       ＃ 选择方式2
Out[54]: 
b  1   -0.661445
   2   -0.334582
   3   -2.317539
c  1   -0.801222
   2   -0.072100
dtype: float64

In [55]: data.ix[['b', 'd']]                  ＃ 选择方式3
Out[55]: 
b  1   -0.661445
   2   -0.334582
   3   -2.317539
d  2    0.750577
   3   -0.304849
dtype: float64

In [56]: data[:, 2]                             ＃ 选择方式4
Out[56]: 
a   -0.239605
b   -0.334582
c   -0.072100
d    0.750577
dtype: float64

In [57]: 

In [57]: data
Out[57]: 
a  1    0.583802
   2   -0.239605
   3    0.033435
b  1   -0.661445
   2   -0.334582
   3   -2.317539
c  1   -0.801222
   2   -0.072100
d  2    0.750577
   3   -0.304849
dtype: float64

In [58]: data.unstack()                   ＃ unstack 转成DataFrame
Out[58]: 
          1         2         3
a  0.583802 -0.239605  0.033435
b -0.661445 -0.334582 -2.317539
c -0.801222 -0.072100       NaN
d       NaN  0.750577 -0.304849

In [59]: data.unstack().stack()            ＃ stack 
Out[59]: 
a  1    0.583802
   2   -0.239605
   3    0.033435
b  1   -0.661445
   2   -0.334582
   3   -2.317539
c  1   -0.801222
   2   -0.072100
d  2    0.750577
   3   -0.304849
dtype: float64

In [60]: 

In [61]: df = DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Color'], ['Green', 'Red', 'Green']])

In [62]: df
Out[62]: 
     Ohio     Color
    Green Red Green
a 1     0   1     2
  2     3   4     5
b 1     6   7     8
  2     9  10    11

In [63]: df['Ohio']
Out[63]: 
     Green  Red
a 1      0    1
  2      3    4
b 1      6    7
  2      9   10

In [64]: df.index.name

In [65]: df.index.names
Out[65]: FrozenList([None, None])

In [66]: df.columns.names
Out[66]: FrozenList([None, None])

In [67]: df.index.names = ['key1', 'key2']

In [68]: df.columns.names = ['state', 'color']

In [69]: df
Out[69]: 
state      Ohio     Color
color     Green Red Green
key1 key2                
a    1        0   1     2
     2        3   4     5
b    1        6   7     8
     2        9  10    11


In [71]: df.swaplevel('key1', 'key2')           ＃ 重排分级顺序
Out[71]: 
state      Ohio     Color
color     Green Red Green
key2 key1                
1    a        0   1     2
2    a        3   4     5
1    b        6   7     8
2    b        9  10    11

In [72]: df.sort
df.sort        df.sort_index  df.sortlevel   

In [72]: df.sortlevel(1)                        ＃ 根据单个级别中的值对数据进行排序
Out[72]: 
state      Ohio     Color
color     Green Red Green
key1 key2                
a    1        0   1     2
b    1        6   7     8
a    2        3   4     5
b    2        9  10    11

In [73]: df.swaplevel(0,1)
Out[73]: 
state      Ohio     Color
color     Green Red Green
key2 key1                
1    a        0   1     2
2    a        3   4     5
1    b        6   7     8
2    b        9  10    11

In [74]: df.swaplevel(0,1).sortlevel(0)         ＃ 注意：从外到内排序，性能好
Out[74]: 
state      Ohio     Color
color     Green Red Green
key2 key1                
1    a        0   1     2
     b        6   7     8
2    a        3   4     5
     b        9  10    11


In [75]: df.index
Out[75]: 
MultiIndex(levels=[[u'a', u'b'], [1, 2]],
           labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
           names=[u'key1', u'key2'])

In [76]: df
Out[76]: 
state      Ohio     Color
color     Green Red Green
key1 key2                
a    1        0   1     2
     2        3   4     5
b    1        6   7     8
     2        9  10    11

In [77]: df.sum(level='key2')           ＃ 通过层次化索引对行求和
Out[77]: 
state  Ohio     Color
color Green Red Green
key2                 
1         6   8    10
2        12  14    16

In [78]: df.sum(level='color', axis=1)    ＃ 通过层次化索引对列求和
Out[78]: 
color      Green  Red
key1 key2            
a    1         2    1
     2         8    4
b    1        14    7
     2        20   10



=========================15 整数索引的问题===================================

In [79]: ser = Series(np.arange(3))

In [80]: ser
Out[80]: 
0    0
1    1
2    2
dtype: int64

In [81]: ser[-1]                # 问题1
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-81-3cbe0b873a9e> in <module>()
----> 1 ser[-1]

/Users/guoqiangzhang/env/lib/python2.7/site-packages/pandas/core/series.pyc in __getitem__(self, key)
    519     def __getitem__(self, key):
    520         try:
--> 521             result = self.index.get_value(self, key)
    522 
    523             if not np.isscalar(result):

/Users/guoqiangzhang/env/lib/python2.7/site-packages/pandas/core/index.pyc in get_value(self, series, key)
   1593 
   1594         try:
-> 1595             return self._engine.get_value(s, k)
   1596         except KeyError as e1:
   1597             if len(self) > 0 and self.inferred_type in ['integer','boolean']:

pandas/index.pyx in pandas.index.IndexEngine.get_value (pandas/index.c:3113)()

pandas/index.pyx in pandas.index.IndexEngine.get_value (pandas/index.c:2844)()

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:3704)()

pandas/hashtable.pyx in pandas.hashtable.Int64HashTable.get_item (pandas/hashtable.c:7224)()

pandas/hashtable.pyx in pandas.hashtable.Int64HashTable.get_item (pandas/hashtable.c:7162)()

KeyError: -1

In [82]: ser2 = Series(np.arange(3), index=['a', 'b', 'c'])   ＃ 非整数索引不会遇到此问题

In [83]: ser2[-1]
Out[83]: 2

In [84]: ser3 = Series(np.arange(3), index=[-5, 1, 3])

In [85]: ser3
Out[85]: 
-5    0
 1    1
 3    2
dtype: int64

In [86]: ser3.iget_value(2)               ＃ Series用iget_value 解决此问题
Out[86]: 2

In [87]: ser3.iget_value(1)
Out[87]: 1

In [88]: ser3.iget_value(0)
Out[88]: 0

In [89]: ser3.iget_value(-1)
Out[89]: 2

In [90]: df = DataFrame(np.arange(6).reshape(3,2), index=[2, 0, 1])

In [91]: df
Out[91]: 
   0  1
2  0  1
0  2  3
1  4  5

In [92]: df.irow(2)                       ＃ DataFrame用irow和icol解决此问题
Out[92]: 
0    4
1    5
Name: 1, dtype: int64

In [93]: df.icol(1)
Out[93]: 
2    1
0    3
1    5
Name: 1, dtype: int64








&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 数据加载、存储、文件格式
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
=========================1 读取文本文件===================================
read_csv
read_talbe
read_fwf
read_clipboard
to_csv
pickle
HDF5
xls


=========================2 读取数据库=====================================
import pymongo
import sqlite3


=========================3 利用Web Api操作网络资源=========================
import json
from lxml.html import pares


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
& 
& 数据归整化：清理、转换、合并、重塑
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
=========================1 合并数据集=====================================
pd.merge
pd.concat

In [98]: df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

In [99]: df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

In [100]: df1
Out[100]: 
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   a
6      6   b

In [101]: df2
Out[101]: 
   data2 key
0      0   a
1      1   b
2      2   d

In [102]: pd.merge(df1, df2)                          # merge
Out[102]: 
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0

In [103]: 

In [103]: pd.merge(df1, df2, on='key')                # on
Out[103]: 
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0

In [104]: 


In [106]: df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

In [107]: df4 = DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

In [108]: df3
Out[108]: 
   data1 lkey
0      0    b
1      1    b
2      2    a
3      3    c
4      4    a
5      5    a
6      6    b

In [109]: df4
Out[109]: 
   data2 rkey
0      0    a
1      1    b
2      2    d

In [110]: pd.merge(df3, df4, left_on='lkey', right_on='rkey')       # left_on right_on
Out[110]: 
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a

In [111]: pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='outer')      # how
Out[111]: 
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a
6      3    c    NaN  NaN
7    NaN  NaN      2    d

In [112]: pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='left')
Out[112]: 
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      2    a      0    a
3      3    c    NaN  NaN
4      4    a      0    a
5      5    a      0    a
6      6    b      1    b

In [113]: 

In [113]: 

In [113]: 

In [113]: left = DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})

In [114]: right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})

In [115]: left
Out[115]: 
  key1 key2  lval
0  foo  one     1
1  foo  two     2
2  bar  one     3

In [116]: right
Out[116]: 
  key1 key2  rval
0  foo  one     4
1  foo  one     5
2  bar  one     6
3  bar  two     7

In [117]: pd.merge(left, right, on=['key1', 'key2'], how='outer')   # on= [] how
Out[117]: 
  key1 key2  lval  rval
0  foo  one     1     4
1  foo  one     1     5
2  foo  two     2   NaN
3  bar  one     3     6
4  bar  two   NaN     7

In [118]: 

In [118]: 

In [118]: pd.merge(left, right, on='key1')
Out[118]: 
  key1 key2_x  lval key2_y  rval
0  foo    one     1    one     4
1  foo    one     1    one     5
2  foo    two     2    one     4
3  foo    two     2    one     5
4  bar    one     3    one     6
5  bar    one     3    two     7

In [119]: pd.merge(left, right, on='key1', suffixes=('_left', '_right'))    # suffixes
Out[119]: 
  key1 key2_left  lval key2_right  rval
0  foo       one     1        one     4
1  foo       one     1        one     5
2  foo       two     2        one     4
3  foo       two     2        one     5
4  bar       one     3        one     6
5  bar       one     3        two     7




In [121]: left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})

In [124]: left2 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

In [125]: left1
Out[125]: 
  key  value
0   a      0
1   b      1
2   a      2
3   a      3
4   b      4
5   c      5

In [126]: left2
Out[126]: 
   group_val
a        3.5
b        7.0

In [127]: pd.merge(left1, left2, left_on='key', right_index=True)   # 索引作为连接键
Out[127]: 
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0




In [128]: lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5)})

In [130]: righth = DataFrame(np.arange(12).reshape((6,2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]], columns=['event1', 'event2'])

In [131]: lefth
Out[131]: 
   data    key1  key2
0     0    Ohio  2000
1     1    Ohio  2001
2     2    Ohio  2002
3     3  Nevada  2001
4     4  Nevada  2002

In [132]: righth
Out[132]: 
             event1  event2
Nevada 2001       0       1
       2000       2       3
Ohio   2000       4       5
       2000       6       7
       2001       8       9
       2002      10      11

In [134]: pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)  ＃ on＝[]
Out[134]: 
   data    key1  key2  event1  event2
0     0    Ohio  2000       4       5
0     0    Ohio  2000       6       7
1     1    Ohio  2001       8       9
2     2    Ohio  2002      10      11
3     3  Nevada  2001       0       1


-----------------------------------------------------------------------------------------
In [136]: arr = np.arange(12).reshape((3, 4))

In [137]: arr
Out[137]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [138]: np.concatenate([arr, arr], axis=1)          # numpy concat axis=1
Out[138]: 
array([[ 0,  1,  2,  3,  0,  1,  2,  3],
       [ 4,  5,  6,  7,  4,  5,  6,  7],
       [ 8,  9, 10, 11,  8,  9, 10, 11]])

In [139]: np.concatenate([arr, arr], axis=0)          # numpy concat axis=0
Out[139]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [140]: 

In [140]: s1 = Series([0, 1], index=['a', 'b'])

In [141]: s2 = Series([2, 3, 4], index=['c', 'd', 'e'])

In [142]: s3 = Series([5, 6], index=['f', 'g'])



In [144]: pd.concat([s1, s2, s3])                     # concat ----> Series
Out[144]: 
a    0
b    1
c    2
d    3
e    4
f    5
g    6
dtype: int64

In [145]: pd.concat([s1, s2, s3], axis=1)             # concat ----> DataFrame
Out[145]: 
    0   1   2
a   0 NaN NaN
b   1 NaN NaN
c NaN   2 NaN
d NaN   3 NaN
e NaN   4 NaN
f NaN NaN   5
g NaN NaN   6

In [146]: 


In [147]: s1
Out[147]: 
a    0
b    1
dtype: int64



In [153]: s1
Out[153]: 
a    0
b    1
dtype: int64

In [154]: s3
Out[154]: 
f    5
g    6
dtype: int64

In [152]: s4 = pd.concat([s1 * 5, s3])


In [155]: s4
Out[155]: 
a    0
b    5
f    5
g    6
dtype: int64

In [156]: pd.concat([s1, s4], axis=1)                   # axis=1列
Out[156]: 
    0  1
a   0  0
b   1  5
f NaN  5
g NaN  6


In [159]: 

In [159]: pd.concat([s1, s4], axis=1, join='inner')       ＃ join
Out[159]: 
   0  1
a  0  0
b  1  5

In [160]: s1
Out[160]: 
a    0
b    1
dtype: int64

In [161]: s4
Out[161]: 
a    0
b    5
f    5
g    6
dtype: int64

In [162]: pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]) ＃join_axes 指定索引
Out[162]: 
    0   1
a   0   0
c NaN NaN
b   1   5
e NaN NaN


In [163]: s1
Out[163]: 
a    0
b    1
dtype: int64

In [164]: s3
Out[164]: 
f    5
g    6
dtype: int64

In [165]: s3
Out[165]: 
f    5
g    6
dtype: int64


In [167]: result = pd.concat([s1, s3, s3], keys=['one', 'two', 'three'])＃ keys层次化索引

In [168]: result
Out[168]: 
one    a    0
       b    1
two    f    5
       g    6
three  f    5
       g    6
dtype: int64


In [170]: pd.concat([s1, s3, s3], axis=1, keys=['one', 'two', 'three']) ＃  keys称为列头
Out[170]: 
   one  two  three
a    0  NaN    NaN
b    1  NaN    NaN
f  NaN    5      5
g  NaN    6      6





In [171]: df1 = DataFrame(np.arange(6).reshape((3, 2)), index=['a', 'b', 'c'], columns=['one', 'two'])

In [172]: df2 = DataFrame(5 + np.arange(4).reshape((2,2)), index=['a', 'c'], columns=['three', 'four'])

In [173]: df1
Out[173]: 
   one  two
a    0    1
b    2    3
c    4    5

In [174]: df2
Out[174]: 
   three  four
a      5     6
c      7     8

In [175]: pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])  ＃DataFrame keys 也类似
Out[175]: 
  level1     level2     
     one two  three four
a      0   1      5    6
b      2   3    NaN  NaN
c      4   5      7    8

In [176]: 

In [176]: pd.concat({'level1': df1, 'level2': df2}, axis=1)     ＃ 传入为字典的情况
Out[176]: 
  level1     level2     
     one two  three four
a      0   1      5    6
b      2   3    NaN  NaN
c      4   5      7    8

In [177]: pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower'])                                                        ＃ names
Out[177]: 
upper level1     level2     
lower    one two  three four
a          0   1      5    6
b          2   3    NaN  NaN
c          4   5      7    8

In [178]: 

In [178]: 

In [178]: df1 = DataFrame(np.random.randn(3,4), columns=['a', 'b', 'c', 'd'])

In [179]: df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

In [180]: df1
Out[180]: 
          a         b         c         d
0 -1.032764  1.527875 -1.207125 -0.587361
1 -0.323649 -0.392722  1.738613  2.381315
2 -1.051298 -0.193449  0.776090 -1.099194

In [181]: df2
Out[181]: 
          b         d         a
0  0.364376  1.400717 -0.577656
1  1.540299  1.714164  0.857042

In [182]: pd.concat([df1, df2])
Out[182]: 
          a         b         c         d
0 -1.032764  1.527875 -1.207125 -0.587361
1 -0.323649 -0.392722  1.738613  2.381315
2 -1.051298 -0.193449  0.776090 -1.099194
0 -0.577656  0.364376       NaN  1.400717
1  0.857042  1.540299       NaN  1.714164

In [183]: pd.concat([df1, df2], ignore_index=True)      ＃ 重新生成index
Out[183]: 
          a         b         c         d
0 -1.032764  1.527875 -1.207125 -0.587361
1 -0.323649 -0.392722  1.738613  2.381315
2 -1.051298 -0.193449  0.776090 -1.099194
3 -0.577656  0.364376       NaN  1.400717
4  0.857042  1.540299       NaN  1.714164




----------------------------------------------------------------------------------------
In [184]: a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=['f', 'e', 'd', 'c', 'b', 'a'])

In [185]: b = Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])

In [186]: a
Out[186]: 
f    NaN
e    2.5
d    NaN
c    3.5
b    4.5
a    NaN
dtype: float64

In [187]: b
Out[187]: 
f    0
e    1
d    2
c    3
b    4
a    5
dtype: float64

In [188]: b[-1] = np.nan

In [189]: b
Out[189]: 
f     0
e     1
d     2
c     3
b     4
a   NaN
dtype: float64

In [190]: b[:-2]
Out[190]: 
f    0
e    1
d    2
c    3
dtype: float64

In [191]: a[2:]
Out[191]: 
d    NaN
c    3.5
b    4.5
a    NaN
dtype: float64

In [192]: np.where(pd.isnull(a), b, a)
Out[192]: array([ 0. ,  2.5,  2. ,  3.5,  4.5,  nan])

In [194]: b[:-2].combine_first(a[2:])             ＃ Series combine_first 相当于np.where
Out[194]: 
a    NaN
b    4.5
c    3.0
d    2.0
e    1.0
f    0.0
dtype: float64

In [195]: df1 = DataFrame({'a': [1, np.nan, 5, np.nan], 'b': [np.nan, 2, np.nan, 6], 'c': range(2, 18, 4)})

In [196]: range(2, 18, 4)
Out[196]: [2, 6, 10, 14]

In [197]: df2 = DataFrame({'a': [5, 4, np.nan, 3, 7], 'b': [np.nan, 3, 4, 6, 8]})

In [198]: df1
Out[198]: 
    a   b   c
0   1 NaN   2
1 NaN   2   6
2   5 NaN  10
3 NaN   6  14

In [199]: df2
Out[199]: 
    a   b
0   5 NaN
1   4   3
2 NaN   4
3   3   6
4   7   8

In [200]: df1.combin
df1.combine        df1.combineAdd     df1.combineMult    df1.combine_first  

In [200]: df1.combine_first(df2)        ＃ Series combine_first 相当于np.where
Out[200]: 
   a   b   c
0  1 NaN   2
1  4   2   6
2  5   4  10
3  3   6  14
4  7   8 NaN

-----------------------------------------------------------------------
重塑层次化索引
stack
unstack
-----------------------------------------------------------------------

In [4]: df = DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['Ohio', 'Colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name='number'))

In [5]: df
Out[5]: 
number    one  two  three
state                    
Ohio        0    1      2
Colorado    3    4      5

In [6]: res = df.stack()      # 列转行

In [7]: res
Out[7]: 
state     number
Ohio      one       0
          two       1
          three     2
Colorado  one       3
          two       4
          three     5
dtype: int32

In [8]: res.unstack()                   # 行转列
Out[8]: 
number    one  two  three
state                    
Ohio        0    1      2
Colorado    3    4      5

In [9]: res.unstack(0)                  # 行转列
Out[9]: 
state   Ohio  Colorado
number                
one        0         3
two        1         4
three      2         5

In [10]: res.unstack('state')           # 行转列
Out[10]: 
state   Ohio  Colorado
number                
one        0         3
two        1         4
three      2         5

In [11]: 

In [11]: 

In [11]: s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])


In [13]: s2 = Series([4, 5, 6], index=['c', 'd', 'e']) 

In [14]: s1
Out[14]: 
a    0
b    1
c    2
d    3
dtype: int64

In [15]: s2
Out[15]: 
c    4
d    5
e    6
dtype: int64

In [16]: df2 = pd.concat([s1,s2], keys=['one', 'two'])

In [17]: df2
Out[17]: 
one  a    0
     b    1
     c    2
     d    3
two  c    4
     d    5
     e    6
dtype: int64

In [18]: data = pd.concat([s1,s2], keys=['one', 'two'])   

In [19]: data
Out[19]: 
one  a    0
     b    1
     c    2
     d    3
two  c    4
     d    5
     e    6
dtype: int64

In [20]: data.unstack()
Out[20]: 
      a   b  c  d   e
one   0   1  2  3 NaN
two NaN NaN  4  5   6

In [21]: 

In [21]: data.unstack().stack(dropna=False)
Out[21]: 
one  a     0
     b     1
     c     2
     d     3
     e   NaN
two  a   NaN
     b   NaN
     c     4
     d     5
     e     6
dtype: float64


http://python.jobbole.com/81212/   （pivot_table）



=========================2 转换=====================================
-----------------------------------------------------------------------
移除重复数据
duplicated
drop_duplicated
-----------------------------------------------------------------------


-----------------------------------------------------------------------
利用函数或映射进行数据转换
map
-----------------------------------------------------------------------
In [17]: df = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

In [18]: df
Out[18]: 
          food  ounces
0        bacon     4.0
1  pulled pork     3.0
2        bacon    12.0
3     Pastrami     6.0
4  corned beef     7.5
5        Bacon     8.0
6     pastrami     3.0
7    honey ham     5.0
8     nova lox     6.0

In [19]: meat_to_animal =  {
   ....:        'bacon': 'pig',
   ....:        'pulled pork': 'pig',
   ....:        'pastrami': 'cow',
   ....:        'corned beef': 'cow',
   ....:        'honey ham': 'pig',
   ....:        'nova lox': 'salmon' }

In [20]: meat_to_animal
Out[20]: 
{'bacon': 'pig',
 'corned beef': 'cow',
 'honey ham': 'pig',
 'nova lox': 'salmon',
 'pastrami': 'cow',
 'pulled pork': 'pig'}


In [22]: df['animal'] = df['food'].map(str.lower).map(meat_to_animal)      

In [23]: df
Out[23]: 
          food  ounces  animal
0        bacon     4.0     pig
1  pulled pork     3.0     pig
2        bacon    12.0     pig
3     Pastrami     6.0     cow
4  corned beef     7.5     cow
5        Bacon     8.0     pig
6     pastrami     3.0     cow
7    honey ham     5.0     pig
8     nova lox     6.0  salmon

In [24]: 

In [24]: 

In [24]: df['food'].map(lambda x: me)
meat_to_animal  memoryview      

In [24]: df['food'].map(lambda x: meat_to_animal[x.lower()])
Out[24]: 
0       pig
1       pig
2       pig
3       cow
4       cow
5       pig
6       cow
7       pig
8    salmon
Name: food, dtype: object



-----------------------------------------------------------------------
替换值
fillna
map
replace
-----------------------------------------------------------------------
In [25]: data = Series([1, -999, 2, -999, -1000, 3])

In [26]: data
Out[26]: 
0       1
1    -999
2       2
3    -999
4   -1000
5       3
dtype: int64

In [27]: data.replace(-999, np.nan)
Out[27]: 
0       1
1     NaN
2       2
3     NaN
4   -1000
5       3
dtype: float64

In [28]: data.replace([-999, -1000], np.nan)
Out[28]: 
0     1
1   NaN
2     2
3   NaN
4   NaN
5     3
dtype: float64

In [29]: data.replace([-999, -1000], [np.nan, 0])
Out[29]: 
0     1
1   NaN
2     2
3   NaN
4     0
5     3
dtype: float64

In [30]: data.replace({-999: np.nan, -1000: 100})
Out[30]: 
0      1
1    NaN
2      2
3    NaN
4    100
5      3
dtype: float64



In [31]: df = DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])

In [32]: df
Out[32]: 
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
New York    8    9     10    11

In [34]: df.index
Out[34]: Index([u'Ohio', u'Colorado', u'New York'], dtype='object')

In [35]: df.index.map(str.upper)
Out[35]: array(['OHIO', 'COLORADO', 'NEW YORK'], dtype=object)

In [36]: df.index = df.index.map(str.upper)     # map

In [37]: df
Out[37]: 
          one  two  three  four
OHIO        0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

In [38]: df.rename(index=str.title, columns=str.upper)    #rename
Out[38]: 
          ONE  TWO  THREE  FOUR
Ohio        0    1      2     3
Colorado    4    5      6     7
New York    8    9     10    11

In [39]: df.rename(columns=str.upper)           #rename      
Out[39]: 
          ONE  TWO  THREE  FOUR
OHIO        0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

In [40]: df
Out[40]: 
          one  two  three  four
OHIO        0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

In [41]: df.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})                                        #rename
Out[41]: 
          one  two  peekaboo  four
INDIANA     0    1         2     3
COLORADO    4    5         6     7
NEW YORK    8    9        10    11

In [42]: df
Out[42]: 
          one  two  three  four
OHIO        0    1      2     3
COLORADO    4    5      6     7
NEW YORK    8    9     10    11

In [43]: df.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}, inplace=True)                #rename replace

In [44]: df
Out[44]: 
          one  two  peekaboo  four
INDIANA     0    1         2     3
COLORADO    4    5         6     7
NEW YORK    8    9        10    11



-----------------------------------------------------------------------
离散化或面元划分
-----------------------------------------------------------------------
In [4]: ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

In [5]: bins = [18, 25, 35, 60, 100]

In [6]: cats = pd.cut(ages, bins)                                   ＃ cut

In [7]: cats
Out[7]: 
[(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
Length: 12
Categories (4, object): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]

In [9]: cats.codes                                                  # 索引编号
Out[9]: array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)


In [11]: cats.categories                                            ＃ 面元区间
Out[11]: Index([u'(18, 25]', u'(25, 35]', u'(35, 60]', u'(60, 100]'], dtype='object')

In [12]: pd.cut(ages,bins, right=False)                              ＃ 左闭右开
Out[12]: 
[[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [25, 35), [60, 100), [35, 60), [35, 60), [25, 35)]
Length: 12
Categories (4, object): [[18, 25) < [25, 35) < [35, 60) < [60, 100)]

In [13]: group_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']


In [15]: pd.cut(ages, bins, labels=group_names)                     ＃ labels 自定义面元名称
Out[15]: 
[Youth, Youth, Youth, YoungAdult, Youth, ..., YoungAdult, Senior, MiddleAge, MiddleAge, YoungAdult]
Length: 12
Categories (4, object): [Youth < YoungAdult < MiddleAge < Senior]

In [16]: data = np.random.rand(20)

In [17]: data
Out[17]: 
array([ 0.96492036,  0.4437016 ,  0.81558274,  0.5022861 ,  0.77521074,
        0.29755531,  0.79947303,  0.85371811,  0.06215576,  0.67135379,
        0.51442841,  0.95681006,  0.94520449,  0.40868635,  0.61001274,
        0.39264929,  0.55563888,  0.41387679,  0.83203188,  0.62974502])

In [18]: pd.cut(data, 4)
Out[18]: 
[(0.739, 0.965], (0.288, 0.514], (0.739, 0.965], (0.288, 0.514], (0.739, 0.965], ..., (0.288, 0.514], (0.514, 0.739], (0.288, 0.514], (0.739, 0.965], (0.514, 0.739]]
Length: 20
Categories (4, object): [(0.0613, 0.288] < (0.288, 0.514] < (0.514, 0.739] < (0.739, 0.965]]

In [19]: pd.cut(data, 4, prec)
%precision  precision=  

In [19]: pd.cut(data, 4, precisi)
%precision  precision=  

In [19]: pd.cut(data, 4, precision=2)
Out[19]: 
[(0.74, 0.96], (0.29, 0.51], (0.74, 0.96], (0.29, 0.51], (0.74, 0.96], ..., (0.29, 0.51], (0.51, 0.74], (0.29, 0.51], (0.74, 0.96], (0.51, 0.74]]
Length: 20
Categories (4, object): [(0.061, 0.29] < (0.29, 0.51] < (0.51, 0.74] < (0.74, 0.96]]

In [20]: 

In [20]: 

In [20]: 

In [20]: data
Out[20]: 
array([ 0.96492036,  0.4437016 ,  0.81558274,  0.5022861 ,  0.77521074,
        0.29755531,  0.79947303,  0.85371811,  0.06215576,  0.67135379,
        0.51442841,  0.95681006,  0.94520449,  0.40868635,  0.61001274,
        0.39264929,  0.55563888,  0.41387679,  0.83203188,  0.62974502])

In [21]: data = np.random.rand
np.random.rand             np.random.randn            np.random.random_integers  
np.random.randint          np.random.random           np.random.random_sample    

In [21]: data = np.random.randn(1000)

In [22]: data
Out[22]: 
array([ -1.10350151e+00,  -1.01649741e+00,   5.97264706e-01,
        -1.51894383e+00,  -1.22555528e+00,   1.10590351e+00,
        -2.38112799e-01,  -8.79647610e-02,  -1.09959201e+00,
        -1.23820496e+00,  -1.50624538e-02,   2.61908086e-01,
         1.56448986e+00])

In [23]: cats = pd.qcut(data, 4)                                        ＃ qcut， 4分位数

In [24]: cats
Out[24]: 
[[-3.31, -0.773], [-3.31, -0.773], (-0.0147, 0.666], [-3.31, -0.773], [-3.31, -0.773], ..., [-3.31, -0.773], [-3.31, -0.773], (-0.773, -0.0147], (-0.0147, 0.666], (0.666, 3.333]]
Length: 1000
Categories (4, object): [[-3.31, -0.773] < (-0.773, -0.0147] < (-0.0147, 0.666] < (0.666, 3.333]]

In [25]: pd.value_counts(cats)
Out[25]: 
(0.666, 3.333]       250
(-0.0147, 0.666]     250
(-0.773, -0.0147]    250
[-3.31, -0.773]      250
dtype: int64

In [26]: pd.qcut(0, 0.1, 0.5, 0.9, 1)

In [27]: pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])                                 ＃ 自定义分位数
Out[27]: 
[(-1.364, -0.0147], (-1.364, -0.0147], (-0.0147, 1.222], [-3.31, -1.364], (-1.364, -0.0147], ..., (-1.364, -0.0147], (-1.364, -0.0147], (-1.364, -0.0147], (-0.0147, 1.222], (1.222, 3.333]]
Length: 1000
Categories (4, object): [[-3.31, -1.364] < (-1.364, -0.0147] < (-0.0147, 1.222] < (1.222, 3.333]]

In [28]: cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])

In [29]: pd.value_counts(cats)
Out[29]: 
(-0.0147, 1.222]     400
(-1.364, -0.0147]    400
(1.222, 3.333]       100
[-3.31, -1.364]      100
dtype: int64


-----------------------------------------------------------------------
检测和过滤异常值
-----------------------------------------------------------------------
In [4]: np.random.seed(12345)
In [5]: df = DataFrame(np.random.rand)
np.random.rand             np.random.randn            np.random.random_integers 
 
np.random.randint          np.random.random           np.random.random_sample   
 

In [5]: df = DataFrame(np.random.randn(1000, 4))

In [6]: df
Out[6]: 
            0         1         2         3
0   -0.204708  0.478943 -0.519439 -0.555730
1    1.965781  1.393406  0.092908  0.281746
2    0.769023  1.246435  1.007189 -1.296221
..        ...       ...       ...       ...
999  0.089987  0.292291  1.177706  0.882755

[1000 rows x 4 columns]

In [7]: df.describe()
Out[7]: 
                 0            1            2            3
count  1000.000000  1000.000000  1000.000000  1000.000000
mean     -0.067684     0.067924     0.025598    -0.002298
std       0.998035     0.992106     1.006835     0.996794
min      -3.428254    -3.548824    -3.184377    -3.745356
25%      -0.774890    -0.591841    -0.641675    -0.644144
50%      -0.116401     0.101143     0.002073    -0.013611
75%       0.616366     0.780282     0.680391     0.654328
max       3.366626     2.653656     3.260383     3.927528

In [8]: col = df[3]

In [9]: col[np.abs(col) > 3]
Out[9]: 
97     3.927528
305   -3.399312
400   -3.745356
Name: 3, dtype: float64

In [10]: df[(np.abs(df) > 3).any(1)]			# 选出绝对值大于3的行
Out[10]: 
            0         1         2         3
5   -0.539741  0.476985  3.248944 -1.021228
97  -0.774363  0.552936  0.106061  3.927528
102 -0.655054 -0.565230  3.176873  0.959533
305 -2.315555  0.457246 -0.025907 -3.399312
324  0.050188  1.951312  3.260383  0.963301
400  0.146326  0.508391 -0.196713 -3.745356
499 -0.293333 -0.242459 -3.056990  1.918403
523 -3.428254 -0.296336 -0.439938 -0.867165
586  0.275144  1.179227 -3.184377  1.369891
808 -0.362528 -3.548824  1.553205 -2.186301
900  3.366626 -2.372214  0.851010  1.332846

In [11]: np.sign(df)			# 返回原始值的符号
Out[11]: 
     0  1  2  3
0   -1  1 -1 -1
1    1  1  1  1

999  1  1  1  1

[1000 rows x 4 columns]

In [12]: df[np.abs(df) > 3] = np.sign(df) * 3

In [13]: df.describe()
Out[13]: 
                 0            1            2            3
count  1000.000000  1000.000000  1000.000000  1000.000000
mean     -0.067623     0.068473     0.025153    -0.002081
std       0.995485     0.990253     1.003977     0.989736
min      -3.000000    -3.000000    -3.000000    -3.000000
25%      -0.774890    -0.591841    -0.641675    -0.644144
50%      -0.116401     0.101143     0.002073    -0.013611
75%       0.616366     0.780282     0.680391     0.654328
max       3.000000     2.653656     3.000000     3.000000


-----------------------------------------------------------------------
排列和随机采样
np.random.permutation
np.random.permuting
-----------------------------------------------------------------------

In [14]: sampler = np.random.permutation(5)
In [16]: sampler
Out[16]: array([1, 0, 2, 3, 4])

In [17]: sampler = np.random.permutation(5)

In [18]: sampler
Out[18]: array([1, 3, 4, 0, 2])

In [19]: df = DataFrame(np.arange(5*4).reshape(5, 4))

In [20]: df
Out[20]: 
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19

In [21]: df.take(sampler)
Out[21]: 
    0   1   2   3
1   4   5   6   7
3  12  13  14  15
4  16  17  18  19
0   0   1   2   3
2   8   9  10  11

In [22]: df.ix(sampler)
Out[22]: <pandas.core.indexing._IXIndexer at 0x9d6344c>

In [23]: df.take(np.random.permutation(len(df))[:3])
Out[23]: 
    0   1   2   3
1   4   5   6   7
3  12  13  14  15
0   0   1   2   3

In [24]: len(df)
Out[24]: 5

In [25]: 

In [25]: bag = np.array([5, 7, -1, 6, 4])

In [26]: bag
Out[26]: array([ 5,  7, -1,  6,  4])

In [27]: sampler = np.random.randint(0, len(bag), size=10)	# 采用替换的方式产生样本

In [28]: sampler
Out[28]: array([2, 2, 0, 3, 0, 4, 1, 1, 2, 3])

In [29]: draws = bag.take(sampler)

In [30]: draws
Out[30]: array([-1, -1,  5,  6,  5,  4,  7,  7, -1,  6])




-----------------------------------------------------------------------
计算指标/哑变量
-----------------------------------------------------------------------
In [33]: df = DataFrame({"key": ['b', 'b', 'a', 'c', 'a', 'b'], "data1": 
range(6)})

In [34]: df
Out[34]: 
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   b

In [35]: pd.get_dummies(df['key'])		# get_dummies
Out[35]: 
   a  b  c
0  0  1  0
1  0  1  0
2  1  0  0
3  0  0  1
4  1  0  0
5  0  1  0

In [36]: 

In [36]: dummies = pd.get_dummies(df['key'], prefix='key')  # get_dummies, 
prefix

In [37]: dummies
Out[37]: 
   key_a  key_b  key_c
0      0      1      0
1      0      1      0
2      1      0      0
3      0      0      1
4      1      0      0
5      0      1      0

In [38]: df[['data1']].join(dummies)
Out[38]: 
   data1  key_a  key_b  key_c
0      0      0      1      0
1      1      0      1      0
2      2      1      0      0
3      3      0      0      1
4      4      1      0      0
5      5      0      1      0

In [39]: values = np.random.rand(10)

In [40]: values
Out[40]: 
array([ 0.96588737,  0.17373658,  0.87592824,  0.75415641,  0.163486  ,
        0.23784062,  0.85564381,  0.58743194,  0.15314009,  0.5950288 ])

In [41]: bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

In [42]: pd.cut(values, bins)
Out[42]: 
[(0.8, 1], (0, 0.2], (0.8, 1], (0.6, 0.8], (0, 0.2], (0.2, 0.4], (0.8, 1], (0.4, 
0.6], (0, 0.2], (0.4, 0.6]]
Categories (5, object): [(0, 0.2] < (0.2, 0.4] < (0.4, 0.6] < (0.6, 0.8] < (0.8, 
1]]

In [45]: pd.get_dummies(pd.cut(values, bins))
Out[45]: 
   (0, 0.2]  (0.2, 0.4]  (0.4, 0.6]  (0.6, 0.8]  (0.8, 1]
0         0           0           0           0         1
1         1           0           0           0         0
2         0           0           0           0         1
3         0           0           0           1         0
4         1           0           0           0         0
5         0           1           0           0         0
6         0           0           0           0         1
7         0           0           1           0         0
8         1           0           0           0         0
9         0           0           1           0         0


=========================3 清理=====================================
-----------------------------------------------------------------------
字串操作
字符串内容方法
count
endswith，startwith
join
index
find
rfind
replace
strip，rstrip，lstrip
split
lower，upper
ljust，rjust

正则
http://regex.learncodethehardway.org/book/
模式匹配，替换，拆分
match，search，findall
sub
split



缺失数据
-----------------------------------------------------------------------



=========================4 重塑=====================================
-----------------------------------------------------------------------
pandas中矢量化的字符串函数
cat
contains
count
endswith, startwith
findall
get 
join
len
lower, upper
match
pad
center
repeat
replace
slice 
split
strip,rstrip,lstrip

-----------------------------------------------------------------------
In [4]: import numpy as np

In [5]: data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob': 
'rob@gmail.com', 'Wes': np.nan}

In [6]: data
Out[6]: 
{'Dave': 'dave@google.com',
 'Rob': 'rob@gmail.com',
 'Steve': 'steve@gmail.com',
 'Wes': nan}

In [7]: dt = Series(data)

In [8]: dt
Out[8]: 
Dave     dave@google.com
Rob        rob@gmail.com
Steve    steve@gmail.com
Wes                  NaN
dtype: object

In [9]: dt.isnull()
Out[9]: 
Dave     False
Rob      False
Steve    False
Wes       True
dtype: bool

In [10]: dt.str.contains('gmail')
Out[10]: 
Dave     False
Rob       True
Steve     True
Wes        NaN
dtype: object

In [11]: import re

In [12]: pattern = re.compile('([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.(A-Z{2,3})')

In [13]: pattern
Out[13]: re.compile(r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.(A-Z{2,3})')

In [15]: pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.(A-Z{2,3})'           

In [16]: dt.str.findall(pattern, flags=re.IGNORECASE)           
Out[16]: 
Dave      []
Rob       []
Steve     []
Wes      NaN
dtype: object

In [17]: dt.str.findall(pattern, flags=re.IGNORECASE)
Out[17]: 
Dave      []
Rob       []
Steve     []
Wes      NaN
dtype: object

In [18]: dt
Out[18]: 
Dave     dave@google.com
Rob        rob@gmail.com
Steve    steve@gmail.com
Wes                  NaN
dtype: object

In [19]: pattern
Out[19]: '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.(A-Z{2,3})'

In [20]: pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,3})'

In [21]: dt.str.findall(pattern, flags=re.IGNORECASE)
Out[21]: 
Dave     [(dave, google, com)]
Rob        [(rob, gmail, com)]
Steve    [(steve, gmail, com)]
Wes                        NaN
dtype: object

In [22]: dt.str.match(pattern, flags=re.IGNORECASE)       
/usr/lib/python2.7/site-packages/pandas/core/strings.py:351: UserWarning: In 
future versions of pandas, match will change to always return a bool indexer.
  " always return a bool indexer.", UserWarning)
Out[22]: 
Dave     (dave, google, com)
Rob        (rob, gmail, com)
Steve    (steve, gmail, com)
Wes                      NaN
dtype: object

In [23]: matchs = dt.str.findall(pattern, flags=re.IGNORECASE)

In [24]: matchs.str.get(1)
Out[24]: 
Dave    NaN
Rob     NaN
Steve   NaN
Wes     NaN
dtype: float64

In [25]: matchs.str.get(0)
Out[25]: 
Dave     (dave, google, com)
Rob        (rob, gmail, com)
Steve    (steve, gmail, com)
Wes                      NaN
dtype: object

In [26]: matchs.str.get(0).get(0)
Out[26]: ('dave', 'google', 'com')


-----------------------------------------------------------------------
示例：USDA视频数据库
-----------------------------------------------------------------------
import json
db = 
json.load(open('/home/andy/Documents/documents/python/mypandas/foods-2011-10-03.
json'))
len(db)
db.head
db.head()
db.describe()
db[0]
len(db[0])
db[0].keys()
db[0]['nutrients'][0]
nutrients = DataFrame(db[0]['nutrients'][0])
nutrients = DataFrame(db[0]['nutrients'])
nutrients
info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)
info[:5]
info
pd.value_counts(info.group)
nutrients = []
for res in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = res['id']
    nutrients.append(fnuts)
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = res['id']
    nutrients.append(fnuts)
nutrients
len(nutrients)
nutrients[0]
history
nutrients.duplicated().sum()
nutrients = pd.concat(nutrients, ignore_index=True)
nutrients
nutrients.duplicated().sum()
nutrients = nutrients.drop_duplicates()
nutrients
info
col_mapping = {'description': 'food', 'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
info
nutrients = nutrients.rename(columns=col_mapping, copy=Flase)
nutrients = nutrients.rename(columns=col_mapping, copy=False)
ndata = pd.merge(nutrients, info, on='id', how='outer')
ndata[:2]



=========================5 绘图和可视化=====================================
d3.js
matplotlib (api) 重要的是学习官方的实例
  mplot3d
  basemap

chaco	http://code.enthought.com/chaco/   (交互式好，渲染速度快)
mayavi
-----------------------------------------------------------------------
颜色，标记，线性
-----------------------------------------------------------------------
In [3]: import matplotlib.pyplot as plt

In [4]: import numpy as np

In [5]: plt.plot(randn(30).cumsum(), 'ko--')                  ＃标记
Out[5]: [<matplotlib.lines.Line2D at 0x115e71110>]

In [12]: plt.plot(randn(30).cumsum(), 'g--')                    ＃ g－－颜色
Out[12]: [<matplotlib.lines.Line2D at 0x117226d10>]

In [15]: plt.plot(randn(30).cumsum(), linestyle='--', color='g')   ＃ linestyle 线型
Out[15]: [<matplotlib.lines.Line2D at 0x117326350>]



-----------------------------------------------------------------------
刻度，标记，图例
-----------------------------------------------------------------------
In [21]: data = randn(30).cumsum()

In [22]: data
Out[22]: 
array([ -0.71937248,  -0.2185741 ,  -0.02641337,  -0.149804  ,
        -1.25909039,  -1.03030546,  -1.46650966,  -0.98655346,
        -1.09277606,  -1.72378266,  -2.70479244,  -3.78121093,
        -3.6506319 ,  -1.69150169,  -2.069725  ,  -3.31299434,
        -4.25089048,  -4.63475893,  -5.09985459,  -6.21975364,
        -6.94440855,  -6.31117895,  -6.87125948,  -8.08452774,
        -8.93959736,  -9.60907252, -10.23138836,  -9.85884595,
        -9.94283278, -10.46412795])

In [24]: plt.plot(data, 'k--', label="Default")
Out[24]: [<matplotlib.lines.Line2D at 0x117470410>]

In [25]: plp.plot(data, 'k--', dra)
drange               draw                 draw_if_interactive  

In [26]: plt.plot(data, 'k--', drawstyle='steps-post', label='steps-post')
Out[26]: [<matplotlib.lines.Line2D at 0x117313e90>]

In [27]: plt.legend(loc='best')                     ＃ 添加图例
Out[27]: <matplotlib.legend.Legend at 0x117519150>

-----------------------------------------------------------------------
设置标题，轴标签，刻度，以及刻度标签
注解以及在subplot上绘图
matplotlib配置
将图表保存到文件
-----------------------------------------------------------------------




-----------------------------------------------------------------------
pandas中的绘图函数
  数据表示
  图例
  标题
  刻度标签
  注解
-----------------------------------------------------------------------


=========================6 数据聚合与分组运算=====================================
拆分pandas对象
计算分组摘要：计数，平均值，标准差，自定义函数，对DataFrame列应用各种函数
应用组内转换或其他运算：规格化，线性回归，排名，选取子集
计算透视表和交叉表
执行分位数

-----------------------------------------------------------------------
分组
  通过key进行分组
  通过字典或者Series进行分组
  通过函数进行分组
  通过索引级别分组


In [1]: from pandas import Series, DataFrame

In [2]: import pandas as pd

In [3]: import numpy ad np
  File "<ipython-input-3-3c49a9e0110a>", line 1
    import numpy ad np
                  ^
SyntaxError: invalid syntax


In [4]: import numpy as np

In [5]: df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'], 'key2': ['one', 'two', 'one', 'two', 'one'], 'data1': np.random.randn(5), 'data2': np.random.randn(5)})

In [6]: df
Out[6]: 
      data1     data2 key1 key2
0  1.020862 -0.875639    a  one
1  1.672014 -0.789872    a  two
2 -0.141552  0.577809    b  one
3  0.497131  0.169680    b  two
4  0.381957 -1.623030    a  one

In [7]: for name, group in df.groupby('key1')
  File "<ipython-input-7-7c2e5928efeb>", line 1
    for name, group in df.groupby('key1')
                                         ^
SyntaxError: invalid syntax


In [8]: for name, group in df.groupby('key1'):
   ...:     print name
   ...:     print group
   ...:     
a
      data1     data2 key1 key2
0  1.020862 -0.875639    a  one
1  1.672014 -0.789872    a  two
4  0.381957 -1.623030    a  one
b
      data1     data2 key1 key2
2 -0.141552  0.577809    b  one
3  0.497131  0.169680    b  two

In [9]: df.groupby('key1')
Out[9]: <pandas.core.groupby.DataFrameGroupBy object at 0x10ebfc9d0>

In [10]: for (key1, key2), group in df.groupby(['key1', 'key2']):
   ....:     print key1, key2
   ....:     print group
   ....:     
a one
      data1     data2 key1 key2
0  1.020862 -0.875639    a  one
4  0.381957 -1.623030    a  one
a two
      data1     data2 key1 key2
1  1.672014 -0.789872    a  two
b one
      data1     data2 key1 key2
2 -0.141552  0.577809    b  one
b two
      data1    data2 key1 key2
3  0.497131  0.16968    b  two

In [11]: list(df.groupby('key1'))
Out[11]: 
[('a',       data1     data2 key1 key2
  0  1.020862 -0.875639    a  one
  1  1.672014 -0.789872    a  two
  4  0.381957 -1.623030    a  one), ('b',       data1     data2 key1 key2
  2 -0.141552  0.577809    b  one
  3  0.497131  0.169680    b  two)]

In [12]: dict(list(df.groupby('key1')))
Out[12]: 
{'a':       data1     data2 key1 key2
 0  1.020862 -0.875639    a  one
 1  1.672014 -0.789872    a  two
 4  0.381957 -1.623030    a  one, 'b':       data1     data2 key1 key2
 2 -0.141552  0.577809    b  one
 3  0.497131  0.169680    b  two}

In [13]: df.dtypes
Out[13]: 
data1    float64
data2    float64
key1      object
key2      object
dtype: object

In [14]: df.groupby('key1')['data1']
Out[14]: <pandas.core.groupby.SeriesGroupBy object at 0x10ece7f90>

In [15]: df.groupby('key1')[['data2']]
Out[15]: <pandas.core.groupby.DataFrameGroupBy object at 0x10ece7b50>

In [16]: df['data1'].groupby(df['key1'])
Out[16]: <pandas.core.groupby.SeriesGroupBy object at 0x10ece7cd0>

In [17]: 

In [17]: 

In [17]: people = DataFrame(np.random.randn(5,5), column)
column_stack  columns=      

In [17]: people = DataFrame(np.random.randn(5,5), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Tr])
True   True_  

In [17]: people = DataFrame(np.random.randn(5,5), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

In [18]: people
Out[18]: 
               a         b         c         d         e
Joe    -0.989974 -0.113296 -0.409059 -1.723388 -0.023146
Steve   0.702044 -0.015409  0.158256 -0.024481  0.848151
Wes     0.609179 -1.367265  0.614181  0.273383  0.990522
Jim    -1.118556 -0.430390  0.450853 -3.593245 -0.828601
Travis  0.895310  1.177308 -1.889844  1.036905  0.489765

In [19]: people.ix([2:3], ['b', 'c']) = np.nan
  File "<ipython-input-19-069133ea2447>", line 1
    people.ix([2:3], ['b', 'c']) = np.nan
                ^
SyntaxError: invalid syntax


In [20]: people.ix(2:3, ['b', 'c']) = np.nan
  File "<ipython-input-20-6b4fb16d415d>", line 1
    people.ix(2:3, ['b', 'c']) = np.nan
               ^
SyntaxError: invalid syntax


In [21]: people.ix[2:3, ['b', 'c']] = np.nan

In [22]: people
Out[22]: 
               a         b         c         d         e
Joe    -0.989974 -0.113296 -0.409059 -1.723388 -0.023146
Steve   0.702044 -0.015409  0.158256 -0.024481  0.848151
Wes     0.609179       NaN       NaN  0.273383  0.990522
Jim    -1.118556 -0.430390  0.450853 -3.593245 -0.828601
Travis  0.895310  1.177308 -1.889844  1.036905  0.489765

In [23]: mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}

In [24]: by_column = people.groupby(mapping, axis=1)        ＃ 根据字典分组

In [25]: by_column
Out[25]: <pandas.core.groupby.DataFrameGroupBy object at 0x10ece7050>

In [26]: by_column.sum()
Out[26]: 
            blue       red
Joe    -2.132447 -1.126416
Steve   0.133775  1.534786
Wes     0.273383  1.599701
Jim    -3.142391 -2.377548
Travis -0.852939  2.562384

In [27]: 

In [27]: 

In [27]: map_series = Series(mapping)                       ＃ 根据Series分组

In [28]: map
map         map_series  mapping     

In [28]: map_series
Out[28]: 
a       red
b       red
c      blue
d      blue
e       red
f    orange
dtype: object

In [29]: people.groupby(map_series, axis=1).count()
Out[29]: 
        blue  red
Joe        2    3
Steve      2    3
Wes        1    2
Jim        2    3
Travis     2    3

In [30]: 

In [30]: 

In [30]: 

In [30]: people.groupby(len).sum()                            ＃ 根据函数分组
Out[30]: 
          a         b         c         d         e
3 -1.499352 -0.543687  0.041795 -5.043250  0.138776
5  0.702044 -0.015409  0.158256 -0.024481  0.848151
6  0.895310  1.177308 -1.889844  1.036905  0.489765

In [31]: key_list = ['one', 'one', 'one', 'two', 'two']

In [32]: people.groupby([len, key])
key1      key2      key_list  

In [32]: people.groupby([len, key_list]).min()                ＃ 根据函数分组
Out[32]: 
              a         b         c         d         e
3 one -0.989974 -0.113296 -0.409059 -1.723388 -0.023146
  two -1.118556 -0.430390  0.450853 -3.593245 -0.828601
5 one  0.702044 -0.015409  0.158256 -0.024481  0.848151
6 two  0.895310  1.177308 -1.889844  1.036905  0.489765

In [33]: 

In [33]: 

In [33]: 

In [33]: columns = pd.MultiIndex.fro
pd.MultiIndex.from_arrays   pd.MultiIndex.from_product  pd.MultiIndex.from_tuples

In [33]: columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'], [1, 3, 5, 1, 3]], names=['cty', 'tenor'])

In [34]: colum
column_stack  columns       

In [34]: columns
Out[34]: 
MultiIndex(levels=[[u'JP', u'US'], [1, 3, 5]],
           labels=[[1, 1, 1, 0, 0], [0, 1, 2, 0, 1]],
           names=[u'cty', u'tenor'])


In [35]: hier_df = DataFrame(np.random.randn(4,5), columns=columns)       ＃  根据索引级别分组

In [36]: hier_df
Out[36]: 
cty          US                            JP          
tenor         1         3         5         1         3
0     -0.262442  0.614584 -0.329450 -0.064656  1.030729
1     -0.812080 -0.232987  0.659975  0.843913 -1.380549
2      1.733506 -2.395643 -1.020630 -0.104583 -1.317876
3     -1.229427 -0.082738 -0.122432 -1.539282  0.133055

In [37]: hier_df.groupby(level='cty', axis=1).count()
Out[37]: 
cty  JP  US
0     2   3
1     2   3
2     2   3
3     2   3



-----------------------------------------------------------------------
聚合
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
-----------------------------------------------------------------------


-----------------------------------------------------------------------
  面向列的多函数应用
    对不同的列使用不同的函数
    一次应用多个函数
-----------------------------------------------------------------------
In [5]: tips = pd.read_csv('/Users/guoqiangzhang/Documents/python/mypandas/tips.csv')

In [6]: tips['tip_pct'] = tips['tip'] / tips['total_bill']

In [7]: tips[:6]
Out[7]: 
   total_bill   tip     sex smoker  day    time  size   tip_pct
0       16.99  1.01  Female     No  Sun  Dinner     2  0.059447
1       10.34  1.66    Male     No  Sun  Dinner     3  0.160542
2       21.01  3.50    Male     No  Sun  Dinner     3  0.166587
3       23.68  3.31    Male     No  Sun  Dinner     2  0.139780
4       24.59  3.61  Female     No  Sun  Dinner     4  0.146808
5       25.29  4.71    Male     No  Sun  Dinner     4  0.186240

In [8]: tips.describe()
Out[8]: 
       total_bill         tip        size     tip_pct
count  244.000000  244.000000  244.000000  244.000000
mean    19.785943    2.998279    2.569672    0.160803
std      8.902412    1.383638    0.951100    0.061072
min      3.070000    1.000000    1.000000    0.035638
25%     13.347500    2.000000    2.000000    0.129127
50%     17.795000    2.900000    2.000000    0.154770
75%     24.127500    3.562500    3.000000    0.191475
max     50.810000   10.000000    6.000000    0.710345

In [9]: grouped = tips.groupby(['sex', 'smoker'])


TypeError: unhashable type

In [11]: grouped_pct = grouped['tip_pct']

In [14]: grouped_pct.agg('mean')
Out[14]: 
sex     smoker
Female  No        0.156921
        Yes       0.182150
Male    No        0.160669
        Yes       0.152771
Name: tip_pct, dtype: float64

In [15]: grouped_pct.agg(['mean', 'std'])                 ＃ 对tip_pct 列应用mean std函数
Out[15]: 
                   mean       std
sex    smoker                    
Female No      0.156921  0.036421
       Yes     0.182150  0.071595
Male   No      0.160669  0.041849
       Yes     0.152771  0.090588

In [16]: grouped_pct.agg([('foo', 'mean'), ('bar', 'std')])    ＃ 重命名用的元组结构
Out[16]: 
                    foo       bar
sex    smoker                    
Female No      0.156921  0.036421
       Yes     0.182150  0.071595
Male   No      0.160669  0.041849
       Yes     0.152771  0.090588

In [17]: 

In [17]: 

In [17]: functions = ['count', 'mean', 'max']

In [18]: result = grouped
grouped      grouped_pct  

In [18]: result = grouped['tip_pct', 'total_bill'].agg(functions)   ＃ 对所有列应用同一个函数是列表结构

In [19]: resul
result       result_type  

In [19]: result
Out[19]: 
              tip_pct                     total_bill                  
                count      mean       max      count       mean    max
sex    smoker                                                         
Female No          54  0.156921  0.252672         54  18.105185  35.83
       Yes         33  0.182150  0.416667         33  17.977879  44.30
Male   No          97  0.160669  0.291990         97  19.791237  48.33
       Yes         60  0.152771  0.710345         60  22.284500  50.81

In [20]: 

In [20]: ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]

In [21]: group
grouped      grouped_pct  

In [21]: grouped['tip_pct', 'total_bill'].agg(ftuples)
Out[21]: 
                   tip_pct              total_bill           
              Durchschnitt Abweichung Durchschnitt Abweichung
sex    smoker                                                
Female No         0.156921   0.001327    18.105185  53.092422
       Yes        0.182150   0.005126    17.977879  84.451517
Male   No         0.160669   0.001751    19.791237  76.152961
       Yes        0.152771   0.008206    22.284500  98.244673


In [23]: 

In [23]: grouped.agg({'tip': np.max, 'size': 'sum'})    ＃ 对所有列应用同一个函数是字典结构
Out[23]: 
                tip  size
sex    smoker            
Female No       5.2   140
       Yes      6.5    74
Male   No       9.0   263
       Yes     10.0   150

In [24]: grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'], 'size': 'sum'})
Out[24]: 
                tip_pct                               size
                    min       max      mean       std  sum
sex    smoker                                             
Female No      0.056797  0.252672  0.156921  0.036421  140
       Yes     0.056433  0.416667  0.182150  0.071595   74
Male   No      0.071804  0.291990  0.160669  0.041849  263
       Yes     0.035638  0.710345  0.152771  0.090588  150


-----------------------------------------------------------------------
  以无索引的形式返回聚合数据
-----------------------------------------------------------------------
In [25]: tips.groupby(['sex', 'smoker'], as_index=False).mean()
Out[25]: 
      sex smoker  total_bill       tip      size   tip_pct
0  Female     No   18.105185  2.773519  2.592593  0.156921
1  Female    Yes   17.977879  2.931515  2.242424  0.182150
2    Male     No   19.791237  3.113402  2.711340  0.160669
3    Male    Yes   22.284500  3.051167  2.500000  0.152771

In [26]: tips.groupby(['sex', 'smoker'], as_index=True).mean()
Out[26]: 
               total_bill       tip      size   tip_pct
sex    smoker                                          
Female No       18.105185  2.773519  2.592593  0.156921
       Yes      17.977879  2.931515  2.242424  0.182150
Male   No       19.791237  3.113402  2.711340  0.160669
       Yes      22.284500  3.051167  2.500000  0.152771

In [27]: 

-----------------------------------------------------------------------
  transform和apply应用
    transform: 将一个函数应用到各个分组
    apply: 拆分－应用－合并
-----------------------------------------------------------------------

In [27]: people = DataFrame(np.random.randn(5,5), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

In [29]: people
Out[29]: 
               a         b         c         d         e
Joe    -0.828596  0.073512 -0.871651 -3.323116 -0.121708
Steve  -0.949652  1.310786 -0.515785  1.131292 -0.698097
Wes    -0.197901  1.282998  0.544361 -1.103824 -0.043458
Jim    -1.224254  0.478567 -0.134686 -0.751795 -2.041950
Travis -0.515863 -0.765875 -1.860462  0.507369 -0.272514

In [30]: key = ['one', 'two', 'one', 'two', 'one']

In [31]: people.groupby(key).mean()
Out[31]: 
            a         b         c         d         e
one -0.514120  0.196878 -0.729251 -1.306524 -0.145894
two -1.086953  0.894677 -0.325235  0.189749 -1.370024

In [32]: people.groupby(key).transform(np.mean)         ＃ transform应用
Out[32]: 
               a         b         c         d         e
Joe    -0.514120  0.196878 -0.729251 -1.306524 -0.145894
Steve  -1.086953  0.894677 -0.325235  0.189749 -1.370024
Wes    -0.514120  0.196878 -0.729251 -1.306524 -0.145894
Jim    -1.086953  0.894677 -0.325235  0.189749 -1.370024
Travis -0.514120  0.196878 -0.729251 -1.306524 -0.145894

In [33]: 

In [33]: 

In [33]: def demean(arr):
   ....:     return arr - arr.mean()
   ....: 

In [34]: demeaned = people.groupby(key).transform(demean)

In [35]: demeaned
Out[35]: 
               a         b         c         d         e
Joe    -0.314476 -0.123366 -0.142400 -2.016592  0.024185
Steve   0.137301  0.416110 -0.190549  0.941543  0.671926
Wes     0.316219  1.086120  1.273612  0.202700  0.102435
Jim    -0.137301 -0.416110  0.190549 -0.941543 -0.671926
Travis -0.001743 -0.962753 -1.131211  1.813892 -0.126621

In [37]: demeaned.groupby(key).mean()
Out[37]: 
                a  b             c             d             e
one  3.700743e-17  0  0.000000e+00  7.401487e-17  0.000000e+00
two  5.551115e-17  0  2.775558e-17  0.000000e+00  5.551115e-17

In [38]: 

In [38]: 

In [38]: def top(df, n=5, column='tip_pct'):
   ....:     return df.sort_index(by=column)[-n:]
   ....: 

In [39]: top(tips, 6)
Out[39]: 
     total_bill   tip     sex smoker  day    time  size   tip_pct
109       14.31  4.00  Female    Yes  Sat  Dinner     2  0.279525
183       23.17  6.50    Male    Yes  Sun  Dinner     4  0.280535
232       11.61  3.39    Male     No  Sat  Dinner     2  0.291990
67         3.07  1.00  Female    Yes  Sat  Dinner     1  0.325733
178        9.60  4.00  Female    Yes  Sun  Dinner     2  0.416667
172        7.25  5.15    Male    Yes  Sun  Dinner     2  0.710345

In [40]: tips.groupby('smoker').apply(top)          ＃ apply 应用
Out[40]: 
            total_bill   tip     sex smoker   day    time  size   tip_pct
smoker                                                                   
No     88        24.71  5.85    Male     No  Thur   Lunch     2  0.236746
       185       20.69  5.00    Male     No   Sun  Dinner     5  0.241663
       51        10.29  2.60  Female     No   Sun  Dinner     2  0.252672
       149        7.51  2.00    Male     No  Thur   Lunch     2  0.266312
       232       11.61  3.39    Male     No   Sat  Dinner     2  0.291990
Yes    109       14.31  4.00  Female    Yes   Sat  Dinner     2  0.279525
       183       23.17  6.50    Male    Yes   Sun  Dinner     4  0.280535
       67         3.07  1.00  Female    Yes   Sat  Dinner     1  0.325733
       178        9.60  4.00  Female    Yes   Sun  Dinner     2  0.416667
       172        7.25  5.15    Male    Yes   Sun  Dinner     2  0.710345

In [42]: tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')  ＃ apply 应用
Out[42]: 
                 total_bill    tip     sex smoker   day    time  size  \
smoker day                                                              
No     Fri  94        22.75   3.25  Female     No   Fri  Dinner     2   
       Sat  212       48.33   9.00    Male     No   Sat  Dinner     4   
       Sun  156       48.17   5.00    Male     No   Sun  Dinner     6   
       Thur 142       41.19   5.00    Male     No  Thur   Lunch     5   
Yes    Fri  95        40.17   4.73    Male    Yes   Fri  Dinner     4   
       Sat  170       50.81  10.00    Male    Yes   Sat  Dinner     3   
       Sun  182       45.35   3.50    Male    Yes   Sun  Dinner     3   
       Thur 197       43.11   5.00  Female    Yes  Thur   Lunch     4   

                  tip_pct  
smoker day                 
No     Fri  94   0.142857  
       Sat  212  0.186220  
       Sun  156  0.103799  
       Thur 142  0.121389  
Yes    Fri  95   0.117750  
       Sat  170  0.196812  
       Sun  182  0.077178  
       Thur 197  0.115982


-----------------------------------------------------------------------
  
-----------------------------------------------------------------------




-----------------------------------------------------------------------
  
-----------------------------------------------------------------------




-----------------------------------------------------------------------
  
-----------------------------------------------------------------------




-----------------------------------------------------------------------
  
-----------------------------------------------------------------------




-----------------------------------------------------------------------
  
-----------------------------------------------------------------------



-----------------------------------------------------------------------
  
-----------------------------------------------------------------------



=========================7 =====================================
=========================8 =====================================
