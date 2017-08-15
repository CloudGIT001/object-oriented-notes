#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

"""
面向对象其他知识点
    - isinstance
    - issubclass
    - 继承2.7
    - 执行父类结构方法
    - 应用：
        自定义类型，对字典进行补充，有序字典
        源码扩展

"""

# isinstance # 判断是否是类的对象
class Bar:
    pass

class Foo(Bar):
    pass

obj = Foo()
print(isinstance(obj,Foo))
# True

ret = isinstance(obj,Bar) # 继承关系，obj,Bar(obj类型和obj类型的父类）的实例
print(ret)
# True

# 执行父类结构方法

class C1:
    def f1(self):
        print("C1.f1")
class C2(C1):
    def f1(self):
        ret= super(C2,self).f1() #主动执行父类的f1方法
        print("C2.f1")
        return ret
    
obj = C2()
obj.f1()