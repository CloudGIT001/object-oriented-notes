#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

"""
成员修饰符
    私有：
        只能类自己本身成员内部可以访问
    共有：
        pass

    ps: 不到万不得已不要在外部强制访问私有成员，_类名__xxxx


"""

class Foo:
    def __init__(self,name):
        self.__name = name   # 将name设置为私有普通字段

    def f1(self):
        print(self.__name)
obj = Foo("helloworld")
# print(obj.__name)  # 外面访问出错，私有自带只能内部访问
obj.f1()
# helloworld
print(obj._Foo__name)  # 从外面强制访问私有的字段
# helloworld


# 当存在继承关系
class Foo:
    def __init__(self,name):
        self.__name = name   # 将name设置为私有

    def f1(self):
        print(self.__name)

class Bar(Foo):
    def f2(self):
        print(self.__name)
# obj = Bar("hellopython")  # 运行出错，私有的字段也不能继承
# obj.f2()
# # AttributeError: 'Bar' object has no attribute '_Bar__name'


# 设置私有静态字段

class Foo:
    __cc = "123456"

    def __init__(self,name):
        self.name = name

    def f1(self):
        print(self.name)

    def f3(self):
        print(Foo.__cc)  # 内部访问私有的静态字段

    @staticmethod
    def f4():
        print(Foo.__cc)   # 设置静态方法

# print(Foo.__cc) 不允许在外面访问私有的静态字段
obj =   Foo("python")
obj.f3()
# 123456
Foo.f4()
# 123456

