#查看关键字的方法
import keyword #引入关键字模块
#打印系统内全部关键字
print(keyword.kwlist)

#变量
#声明的三种格式

#格式1
s = "我爱余思敏"

#格式2
s2 = s1 = "我爱余思大头"

#格式3
s1,s2,s3 = "我爱余思敏","I love yudatou","这是我的python第一节课"


'''
变量类型：严格意义来讲，python只有一种类型
标准数据类型一共六种
'''

#    -数字 Nmuber
#    -字符串类型 str
#    -列表 list
#    -元组 tuple
#    -字典 dict
#    -集合 set


'''
number 数字类型
'''
#python中的数字没有大小限制

'''
常见数字分类
'''

'''
整数  （没有小数部分，包含正数、负数和0。）
        二进制
        -只有0，1
        -以0b开头的01串
        -例如：
            -0b110
            -0b11110

        八进制
        -以0o开头的，0-7之间的数字
        -例如：
            -0o71

        十六进制
        -以0x组成的由0-9，a-f构成的串

'''

#二进制定义
a = 0b10010
print(a)
#八进制定义
a1= 0o1572
print(a1)
#十六进制定义
a2 = 0x17ace
print(a2)


'''
浮点数
    -就是通俗意义上的小数 
    -常见的案例格式
        -3.14159
        -3.
        -0.4
        -.4    
'''

'''  
    -科学记数法
        -定义和数学定义一致
        -写法就是e后买你跟整数用来表示10的指数，e2 表示10的2次方

'''
heigh = 184
print(heigh)
heigh = 1.84e2
print(heigh)
a = .2
print(a)

'''
复数 complex
    -与数学定义一样
    -复数的虚部用j/J表示
    -例如：
        -5+4j
        -4j
        -(4j)
'''
a= 4j
print(a)

'''
布尔值
    -布尔值就是用来表示真假的值
    -只有两个值：True/False
    -在python中，布尔值可以当数字使用
        -布尔值如果当数字使用，True=1，False=0
        -如果数字用来当作布尔值使用，0=False，其余当作True
'''
age=18+True
print(age)
age=18+False
print(age)
#判断语句
a = -1
if a:
    print("负数是True")
else:
    print("负数是False")

'''
字符串
    -表达文字信息的内容，比如：“我爱大头”
    -形式上是引号引起来的一段内容
    -引号包括
        -单引号
        -双引号
        -三引号，可以用来表示多行信息
    -单引号和双引号意思一致
'''
#字符串案例
love="Ich liebe Wang Xiao Jing"
print(love)
love2 = 'I love Wang Xiao Jing'
print(love2)
#三引号可以表示多行
love3 = '''
你好，你叫
大头余
就是一个
大大的猪头
'''
print(love3)

'''
None类型
    -表示什么都没有，通常用来占位
    -比如返回，用来表示返回一个空d
'''


'''
表达式
    -由一个或者几个数字或者变量或者运算符合成第一行代码
    -通常返回一个结果

运算符
    -由一个以上的值经过一系列的运算得到新值的过程就叫做运算
    -用来操作运算的符号叫做运算符
    -运算符分类
        -算数运算符
        -比较或关系运算符
        -赋值运算符
        -逻辑运算符
        -位运算
        -成员运算符
        -身份运算符
            算术运算符
                -用来进行算术运算的符号
                -通常用来表现加减乘除
                -python没用自增自减运算符
            比较运算符
                -对两个内容进行比较的运算符
                -结果一定是一个布尔值，即True/False
            赋值运算符
                -把一个值放到变量里边去，符号为=，运算优先级为最低
            逻辑运算符
                -对布尔变量或者值进行运算的符号
                -and：逻辑与
                -or ：逻辑或
                -not：逻辑非
                -python里面的逻辑运算没用异或
                -运算规则：
                    and看作乘法，or看作加法
                    True看作1，False看作0
                    则逻辑运算就能转换成整数数学运算
                    最后结果如果是0则为False，否则为True
            成员运算符
                -用来检测一个值或者变量是否在某个集合里面
                -in：成员运算符
                -not in：不在里边的意思
            身份运算符
                -用来确定两个变量是否是同一变量
                
'''
#表达式案例
a = 1+2
print(a)
#算术运算符案例
a = 9 - 2
print(a)
b = 9 + 2
print(b)
c = 8 * 2
print(c)
#python除法分为普通除法、地板除、取余
a = 9 / 2 #正常除法，此操作在python2.x和3.x中有些不同
print(a)
a = 9 // 2 #地板除,取整除
print(a)
a = 9 % 2 #取余
print(a)
a = 9 % -4
print(a)
#不等于，!=
#逻辑表达举例
a = True
b = True
c = False
aa = a and b
bb = a and c
print(bb)

