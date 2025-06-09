""" 第一天Python的学习 """

# print:打印  可以打印很多种类型数据，逗号隔开就可以
# print('"Hello,world!"')  #  字符串需 "  " 或 ' ' 无论用单引号或双引号，但要成对出现 括起来   还可以 '''  ''' 可以跨行写
# print(2333) #整数
# print(2.333) #小数
# print(True) #布尔值 用于判断里面 一些语言中还用非0表示真，0表示假
# print(()) #元组
# print([]) #数组
# print({}) #字典
#Python的注释分 单行注释： #注释内容  多行注释："""  注释内容  """
#print("Hello,world!",2333,True)

'''
 变量的命名
·变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
· 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
· 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
· 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
· 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
'''
# 字符串的拼接（合并），但是只能相同数据类型操作  不能用减号的 可以用乘号
# first_name = "ada"
# last_name ="lovelace"
# full_name = f"{first_name}{last_name}"  # f-string 格式化字符串的方式，在字符串前加上f，然后在字符串中使用花括号{}来引用变量。
# print(f"hallo, {full_name.title()}!") # f"Hello, {name}!" 会将变量name的值插入到字符串中的花括号中。
# full_name = first_name+" "+last_name   # "",引号之间有个空格
# print("hallo, "+full_name.title()+"!") # .title()将字符串每个单词的首字母改大写  .upper()全部大写 ：.lower()全部小写    hallo，后面有个空格

# a = input ("请输入：")
# b = input ("请输入：")
# print("input获取的内容：",a+b) # 数据类型，形成了字符串的拼接 
# input的特点：不管你输入什么东西，只要是通过input获取的，对于我们代码来说都是字符串


##Python的运算符：
# + - * /  加减乘除    ** 幂运算  2**3  2的三次方  // 取整  2//3  0   % 取余  2%3  2
# ==  等于 != 不等于
# > 大于 < 小于 >= 大于等于 <= 小于等于
# and 与  两个条件同时满足 or 或  两个条件满足一个即可
# not 非  取反
# 优先级：
# 幂运算 > 乘除 > 加减 > 比较运算符 > 逻辑运算符
# 括号可以改变优先级
# and 与  两个条件同时满足 or 或  两个条件满足一个即可

# print(((1+2)*3-4)/5) 
# print(2>3)   
# print(2<3)
#变量和赋值
# Xx = "张三" # 把张三这个值赋值给了名字叫xx的这个变量   变量一定要用小写还是最好用小写？
# print(Xx)

#判断数据类型 Type
# a = type(2333)
# print(a) #读取了数据判断其类型为整数（int）  运行结果为：<class 'int'>
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

#数据类型的转换
# a = int("2333")
# print(type(a))  #字符串转换为整数
# a = str(True)
# print(type(a))  #布尔值转换为字符串
# print(bool(1)) #整数转换为布尔值
# print(type(bool(1))) #判断其数据类型
# print(bool(0))
"""
数据类型转换的规律：
1任何数据都可以转换为字符串；除了 空/None 不能转
2整数和小数可以互相转换；
3字符串转换为其他类型的数据，必须满足【长得像】这个规律  （口水话，但有用）。长得像：如：2333、2.333 
"""

# a = int (input("请输入："))
# b = int (input("请输入："))
# print(a+b) #整数的相加
# a = float (input("请输入："))
# b = float (input("请输入："))
# print("input获取的内容是：",a+b) #支持小数的相加

# a = "哈哈哈哈"
# print(len(a))  # len是用于获取“字符串”的长度的
# 注意与下面的区分？所输出的长度不同

""" 第二天Python的学习 """

#  元组，下标，正向从0开始编号，反向-1开始
# a = (1,2,3,4,"好好","学习","Python",True,False,"Python","Python")
# print(len(a)) 
# print(a[-6])     # 下标
# a.index("Python") # index查找某一个值的下标是多少
# index count ，他们只能在一维元组中使用
# print(a.index("Python")) #当有很多个重复的值的时候，它搜索这个值的下标是第一个值的下标，就近原则
# print(a.count("Python")) # count统计某个值的数量
# print("Python" in a) # in 指在  not in 不在
# print(1 not in a)  #指定的对象判断在不在成员当中，即：成员关系操作符  对象[not]in序列
# print("\t我要好好学Python\n"*10) #字符串的重复操作： "字符串"*整数
''' 空格与（制表符\t），通俗点说这两个东西的内部表示方法和显示出来的都不一样，编程的时候，空格用" "表示，制表符用"\t"表示
    显示的时候空格就是一个空格 制表符一般显示为四个空格，换行符：\n
'''
# name= input("Please input your name: ") #字符串的替换功能 %s 替换字符串  %d十进制整数
# print("Hello, %s good morning!" %name)  #一种字符串格式化的语法， 基本用法是将值插入到 %s占位符的字符串中。%s,表示格式化一个对象为字符 
# name= str(input("Please input your name: "))
# print("Hello, "+name+" good morning!" )   #同上
#二维元组
# b =(a,"好好学习","天天向上") # b 里面有几个值？  3
# print(b[0][6])
#切片[0:整数]
# print(a[0:4]) # 左闭右开
# print(a[:4]) #效果同上   不写 0 ，意思从同开始
# print(a[4:6])#取第4个和第5个
# print(len(a))  # len是用于获取“字符串”的长度的
# print(a[6:]) #不写 最后 ，意思从 6 开始到最后
# print(a[6:12])# 效果同上
# print(a[:]) # 全部

