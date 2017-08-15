#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


"""
面向对象中的类成员
    字段
        静态字段
        普通字段
        ps: 静态字段代码加载时候已经创建，普通字段必须要创建对象时，才创建到内存中

    方法
        方法由对象调用，所有的方法属于类
        1. 普通方法：至少一个self,对象执行
        2. 静态方法：任意参数，类执行（对象执行）
        3. 类方法： 至少一个cls,类执行

    属性
        不伦不类的东西
        具有方法的写作形式，具有字段的访问形式

学习参考：http://www.cnblogs.com/wupeiqi/p/4766801.html

"""

# 字段

class Foo:

    dd = 123456 # 字段（静态字段。属于类中）

    def __init__(self):
        self.name = "python"   # 字段（普通字段，保存对象中），self.xxx = xxx 这些统称字段

    def show(self):
        print(self.name)

# 示例_v1
class Province:

    country = "中国" # 将country设置为静态字段，各省份公用一个country，节省内存空间

    def __init__(self,name):
        self.name = name
        # self.country = "中国"

# 一般情况下，自己访问自己的字段
# 规则：
# 普通字段只能对象访问
# 静态字段用类访问（万不得已的时候可以使用对象访问）
gd = Province("广东")
gx = Province("广西")
hn = Province("河南")
print(hn.name)  # 访问省份（即访问普通字段）
print(Province.country) # 通过类访问静态字段方法，直接类调用
print(hn.country)  #通过对象访问静态字段
# 河南
# 中国
# 中国


# 方法

class Province:

    country = "中国"

    def __init__(self,name):
        self.name = name

    # 普通方法，由对象去调用执行（方法属于类）
    def show(self):
        print(self.name)

    @staticmethod
    def f1(*args):   #  静态方法属于类，由类直接调用执行，跟对象没关系
        print(*args)
        pass

    @classmethod
    def f2(cls):   # 类方法,必须有cls 参数。自动传值，得到类名称
        print(cls)

obj = Province("广东")
obj.show()
# 广东
Province.f1(111,222)
# 111 222
Province.f2()
# <class '__main__.Province'>


# 属性

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    @property  # 取值装饰器
    def all_pager(self):  # 完成一个简单的分页功能
        a1,a2 = divmod(self.all_count,10)  # divmod 得到两个值，第一个为商，第二个为余数
        if a2 == 0:
            return a1
        else:
            return a1+1

    @all_pager.setter  # 设置值装饰器
    def all_pager(self,value):
        print(value)

    @all_pager.deleter  # 删除值装饰器
    def all_pager(self):
        print("del all_pager")


P = Pager(102)
# result = P.all_pager()
# print(result)
# # 11
ret = P.all_pager  # 通过@property 改变属性 不需要调用可以直接得到结果
print(ret)
# 11
P.all_pager = 111
# 111
del P.all_pager
# del all_pager



# 另一种属性的表达方式

class Pager1:
    def __init__(self,all_count):
        self.all_count = all_count

    def f1(self):
        return "Pager1.f1"

    def f2(self,value):
        print(value)

    def f3(self):
        print("del Pager.f3")

    foo = property(fget=f1,fset=f2,fdel=f3)
P = Pager1(101)
result = P.foo  # 执行fget=f1
print(result)
# Pager1.f1
P.foo = "PYTHON"  # 执行fset=f2
# PYTHON
del P.foo  # 执行fdel=f3
# del Pager.f3