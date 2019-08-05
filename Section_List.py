print('Hello world')
'''
list列表
    -一组由有序数据做成的序列
        -数据就有先后顺序
        -数据可以不是一类数据
    -list的创建
        -直接创建。用中括号创建，内容直接用英文逗号隔开
    -列表的常见操作
        -访问
            -使用下标操作，也叫索引
            -列表的元素索引是从0开始
        -切片操作
            -对列表进行任意一段的截取
            -截取之后，创建一个新的列表
'''


'''
tuple元组
    -可以理解成一个不可以随便更改的列表
    -tuple其余特征和list基本一致
        -有序
        -可以访问不可以被修改
        -元素可以是任意类型
'''

#tuple的创建
ta = () #使用括号创建
print(type(ta))

tb = 100,200  #使用逗号直接创建
print(tb)

li = [1,2,3,"datou"]
tc = tuple(li) #要求tuple参数必须可迭代
print(tc)
print(li)

#tuple索引操作
ca = ["datou","yusimin","changhaoyu"]
print(ca)
ta = tuple(ca)
print(ta[2])
#tuple切片操作
print(ta[:])
print(ta[:2])
#元祖的相加
ta = 100,200,300
tb = ("yusimin ","changhaoyu ","love")
tc = ta + tb
print(tc)

#元祖的相乘
tc = tb*2
print(tc)
#成员检测
if "love" in tb :
    print("对的")
#元祖遍历
for i in tb :
    print(i)
#嵌套元祖
tc = ((100,200,300),("changhaoyu","love","ss"),("yusimin","sd","cs"))
for i in tc:
    print(i)
    for j in i :
        print(j)
for i,j,k in tc : #必须保证每个元祖的元素一致
    print(i,j,k)

#常用元祖函数
#len:取长度
Len = 100,200,300
print(len(Len))
#count：对某一元素计数
sz = 1,1,1,1,200,2,35,124,1
print(sz.count(1))
#index：某一元素所在位置
sb = ("yusimin","changhaoyu","yuansu")
print(sb.index("yuansu"))
#tuple的特殊用法
a = 100
b  = "yusimin"
a,b = b,a
print(a,b)

'''
set 集合
    -跟数学中的集合的概念一致
    -内容无需+内容不重复
'''

#集合的定义
#1、通过set关键字
ra = set()
print(ra)
rb = [1,23,4,5,6,7,8,9,10,1,2,1,2]
rc = set(rb)
print(rc)
#in操作
if 2 in rc :
    print(222222)
if 24 in rc :
    print(444444)

#集合的内置函数
#len：长度
#max/min :最值
#add：向集合中添加元素
sa = {1,2,3,4,5,6,5,4,3,2,1}
print(sa)
sa.add(7)
print(sa)
#clear:清空
#remove 、discard 删除
print(sa)
sa.remove(5) #remove 删除的值如果不在集合中，报错
print(sa)

#pop弹出集合的一个内容
#删除的内容是随机的
sa = {1,2,3,4,5,6,7}
print(sa)
sa.pop()
print(sa)
print(sa)

sa = {1,2,3,4,5,6,7}
sb = {4,5,6,7,8}
print(sa.intersection(sb)) #交集
print(sa.difference(sb)) #差集
print(sa-sb) #差集的另外一种表达形式
print(sa.union(sb)) #并集

#frozenset 冰冻集合
print(sa)
sb = frozenset(sa)
print(sb)

'''
递归函数
    -递归：函数间接或直接调用自己
    -递归两个过程：
        -往下调用，分解的过程
        -往上回数，综合的过程
    -递归需要注意
        -一定要有结束条件
    -是以资源换取编写速度
'''
#fun_a表示计算阶乘
#利用数学公式
def fun_a(n) :
    print(n)
    #递归一定要有结束条件
    if n == 1:
        return 1
    return n*fun_a(n-1)
rst =fun_a(5)
print(rst)

#递归必须有结束条件，否则会死掉
def fun_b(n) :
    print(n)
    return n * fun_b(n-1)
 #斐波那契数列
def Feb(n) :
    if n ==1 or n ==2:
        return 1
    return Feb(n-1)+Feb(n-2)
rst = Feb(10)
print(rst)

#汉诺塔
a = "A"
b = "B"
c = "C"
def han_a(a,b,c,n):
    if n ==1 :
        print("{}--{}>".format(a,c))
        return None
    if n ==2 :
        print("{}-->{}".format(a,c))
        print("{}-->{}".format(a,b))
        print("{}-->{}".format(b,c))
        return None
    han_a(a,c,b,n-1)
    print("{}-->{}".format(a,c))
    han_a(b,a,c,n-1)
han_a(a,b,c,5)

'''
OPP
    -思想
        -以模块化思想解决工程问题
         -面向过程 VS 面向对象
        -由面向过程转向面向对象
        -例子：开学校，叫青玉学院，教编程
            -讲师
            -学生
            -班主任
            -教室
            -学校
    -常用名词
        -OO：面向对象
        -ooa：分析
        -ood：设计
        -oop：编程
        -ooi：实现
        -ooa-> ood -> ooi
    -类 VS 对象
        -类：抽象，描述的是一个集合，侧重与共性
        对象：具体，描述的是个体
    -类的内容：
        -动作，函数
        -属性，变量
    -定义类：class关键字
    -类命名：
        -遵循大驼峰
        -第一个字母大写
    -self
        -self可以用别的名称代替
        -self不是关键字
        -作用是指代本身
    -类的变量作用域的问题
        -类变量：属于类自己的变量
        -实例变量：属于实例的变量
        -访问实例的属性，如果实例没有定义属性，则自动访问类的属性，如果类也没有定义，则报错
    -访问类的属性
        -在类里面如果强制访问类的属性，则需要使用__class__,(注意前后是两个下划线)
        -类方法
            -定义类的方法的时候，没self参数
            -类的方法只允许使用类的内容
            -两种用法
                -ClassName
                -__class__
    -构造函数
        -类在实例化的时候，执行一些基础性的初始化的工作
        -使用特殊的名称和写法
        -在实例化的时候自动执行
        -是在实例化的时候第一个被执行的函数    
'''
#定义学生类，和几个学生
class Student():
    pass #pass是关键字，表示占位用的，无意义
#定义一个对象
xxxxxbai = Student()

#
class PythonStudent() :
    name = "NoOne"
    age = 18
    course = "Python"
    def giveMeMoneys(meme):
        print("Show me the money")
        return None
Xiaobai = PythonStudent()
print(Xiaobai.name)
print(Xiaobai.age)
print(Xiaobai.course)

#self举例
#实例调用函数
datou = PythonStudent
#让大头跟我打声招
datou.giveMeMoneys(datou)

#注意类的定义
class Students():
    #name,age是类的变量
    #注意类的变量的定义位置和方法
    #不需要前缀
    name = "常浩宇"
    age = 22
    def sayHi(self):
        print("My name is {},I am {} years old".format(self.name,self.age))
        return None


class People() :
    sex = "男"
    job = "Teacher"
    def niHao(self):
        print("My sex is {},I am a {} ".format(self.sex,self.job))
        return None
Test = People()
Test.niHao()
#体验类的方法
s = Students()
s.sayHi()

#调用类的方法的例子

#构造函数
class Studeng():
    names = "NoName"
    ages = 0
    #构造函数名称固定，写法相对固定
    def __init__(self):
        print("我是构造函数")
erjings = Studeng()
print("-----------------")
print(erjings.names)
print(erjings.ages)