#列表 （Python里叫列表/list（同数组一样））  与元组区别：元组一旦写好过后不可以修改，而列表是可以修改的
#列表 list  同样也有成员关系操作符，拼接（连接）操作符，重复操作符和切片操作符  等功能
# a =[1,2,3,4,"好好","学习","Python",True,False,"Python","Python"]
# print(a[-6]) 
# a.append("append1") 
# a.append("append2") #往列表尾端增加（追加）一个数据
# b =["呵呵","嘿嘿"]
# print((a + b)*2)  #拼接和重复
# b = a.remove("Python") #移除（删除）某个值（就近）
# print(b)
# b = a.remove(0)  # 注意：True = 1,False = 0
# print(a)  
# a.insert(4,"inster")  #往数组中指定的位置插入数据
# print(a)
# a.pop(0)
# print(a)
# b = a.pop(0)# 类似于剪切，把数组里某一个值从中拿出来用到别处去
# print(b)
# print(a)
# c = a.pop(0)#剪切数据a，赋值给c用
# print(b+c)
# print(a)
# a.clear() #清空数组
# print(a)
# xx =["Hello,Python","Hello,World"]
# a.extend(xx) #把一个数组里面的多个值加到另一个数组的数据中去，即：合并数组
# print(a)  


# xx = [0,False,1,True]
# c = xx.count(1) #统计某个值得数量
# print(c)
#下标不要超出范围  否则为 越界
   
"""
Python的语法
所有的方法都是小括号结尾的。比如，print(),input(),len(),... 
元组、数组、字典的取值，都是用中括号，比如 a[0]
元组、数组、字典的定义，分别是(),[],{}
"""  

"""
字典的特点(记录对应关系)
1、字典中的值没有顺序。  字典把数组里的下标自定义了
2、字典的结构必须是 键值对的结构。 key:value(值) {"哈希值":"对象"}
3、字典的取值，是通过Key去取这个value
          任何地方的字符串都要加引号
"""
#映射的类型：字典   包含哈希值和指向的对象，如 ：{"哈希值":"对象"}
# a = {"name":"张三",
#      0:"哈哈",
#      "age":25
#      }
# print(type(a),a)
# print (a["name"])  #取值
# a["high"] = "183cm" #新增
# print(a)
# a["name"] = "李四" #修改
# print(a)

# b = a.get("name") #取值
# print(b)
# b = a.pop("name") #剪切
# print(b)
# print(a)
# a.update(name=1111) #更新与修改类似  name为啥没加引号？  name为变量，赋值给name一个值
# print(a)
# print(a.get("name"))
# print(a["name"])
# print("---------------")
# #假如写了不存在的 Key  区别就如下：
# print(a.get("name1")) #会回馈为 空/None
# print(a["name1"]) # 代码报错           两者虽都为取值，这就是不同点

#数组和字典的删除
# del a["name"]
# print(a)

""" 第三天Python的学习 """

#判断  Tab缩进       == 判断是否相等   = 是赋值

# print("比大小")
# a = float(input("请输入："))
# b = float(input("请输入："))
# if a > b:  # 条件过后不要忘记冒号 ：
#     print(a) #前面缩进为四个空格，代表和if是一个代码块
# else:
#     print(b)

# age = int(input("请输入你的年龄："))
# if age > 60:               # 60是整数（int），所以age得是整数才行，记得数据类型转换和对应
#     print("你应该退休了")
# elif age >30:
#     print("家庭责任重大")
# elif age >20:
#     print("你需要好好思考你想要的生活是什么？") 
# else:
#     print("好好学习天天向上") 

