"""
练习：
通过代码获取两段内容，并且计算他们的长度的和。
"""
# a = input ("请输入：")
# b = input ("请输入：")
# print("input获取的内容：",a+b)
# print(len(a+b))

#答案

#  a = input ("请输入：")
# b = input ("请输入：")
# print("两段字符串的长度是：",len(a)+len(b))

"""
练习：
获取用户输入的出生年份，判断其生肖。
"""
# Symbolic_Animals =( '子鼠','丑牛','寅虎','卯兔','辰龙','巳蛇','午马','未羊','申猴','酉鸡','戌狗','亥猪')
# # print(len(Symbolic_Animals))
# year =int(input("请输入你完整的出生年份："))
# print(Symbolic_Animals[(year - 2008)% 12])
# # 或者知道其年龄判断属相
# Symbolic_Animals =( '子鼠','丑牛','寅虎','卯兔','辰龙','巳蛇','午马','未羊','申猴','酉鸡','戌狗','亥猪')
# Age =int(input("请输入你的年龄："))
# if Age%12 == 0:
#     print("恭喜了，今年是你的本命年！")
# else:
#     print(Symbolic_Animals[-Age%12])

# 反之，知道其属相判断其年龄   ？？？
# Symbolic_Animals =( '鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪')
# Animals =input("请输入你的属相：")
# year =int(input("请输入现在完整的年份："))
# A = Symbolic_Animals.index(Animals) # index查找某一个值的下标
# # print(Symbolic_Animals.index(Animals))
# B = str((year-2008)/12+A)
# print("你的年龄为："+B)


zodiac = {'白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座'}




"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了:Name,Age,Sex。
"""
# a ={"Name" : input("请输入你的姓名："),"Age" : input("请输入你的年龄："),"Sex" : input("请输入你的性别：")}
# print(a)

#答案

# Name = input("请输入你的姓名：")
# Age = input("请输入你的年龄：")
# Sex = input("请输入你的性别：")
# Userinfor ={}
# Userinfor.update(Name=Name,Age=Age,Sex=Sex) 
# print(Userinfor)   方法一

# Userinfor["Name"] = Name
# Userinfor["Age"] = Age
# Userinfor["Sex"] = Sex
# print(Userinfor)  方法二

"""
练习：
现在有8个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""

# c = 1
# while c < 9 :
#     a = input ("请输入学生姓名：")
#     b = int(input ("请输入该生成绩："))
#     if (b < 60) :
#        print(a,b)
#     else:
#         a = input ("请输入学生姓名：")
#         b = input ("请输入该生成绩：")
#     c = c + 1

# highchengji = {} #定义了一个空字典，用来存储大于60的信息
# lowchengji = {}  #定义了一个空字典，用来存储小于60的信息
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗"]
# a = 0  #定义了一个变量，用来控制数组下标的变化
# while a < len(studentlist) :  #为什么写个循环？因为所有的人的信息的录入，都是要用input，所以写了循环。len判断了数组的长度，总长度-1就是最大的下标
#     # print(studentlist[a])   # 为了便于自己理解下一句代码   理解为输出studentlist下标为xx的值
#     chengji = int(input("请输入"+studentlist[a]+"的成绩：")) #？？？？？录入信息，为了方便判断，所以转换了类型
#     if chengji >= 60: #判断分数
#         highchengji[studentlist[a]] = chengji #存到字典中
#     else:
#         lowchengji[studentlist[a]] = chengji
#     a = a + 1 #控制下标变化，每一次循环都 +1
# print("大于60的：",highchengji)
# print("小于60的：",lowchengji)   #方法一

"""  对  chengji = int(input("请输入"+studentlist[a]+"的成绩："))  该语句的作解
input（"请输入张三的成绩："）  学生不是固定的一个
input（"请输入"+"张三"+"的成绩："）  所以拆开来写，字符串相加拼接起来
进一步理解：
print(studentlist[a]) = 
"""

# highchengji = {} #定义了一个空字典，用来存储大于60的信息
# lowchengji = {}  #定义了一个空字典，用来存储小于60的信息
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗"]
# for i in studentlist:
#     chengji = int(input("请输入"+i+"的成绩："))
#     if chengji >= 60: #判断分数
#         highchengji[i] = chengji #存到字典中
#     else:
#         lowchengji[i] = chengji
# print("大于60的：",highchengji)
# print("小于60的：",lowchengji)      #方法二

"""
练习：
打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,"=",i*j,end="  ")  
    print() 

"""
练习：
记录生肖，根据年份来判断生肖。
"""
# Symbolic_Animals =( '鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪')
# for year in range(1990,2021):
#     print('%s年的生肖是：%s'%(year,Symbolic_Animals[(year - 2008)% 12]))
''' 一种字符串格式化的语法， 基本用法是将值插入到%s占位符的字符串中。
    %s,表示格式化一个对象为字符   %s 替换字符串  被替换的内容如何用变量替换进来：%()  括号里是替换为字符串的内容
'''
"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号不能以下划线开头。
储到字典中，{username:password}
"""

"练习一"
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True: # True 写成 1 也行
#     for i in light:  # 遍历字典中的 Key值
#         for j in range(light[i]):  # 第一次循环遍历到红灯时循环30次，绿灯时35次，黄灯时3次
#             print(i,"倒计时还有：",light[i]-j,"秒") 
#     break

"练习二"
# username = input("请注册你的账号名：")
# password = input("请输入你的密码：")
# if 5<= len(username) <= 11:
#     if username[0] not in "-":
#         if 6<= len(password) <= 12:
#             print("注册成功!请返回重新登陆验证！")
#         else:
#             print("密码必须6-12位")
#     else:
#         print("账号的不能以下划线开头！")
# else:
#     print("账号的长度不符合规范，请输入5-8位账号")

# Name = input("请输入你的姓名：")
# Age = input("请输入你的年龄：")
# try:
#     if int(Age) >= 18:
#         print(Name,"已经成年了")
#     else:
#         print(Name,"尚未成年")
# except:
#     print("请输入正确的年龄")
""" try:  

    except:
                使用场景：当我们无法判断用户输入的数据是否正确的情况下
这也是测试时为什么要输入不同的数据类型，你控制得了编码，但你控制不住用户输入的数据   
处理用户输入的数据
"""

"""
练习：
定义一个方法，用来判断用户输入的账号密码是否符合规范。
"""

# def cheakname (username,password):
#     """
#     自动判断
#     账号长度是5-11位，并且账号必须以小写字母开头
#     密码长度是6-12位
#     """
#     if len(username)>=5 and len(username)<=11:
#         if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
#             if len(password)>=6 and len(password)<=12:
#                 return True
#             else:
#                 return "密码不符合规范！"
#         else:
#             return "账号的首字母必须小写字母开头"
#     else:
#         return "账号的长度不符合规范，请输入5-11的账号"
