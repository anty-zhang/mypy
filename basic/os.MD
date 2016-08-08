1.os
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径 
os.getcwdu() 获取当前工作目录，即当前python脚本工作的目录路径(返回unicode字符串)
os.chdir("dirname") 改变当前脚本工作目录；相当于shell下cd
os.curdir 返回当前目录: ('.')
os.pardir 获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2') 可生成多层递归目录
os.removedirs('dirname1') 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname') 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname') 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname') 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove() 删除一个文件
os.rename("oldname","newname") 重命名文件/目录
os.stat('path/filename') 获取文件/目录信息
os.symlink('path/filename','ln_filename') 创建符号链接，源需绝对路径
os.utime() 修改时间属性
os.tmpfile() 创建并打开‘w+b'一个新的临时文件
os.sep 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep 输出用于分割文件路径的字符串
os.name 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command") 运行shell命令，直接显示
os.popen("bash command") 运行shell命令，生成对象，可赋给变量，再用read读取
>>> import os
>>> os.system('ls twisted')
chat_client_twisted.py chat_server_twisted.py
0
 
>>> LS = os.popen('ls twisted')
>>> LS.readlines()
['chat_client_twisted.py\n', 'chat_server_twisted.py\n']

os.environ 获取系统环境变量
os.access('pathfile',os.W_OK) 检验文件权限模式，输出True，False
os.chmod('pathfile',os.W_OK) 改变文件权限模式

# echo 'test' > test.sh
>>> os.access('test.sh',os.W_OK)
True
>>> os.access('test.sh',os.X_OK)
False
>>> os.chmod('test.sh',os.X_OK)
>>> os.access('test.sh',os.X_OK)
True
# ls -l test.sh
---------x 1 root root 12 Oct 20 23:03 test.sh


os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
  top表示需要遍历的目录树的路径
  topdown的默认值是”True”,表示首先返回目录树下的文件，然后在遍历目录树的子目录.
  Topdown的值为”False”时，则表示先遍历目录树的子目录，返回子目录下的文件，最后返回根目录下的文件
      onerror的默认值是”None”,表示忽略文件遍历时产生的错误.如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历

  该函数返回一个元组，该元组有3个元素，这3个元素分别表示每次遍历的路径名，目录列表和文件列表
  os.walk()举例：
  >>> import os
  >>> for root, dirs, files in os.walk("wd/chat", topdown=False):
  ... for name in files:
  ...  print(os.path.join(root, name)) #打印文件绝对路径
  ... for name in dirs:
  ...  print(os.path.join(root, name)) #打印目录绝对路径
  ...

2.os.path常用模块详解

os.path.abspath(path) 返回path规范化的绝对路径
>>> import os.path
>>> os.path.abspath('c.py')
'/root/py/c.py'
>>> os.path.abspath('../py/c.py')
'/root/py/c.py'

os.path.split(path) 将path分割成目录和文件名二元组返回
>>> os.path.split('/root/py/c.py')
('/root/py', 'c.py')
>>> os.path.split('/root/py/')
('/root/py', '')

os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
>>> os.path.dirname('/root/py/c.py')
'/root/py'
>>> os.path.dirname('c.py')
''

os.path.basename(path) 
返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
>>> os.path.basename('/root/py/c.py')
'c.py'
>>> os.path.basename('/root/py')
'py'

os.path.commonprefix(list) 返回list中，所有path共有的最长的路径，从左向右，相同字符
>>> dl = ['/home/andy/dir1', '/home/yes/dir1', '/home/no/dir2']
>>> os.path.commonprefix(dl)
'/home/'

os.path.exists(path) 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path) 如果path是绝对路径，返回True
os.path.isfile(path) 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

os.path.normcase(path) 
在Linux下，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为反斜杠
>>> os.path.normcase('c:/windows\\system32\\')
'c:\\windows\\system32\\'

os.path.normpath(path) 规范化路径
>>> os.path.normpath('c://windows\\System32\\../Temp/')
'c:\\windows\\Temp'

os.path.splitdrive(path) 拆分驱动器名和路径，主要对win，对linux元组第一个总是空的
>>> os.path.splitdrive('c:\\windows')
('c:', '\\windows')

os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作 ，以“.”为分隔符
>>> os.path.splitext('/root/py/c.py')
('/root/py/c', '.py')

os.path.getsize(path) 返回path的大小（字节）
os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间

os.path.walk(top,func,arg)
    top表示需要遍历的目录树的路径
    
    func表示回调函数，对遍历路径进行处理.所谓回调函数，是作为某个函数的参数使用，当某个时间触发时，
    程序将调用定义好的回调函数处理某个任务.回调函数必须提供3个参数：第1个参数为walk()的参数tag，
    第2个参数表示目录列表，第3个参数表示文件列表
    arg是传递给回调参数func的元组.回调函数的一个参数必须是arg，为回调函数提供处理参数.参数arg可以为空

>>> import os
>>> def VisitDir(arg,dirname,names):
... for filespath in names:
...  print os.path.join(dirname,filespath)
...
>>> path='/root/py/wd/chat'
>>> os.path.walk(path,VisitDir,())
/root/py/wd/chat/chat_server.py
/root/py/wd/chat/chat_client.py
/root/py/wd/chat/test
/root/py/wd/chat/test/linuxeye
/root/py/wd/chat/test/test2
/root/py/wd/chat/test/test3
/root/py/wd/chat/test/test2/asdf
/root/py/wd/chat/test/test3/sdfaxx

os.path.walk()与os.walk()产生的文件名列表并不相同。os.path.walk()产生目录树下的目录路径和文件路径，
而os.walk()只产生文件路径


3.实例
3.1 返回命令name的绝对路径，比如/usr/bin/ffmpeg
def which(name):
    path = os.environ.get('PATH', os.defpath)
    for d in path.split(':'):
        fpath = os.path.join(d, name)
        if os.path.exists(fpath) and os.access(fpath, os.X_OK):
            return fpath
    return None


