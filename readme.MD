一.<利用Python进行数据分析>
http://oreilly.com.cn/
http://www.youtube.com/oreillymedia

http://githup.com/pydata/pydata-book

http://download.csdn.net/detail/olaking/8379721

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ipython 说明
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#############################################################
# ipython特性
#############################################################

(1)人性化格式化
(2)自动补全
(3)用?内省
??显示源代码
np.*load*? : 显示numpy顶级命名空间中含有load的函数
%run python_script.py sys.args[0]

#############################################################
# ipython 魔术命令
#############################################################
%quickref   显示IPython的快速参考
%magic      显示魔术命令的详细文档
%timeit     检测python语句的执行时间
%paste
%cpaste
%xmode
%hist       打印全部输入历史
%reset      清空interactive命名空间
%logstart   记录整个会话，包括输入和输出

#############################################################
# 从新加载模块依赖项
#############################################################
reload(moudle)  非递归
dreload(moudle) 递归

#############################################################
# ipython 和matplotlib 集成
#############################################################
ipython --pylab

#############################################################
# 输入和输出变量
#############################################################
结果未赋值给变量时
    _   保存最近的输出变量
    __  保存第二个输出变量

_iX     保存输入变量，X为行号
_X      保存输出变量，X为行号

#############################################################
# IPython 调试命令
#############################################################
  h(elp)
  help command
  c(ontinue)
  q(uit)
  b(reak) number
  b path/file.py:number
  s(tep)	单不进入函数调用
  n(ext)
  u(p)/d(own)	在函数栈中向上或者向下移动
  a(rgs)	显示当前函数参数
  debug statement	在新的调试器中调用statement
  l(ist) statement	
  w(here)
  

//api.py
def set_trace(): 		# 插入到代码中的任意位置
  from IPython.core.debugger import Pdb
  Pdb(color_scheme='linux').set_trace(sys._getframe().f_back)
  
def debug(f, *args, **kwargs):
  from IPython.core.debugger import Pdb
  pdb = Pdb(color_scheme='linux')
  return pdb.runcall(f, *args, **kwargs)

  
/home/andy/test/some.py
def f(x, y, z=1):
  tmp = x + y
  return tmp/z
      
%run -d -b10 test_debug.py

from api import debug
from api import set_trace
from test import f
>>>debug(f,1,2,3)
ipdb> n
> /home/andy/test/some.py(9)f()
      7 def f(x, y, z=1):
      8     tmp = x + y
----> 9     return tmp/z

ipdb> 
--Return--
1
> /home/andy/test/some.py(9)f()
      7 def f(x, y, z=1):
      8     tmp = x + y
----> 9     return tmp/z
ipdb> 
Out[10]: 1


#############################################################
# %time %timeit 测试代码的执行时间
#############################################################

%time ： 一次执行一条语句，时间是执行一次的时间
%timeit ： 执行多次的平均时间

例如：
In [22]: s = ['foo','zh','foobar','baz','qux','python','Guido Van Rossum'] * 
100000

In [23]: %timeit method1 = [x for x in s if x.startswith('foo')]
1 loops, best of 3: 295 ms per loop

In [24]: %timeit method2 = [x for x in s if x[0:3] == 'foo']
10 loops, best of 3: 136 ms per loop