'''
程序结构
    -程序三种结构
        -顺序
        -循环
            -重复的执行某一个固定的任务或动作
            -分类
                -for
                    -语法
                        for 变量 in 序列 ：
                            语句1
                            语句2
                            ...
                -break、continue、pass
                    -break：无条件结束整个循环，简称循环猝死
                        num_list=[1,2,3,4,5,6,7]
                        fo num in num_list :
                            if num == 7 :
                                print("找到了")
                                break   
                            else ：
                                print(num)
                    -continue：继续
                        在数字1-10中，寻找所有偶数，找到偶数后进行打印
                            dig_list=[1,2,3,4,5,6,7,8,9,10]
                            for dif in dig_list :
                                if dig % 2 == 0
                                    print(dig)
                                    print("这是双数")
                                else ： 
                                    continue
                    -pass：只是个占位符,代表这句话什么也不干，没有跳过的功能
                        案例1：
                        age = 19
                        if age >= 18 :
                            pass
                        else :
                            print('你还小')
                        
                        案例2：
                        ages = [22,23,24,26,27,30]
                        for age in sges :
                            pass
                            print(age) 
                    -range函数：
                        -生成有序数列
                        -生成数字队列可以定制
                -while
                    一个循环语句
                    表示当条件成立的时候，就循环，适应用于不知道具体循环次数，但能确定某个条件只要成立就去循环
                    while语法：
                        while 条件表达式：
                            语句块
                         else：
                            语句块 
        -分支
            分支结构
                -分支结构的基本语法
                    if 条件表达式：
                        语句1
                        语句2
                        语句3
                        ......
                -条件表达式就是运算结果必须为布尔值的表达式
                 -表达式后面的冒号不能少
                 -注意if后面出现的语句，如果属于if语句块，则必须同缩进一个等级
                 -条件表达式结果为True则执行if后面的语句块
                双向分支
                    -if ....else....表达
                    -语法结构：
                        if 条件表达式：
                            语句1
                            语句2
                            ......
                        else:
                            语句1
                            语句2
                            ......
                多路分支
                    -语法结构：
                        -if 条件表达式：
                            语句1
                            .....
                        elif 条件表达式：
                            语句1
                            ....
                        else：
                            语句1
                            ......
                    -elif可以有好多个，根据实际情况
                    -else可选
                    -多路分支最多只会执行一种情况
'''
#age = input("请输入你的性别：") #input负责接受用户输入并把内容返回给变量20
#print(age)
#if age=='Man' :
#    print("今天是个好日子")
#else:
#    print("今天是个倒霉的日子")

#achievement = input("请输入您的成绩：")
#if achievement> '90':   #input输入的值全部都是字符串类型
#    print('优秀')
#elif achievement >= '80' :
#    print('良好')
#else :
#    print('一般')


#如果说年利率是6.7%，本利是每年翻滚，多少年后本钱会翻倍
benqian = 10000;
year = 0
while benqian < 20000 :
    benqian = benqian*(1+0.067)
    year = year + 1
print(year)

