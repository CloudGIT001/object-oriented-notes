#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


"""
面向对象 -- 继承


"""

# 示例_v1

class F1:     # 父类，基类
    def show(self):
        print("show")

class F2(F1): # 子类，派生类
    def bar(self):
        print("bar")

    # def show(self):  # 当子类与父类有相同方法时，执行子类的方法，子类优先级大于父类
    #     print("F2.show")

obj = F2() #F2 继承F1的方法
obj.show()
obj.bar()
# show
# bar


# 示例_v2

class F3:     # 父类，基类
    def show(self):
        print("show")

    def foo(self):
        print(self.name)


class F4(F3): # 子类，派生类
    def __init__(self,name):
        self.name = name

    def bar(self):
        print("bar")

    def show(self):  # 当子类与父类有相同方法时，执行子类的方法，子类优先级大于父类
        print("F2.show")

    # def show(self):
    #     print("show")
    #
    # def foo(self):
    #     print(self.name)

obj = F4("hello") #F2 继承F1的方法
obj.foo()  # 可以执行F3中的foo方法，因为继承相当于将F3的方法在F4中重新写了一遍
# hello


# 示例_v3
class S1:
    def F1(self):
        self.F2()
    def F2(self):
        print("s1.f2")

class S2(S1):
    def F3(self):
        self.F1()
    def F2(self):
        print("s2.f2")

obj = S2()
obj.F3()    # 执行的结果是 S2.F2方法 （当子类和父类存在相同方法时，执行子类的方法）
# s2.f2
obj = S1()
obj.F1()    #
# s1.f2


# 示例_v4 多继承

class C1:
    def f1(self):
        print("f1")

    def f2(self):
        print("c1.f2")

class C2:
    def f2(self):
        print("f2")

class C3(C1,C2):  # C3 继承 C1 和 C2 ，C1优先级比C2高
    def f3(self):
        pass

obj = C3()
obj.f2()
# c1.f2


# 示例_v5 多继承

class C0:
    def f2(self):
        print("c0.f2")

class C1(C0):
    def f1(self):
        print("f1")


class C2:
    def f2(self):
        print("f2")

class C3(C1,C2):  # C3 继承 C1 和 C2 ，C1优先级比C2高
    def f3(self):
        pass

obj = C3()
obj.f2()       # 当C1没有f2方法，向上查找，直到没有，再往C2方向找，关系是：先自己，然后左，左上，再右，右上
# c0.f2


# 示例_v6 多继承

class B0:
    def b2(self):
        print("B0.b2")

class B1(B0):
    def b2(self):
        print("B1.b2")

class B2(B1):
    def b2(self):
        print("B2.b2")

class B_1(B0):
    def b1(self):
        print("B_1.b1")

class B_2(B_1):
    def b1(self):
        print("B_2.b1")

class B3(B_2,B2):
    def b1(self):
        print("B3")

obj = B3()
obj.b2()    # 没有共同父类，一路走到黑，当有共同的父类，最最最后才找那个共同父类
# B2.b2




# # 示例_v7 多继承
#
# class A0:
#     def process(self):
#         print("A0.process")
#
# class A1:
#     def forever(self):
#         self.run = 123
#
# class A2(A1):
#     def __init__(self):
#         pass
#     def run(self):
#         pass
#     def process(self):
#         print("A2.process")
#
# class A3(A2):
#     def __init__(self):
#         print("A3.INIT")
#
# class A4(A0,A3):
#     pass
#
# obj = A4
# obj.forever()

"""
作业：选课系统
    
    思路：
        管理员：
            1. 创建老师（爱好，姓名，年龄，资产=0）
            class Teacher:
                def __init__(self,favor,name,age)
                    self.favor = favor
                    self.name = name
                    self.age = age
                    self.asset = 0
                def 教学事故()
                    self.asset = self.asset - 1
                def 挣钱()
                    self.asset = self.asset - 1
                    
            obj1 = Teacher(...)
            obj2 = Teacher(...)
            obj3 = Teacher(...)
            obj4 = Teacher(...)
            [obj1,obj2,obj3....]
            pickle.dump([obj1,obj2,obj3....],文件)
            # Teacher 类型  （pickle 可以对python所有类型进行序列化）
            
            2. 创建课程
                li = pickle.load()
                li[0]
            
                课程类
                    - 课程名
                    - 课时费
                    - 负责老师 = obj1
                
                功能：
                    上课
                        返回给学生学习的内容
                        负责老师加钱
                课程对象()
                
        
        学生：
            类 >>> 选课 （可多选）
            
            __init__
                选课 = [课程对象，列表形式]
            
            上课：
                选课
                1. 生物课
                    课程对象.上课()

"""