""" 
Python的判断条件 
三种类型：1、if  表达式： 2、if 表达式：  3、if 表达式：
                代码块         代码块         代码块 
                           else：         elif 表达式： #（else-if）
                               代码块          代码块 
                                          (可以多个 elif...)
                                          else：
                                              代码块           
"""
# age = int(input("请输入你的年龄："))
# # print(type(age))
# if age == "":
#     print("不能为空！！！")
#     exit()
# if age > 20 and age <30:
#     print("你该成家立业了！")
# elif age >30 and age <=50:
#     print("家庭责任重大") 
# else:
#     print("保证生命成长")  

# a = "你好"
# if a in "你好吗？":    #in  表示：a 的内容存在 in 后  in后可以是字符串也可以是数组、字典等内容
#     print("我很好")
# else:
#     print("I'm Sorry")
''' 测试时记得特殊值，比如 空 '''
# a = input("请输入：")
# if type(a) is int :   # is用来数据判断类型的
#     print("是整数")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他") 

"""
while循环语句
while 表达式：
    代码块
"""                 
# a = 1
# while a < 10:
#     print("Hello,Python",a)
#     break # 终止循环或跳出循环（只针对本层循环，嵌套循环不能终止全部）
#     a = a + 1

# for 循环 原理： 遍历实现 

# a = "你好，今天你吃了吗？"
# print(len(a)) 
                 #两者输出len的值不同
# a = "张三","李四","王麻子","浪晋","流云","希希","小梁","二狗"
# print(len(a))
# for i in a:   # 遍历，每一个都打印一遍  i是一个变量名
#     print(i)

# range()数列生成器    左闭右开   只写一个值，默认从0开始依次
# b = list(range(100)) #自动生成了一个数列  左闭右开   只写一个值，默认从0开始依次
# b = list(range(0,100,2)) # 步进/步长  默认从0开始按步进依次
# print(b)

# for i in range(100):
#     print(i)

# 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="  ")  # end 控制不换行
#     print() # 空的print 起了换行的作用

# 从1到10 所有偶数的平方
# alist = []
# for i in range(1,11):
#     if(i%2==0):
#         alist.append(i*i)
# print(alist)
# #python 独有的 列表（数组）推导式 或字典推导式
# blist = [i*i for i in range(1,11) if(i%2)==0]
# print(blist)
# for i in range(10):
#     if i ==3:
#         continue   # 遇到 continue 结束后面代码运行 （跳过当前本次循环不输出）重新开始下一个的循环
#     print(i)

""" 第四天Python的学习 """

# def playfootball(members):
#     """
#     踢足球
#     """
#     print(members)
#     print("拿起足球")
#     print("来到球场上")
#     print("分成两队")
#     print("设法把球踢进对方球门")
# playfootball("张三、李四、王二、麻子。。。。") 

# 函数(function)/方法   
# def 方法的声明/定义函数 关键字  
# sum 方法的名字/函数的名字
# a,b 方法的参数(可以没有)
#定义参数（形参）时的命名规则和变量一样，可以是一个或多个（逗号隔开），调用函数时，传入对应个数的参数（实参）
# """方法的说明"""
# 方法的逻辑代码    
# def sum(a,b):  #不要忘记冒号
#     """
#     这个方法的作用时两数相加      # 此注释是方法的说明
#     """
#     if type(a) is int and type(b) is int:
#         return a+b 
#     else:
#         return "输入的数据类型不正确！"  # if... else...是方法的逻辑代码

"""
返回值/return ，返回后我们可以对这个值做其他的操作
而，print 不能
"""
# sum(24,56)  # 方法使用/调用函数

# a = sum(24,56)
# print(a+2)    



# 异常捕获
# try:
#     print(sum("5",8)+6)
# except Exception as e:
#     print("上面的参数有错误",e)

# 异常类/Exception  
# 代码的单位：包->模块->类->方法->变量   使用的时候是并列关系
"""包的使用：import 包   直接导入自带的某个包  写在程序最上方
第三方包的使用：（pip 是管理第三方包的工具） 先下载安装 pip install 包名  / 卸载 pip uninstall 包名
查找你安装的第三方包有哪些：pip list  
"""
# import time  #导入python 时间包
# for i in range(10):
#     time.sleep(1)  #停顿一秒的运行
#     print(i)
# import random # random 生成随机数
# a = random.randint(0,100)
# print(a)

""" 第五天Python的学习 """

"""
class 声明类的名字  class Test(): 括号里填写参数，即类的继承/重写（多写）
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
默认属性方法 _init_ (也可以没有属性)
"""
# 类的实例化

# Python文件的读写

