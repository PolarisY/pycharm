#-*-coding:UTF-8-*-    #中文编码
'''
#!/usr/bin/python
表示写死了就是要 /usr/bin/python 这个目录下 python 来执行你的脚本。
第二种写法：

#!/usr/bin/env
这种写法在你机器上安装了多个版本的python的时候有意义，这样声明的时候，会去取你机器的 PATH 中指定的第一个 python 来执行你的脚本。如果这时候你又配置了虚拟环境的话，那么这样写可以保证脚本会使用你虚拟环境中的 python 来执行。

所以这样看来，只有第二种方法才是正确的写法。


#GBK包含全部中文字符；UTF-8则包含全世界所有国家需要用到的字符。

# -*- coding: UTF-8 -*- 或者 #coding=utf-8 
'''

#!/user/bin/env python

#文件名：hello.py

#基础语法

'''
if True:
    print "Answer"
    print "True"
else:
     print "Answer"
     print "False"
'''

#raw_input("\n\npress the enter key to exit")

#import sys
# x="""runoob"""
#sys.stdout.write(x+"\n")

'''
x='a'
y='b'
#换行输出
print x
print y
print "-------------------"
#不换行输出
print x,
print y,
print x,y

'''

"""
import sys
#sys.argv 用来获取命令行参数
print sys.argv
#sys.argv[0] 代表文件本身路径，所带参数从 sys.argv[1] 开始。
"""

#变量类型

'''
a,b,c=100,100.0,"john"
print a,b,c
'''

#变量类型（字符串）

"""
str = 'Hello World!'

print str  # 输出完整字符串   Hello World
print str[0]  # 输出字符串中的第一个字符   H
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串    llo 取到的最大范围不包括上边界
print str[2:]  # 输出从第三个字符开始的字符串   llo World
print str * 2  # 输出字符串两次   Hello World!Hello World!
print str + "TEST"  # 输出连接的字符串   Hello World!TEST
"""

#变量类型（列表list）

'''
list=['runoob',786,2.23,'john',70.2 ]
tinylist=[123,'john']

print list                         #['runoob', 786, 2.23, 'john', 70.2]# 输出完整列表
print list[0]  #runoob             # 输出列表的第一个元素
print list[1:3]  #[786, 2.23]      # 输出第二个至第三个元素
print  list[2:]  #[2.23, 'john', 70.2]                # 输出从第三个开始至列表末尾的所有元素
print tinylist *2   #[123, 'john', 123, 'john']       # 输出列表两次
print list + tinylist #['runoob', 786, 2.23, 'john', 70.2, 123, 'john']# 打印组合的列表
'''

#变量类型（元组tuple）

"""
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
"""

'''
tuple=('runoob',786,2.23,'john',70.2)
tinytuple=(123,'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple *2        # 输出元组两次
print tuple + tinytuple   # 打印组合的元组
'''

#变量类型（字典）

"""
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""

'''
dict = {}
dict['one']="This is one"
dict[2]="This is two"

tinydict = {'name':'john','code':6734,'dept':'sale'}

print dict['one']                # 输出键为'one' 的值
print dict[2]                     #  输出键为 2 的值
print  tinydict                   # 输出完整的字典
print  tinydict.keys()            # 输出所有键
print tinydict.values()           # 输出所有值
'''

#python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型:
'''
n=1
print type(n)
'''

#此外还可以用 isinstance 来判断：
'''
a=111
print isinstance(a,int)
'''

# type()不会认为子类是一种父类类型。
 #isinstance()会认为子类是一种父类类型















