'''
函数
    -函数是代码的一种组织形式
    -函数应该能完成一项特定的工作，而且一般一个函数值完成一项工作
    -有些语言，分函数和过程两个概念，通俗解释是，又返回结果的叫函数，无返回结果的叫过程，python不加以区分
    -函数的使用
        -函数使用需要先定义
        -使用函数，俗称调用
        -函数的调用，直接写出函数名字，后面的小括号不能省略，括号内内容根据实际情况而定
    -函数的参数和返回值
        -参数：负责给函数传递一些必要的数据或信息
            -形参（形式参数）：在函数定义的时候用到的参数，没有具体值，只是一个占位符号
            -实参（实际参数）：在调用函数的时候输入的值
        -返回值：调用函数的时候的一个执行结果
            -使用return返回结果
            -如果没有值需要返回，推荐使用return None表示函数结束
            -如果函数没有return关键字，则函数默认返回值为None
参数
    -参数分类
        -普通参数/位置参数
        -默认参数
            案例
                -def a(one,two,therr=100)
                    print(one+two)
                    print(three)
                    return None
                a(1,2)
                a(1,2,3)
        -关键字参数
        
        -收集参数 
'''
def func() :
    print("这是一个函数")
    print("我是被调用的")
func()

def hello(person): #参数person只是一个符号，真正调用的时候调用的是另外一个
    print("{0},你好么".format(person))
    print("{},你看见我家小静了么".format(person))
p = "小明"
e= "小五"
#调用函数，需要把P作为实参传入
hello(p)
hello(e)
pp = hello("大头")
print(pp)
help(print)

#九九乘法表
for i in range(1,10) : #控制外循环，从1到9
    for j in range(1,i+1) : #内循环，每次从第一个数字开始，打印到和行数相同的数量
        print(i*j,end=" ") #end表示换行
    print()

#函数打印九九乘法表
def jiujiu():
    for i in range(1, 10):  # 控制外循环，从1到9
        for j in range(1, i + 1):  # 内循环，每次从第一个数字开始，打印到和行数相同的数量
            print(i * j, end=" ")  # end表示换行
        print()
    return None
jiujiu()
jiujiu()
#嵌套函数
def printLine(line_num): #参数代表行号
    for i in range(1,line_num+1) :
        print(line_num*i,end=" ")
    print()
def jiujiu1() :
    for j in range(1,10) :
        printLine(j)
jiujiu1()



'''
字符串
    -表示文字信息
    -用单引号、双引号、三引号括起来
'''

'''
转义字符
    -用一个特色的方法表示出一系列不方便写出的内容，必须换行符，回车键，退格符
    -借助反斜杠字符，一旦字符串中出现了反斜杠，则反斜杠后面的字符表示已经进行了转义
    -使用字符串中，一旦出现反斜杠就要加倍小心，可能有转义字符出现
    -不同操作系统对换行操作有不同的表示
        -Windows \n
        -Linux \r\n
'''

#   -常用的转义字符
#        \\ 反斜杠字符
#        \' 单引号
#        \" 双引号
#        \a 响铃
#        \b 退格（Backspace）
#
#        \000 空
#        \n 换行
#        \v 纵向制表符
#        \t 横向制表符
#        \r 回车
#        \f 换页
#        \oyy 八进制数.yy代表字符，例如:\o12代表换行
#        \xyy 十六进制数，yy代表的字符，例如\x0a代表换行
#       \other 其它的字符以普通格式输出    


#转义字符案例，表达Let's Go
s = 'Let\'s Go' #使用转义字符
print(s)

s = "Let's Go" #使用单双引号嵌套
print(s)

#表示斜杠，比如：C:\User\Name
s = 'c:\\User\\Name'
print(s)

#回车换行
s = "你好：\n这里是大头余 \n我是小胖子"
print(s)

#单个反斜杠的用法，需要美观换行，但是显示不换行
def myDemo(x,\
           y,\
           z):
    print('hahhahah')
