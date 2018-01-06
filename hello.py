#-*-coding:UTF-8-*-
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

import sys
#sys.argv 用来获取命令行参数
print sys.argv
#sys.argv[0] 代表文件本身路径，所带参数从 sys.argv[1] 开始。





