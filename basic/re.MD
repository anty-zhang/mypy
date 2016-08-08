1. r'simple string'(原始字符串):在普通字符串前加r实现

2.使用正则表达式进行查找
（1）re.match查找
match()方法的工作方式是只有当被搜索字符串的开头匹配模式的时候它才能查找到匹配对象。
>>> re.match(r'dog', 'dog cat dog')
<_sre.SRE_Match object at 0xb743e720<
>>> match = re.match(r'dog', 'dog cat dog')
>>> match.group(0)
'dog'


但是，如果我们对同一个字符串调用math()方法，查找模式‘cat’，则不会找到匹配。
>>> re.match(r'cat', 'dog cat dog')
>>>

（2）search()方法和match()类似，不过search()方法不会限制我们只从字符串的开头查找匹配
因此在我们的示例字符串中查找‘cat’会查找到一个匹配：

search(r'cat', 'dog cat dog')
>>> match.group(0)
'cat'

然而search()方法会在它查找到一个匹配项之后停止继续查找
因此在我们的示例字符串中用searc()方法查找‘dog’只找到其首次出现的位置。

>>> match = re.search(r'dog', 'dog cat dog')
>>> match.group(0)
'dog'

（3）re.findall()
当我们调用findall()方法，我们可以非常简单的得到一个所有匹配模式的列表，而不是得到match的对象（我们会在接下来更多的讨论match对象）。
对我而言这更加简单。对示例字符串调用findall()方法我们得到：
['dog', 'dog']
>>> re.findall(r'cat', 'dog cat dog')
['cat']


3.其他方法
（1）match.start 和 match.end
（2）使用 mathch.group 通过数字分组

就像我之前提到的，匹配对象在处理分组时非常得心应手。
分组是对整个正则表达式的特定子串进行定位的能力
我们可以定义一个分组做为整个正则表达式的一部分，然后单独的对这部分对应匹配到的内容定位。
让我们来看一下它是怎么工作的：

>>> contactInfo = 'Doe, John: 555-1212'
我刚才创建的字符串类似一个从某人的地址本里取出来的一个片段。
我们可以通过这样一个正则表达式来匹配这一行：

>>> re.search(r'\w+, \w+: \S+', contactInfo)
<_sre.SRE_Match object at 0xb74e1ad8<

通过用圆括号来（字符‘(’和‘)’）包围正则表达式的特定部分，
我们可以对内容进行分组然后对这些子组做单独处理。

>>> match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)

这些分组可以通过用分组对象的group()方法得到。
它们可以通过其在正则表达式中从左到右出现的数字顺序来定位（从1开始）：

>>> match.group(1)
'Doe'
>>> match.group(2)
'John'
>>> match.group(3)
'555-1212'

组的序数从1开始的原因是因为第0个组被预留来存放所有匹配对象
（我们在之前学习match()方法和search()方法到时候看到过）。

>>> match.group(0)
'Doe, John: 555-1212'

（3）使用match.group 通过别名来分组
有时候，特别是当一个正则表达式有很多分组的时候，通过组的出现次序来定位就会变的不现实。
Python还允许你通过下面的语句来指定一个组名：
>>> match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
>>> match.group('last')
'Doe'
>>> match.group('first')
'John'
>>> match.group('phone')
'555-1212'

尽管findall()方法不返回分组对象，它也可以使用分组。类似的，findall()方法将返回一个元组的集合，
其中每个元组中的第N个元素对应了正则表达式中的第N个分组。

>>> re.findall(r'(\w+), (\w+): (\S+)', contactInfo)
[('Doe', 'John', '555-1212')]