print(myDemo)

'''
字符串的传统格式化方式
    -使用%进行格式化
    -%（百分号）也叫占位符
        %s :字符串
        %r ：字符串，但是是使用repr而不是str
        %c ：整数转换为单个字符
        %d ：十进制整数
        %u ：无符号整数
        %o ：表示八进制
        %x ：表示十六进制，字母为小写（x为小写）
        %X ：十六进制，字母为大写（X为大写）        
        %f : 十进制浮点数
'''
# %s表示简单的字符串
s = "I love %s"
print(s%"俞大头")
print("I Love %s"%"大头余")

#有两个需要替换的
s = "I am %fKG,whight,%fM,Heigh"  #默认格式，打出多余的0
print(s%(71.4,1.765))

s = "I am %.2fKG,whight,%.2fM,Heigh"  #对占位符进行控制，.2表示只打印小数点后两位
print(s%(71.4,1.765))

'''
format格式化
    -使用函数形式进行格式化，代替以前的百分号
'''
#不用自会顶位置，按顺序读取
s = "{} {}!"
print(s.format('Hello','World')) #方式1

s = "{} {}!".format("Hello","World")
print(s)

s = "{1} {1}!".format("Hello","World") #设定指定位置
print(s)

#使用命名参数
s = "大头是{sex_name}，大头最爱{man_name}，{name}最帅"
s = s.format(sex_name = "猪头",man_name = "常浩宇",name = "常浩宇")
print(s)
#通过字典设置参数，需要解包
s = "大头是{sex_name}，大头最爱{man_name}，{name}最帅"
s_dict= {"sex_name":"猪头",\
         "man_name":"常浩宇",\
         "name":"常浩宇"}
s = s.format(**s_dict) #**代表解包操作
print(s)
#对数字的格式化需要用到
s = "Chang HaoYu is {} M, {}KG wgight"
print(s.format(1.76,71.5))

'''
str内置函数
    -很多语言字符串使用string表示，但是python中用str来表示
'''


'''
str内置函数
    -字符串查找类，find，index，islower
        -find：查找字符串中是否包含一个子串
        -index:跟find的唯一区别是index如果找不到会引发异常
        -rfind\lfind :从左边开始或者从右边开始查找
    -判断类函数
        -此类函数的特点一般是用is开头，比如islower
        -isalpha:判断是否是字母，需要注意两点
            -此类函数默认的是前提是字符串必须至少包含一个字母，如果没有则返回false
            -汉字被认为是alpha，所以函数不能区分英文字母还是汉字的标识，区分中英文使用unicode码    
    -内容判断类
        -startswith/endswich：是否以xxx开头或者结尾
            -检测某个字符串是否以某个字串开头，常用三个参数
                -suffix：被检查的字符串，必须要有
                -start：检查范围的开始范围
                -end：检查范围的结束范围
        islower/isupper：判断字符串是否是大写或者是小写
    -操作类函数
        -format：格式化用的
        -strip：默认删除空格，主要删除字符串两边的空格，也可以删除指定的两边的哪个字符    
'''

#help(str.find)
k = "Yu Da Tou shi PigZhutou yusimin"
k1 = "Pig" #返回第一次发现这个字符串的位置
k2 = "yusimin"
k.find(k1)
k.find(k2)
#使用的时候还可以使用区间
z = "Yu Da Tou shi PigZhutou yusimin"
z1 = "PigZhutou"
s.find(z1,25)
help(str.rfind)

s1 = "余大头是猪头"
s2 = "DAtou shi zhu "
s3 = "woshizhitou"
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())

datou = "Yu datou "
haoyu = "Haoyu"
s = "Yu datou and Haoyu "
print(s.startswith(datou))

c = "DDDDDDDatou shi zhu "
print(c.strip(),end="--") #看不出是否删除了两边的空格
print()
print(c.strip('D'),end="--")

