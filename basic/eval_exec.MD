1.callable(): 布尔函数，确定一个对象是否可以通过函数操作符()来调用。

>>> callable(dir)
True
>>> callable(1)
False
>>> class C(object):
...     pass
...
>>> callable(C)
True
>>>


2.compile(): 在运行时刻迅速生成代码对象，然后用exec语句或者内嵌函数eval来执行这些对象或者对其求值。
compile(source, filename, mode[, flags[, dont_inherit]]) -> code object

mode:
    'eval'   可求值表达式[和eval一起使用]
    'exec'   可执行语句组[和exec一起使用]
    'single' 单一可执行语句[和exec一起使用]


>>> eval_mode = compile('100+200','','eval')
>>> eval(eval_mode)
300
>>> single_mode = compile('print "hello world"', '', 'single')
>>> single_mode
<code object <module> at 0xb7773cc8, file "", line 1>
>>> exec single_mode
hello world

>>> exec_mode = compile("""print 'exec mode1'
... print 'exec mode2'
... """, '', 'exec')
>>> exec exec_mode
exec mode1
exec mode2


>>> int('100+200')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '100+200'
>>> eval('100+200')
300


3.execfile(filename[, globals[, locals]])

execfile(filename)




