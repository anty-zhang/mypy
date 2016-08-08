该模块是专门用来处理命令行参数的


函数getopt(args, shortopts, longopts = [])

参数args一般是sys.argv[1:]
shortopts  短格式 (-) 

longopts 长格式(--) 

命令行中输入：
python test.py -i 127.0.0.1 -p 80 55 66

python test.py --ip=127.0.0.1 --port=80 55 66


下面的代码：

try:
options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
except getopt.GetoptError:
sys.exit()

for name,value in options:
if name in ("-h","--help"):
usage()
if name in ("-i","--ip"):
print 'ip is----',value
if name in ("-p","--port")

print 'port is----',value


options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])



“hp:i:”
短格式 --- h 后面没有冒号：表示后面不带参数，p：和 i：后面有冒号表示后面需要参数

["help","ip=","port="]

长格式 --- help后面没有等号=，表示后面不带参数，其他三个有=，表示后面需要参数

返回值 options 是个包含元祖的列表，每个元祖是分析出来的格式信息，比如 [('-i','127.0.0.1'),('-p','80')] ;
 args 是个列表，包含那些没有‘-’或‘--’的参数，比如：['55','66']

注意：定义命令行参数时，要先定义带'-'选项的参数，再定义没有‘-’的参数
