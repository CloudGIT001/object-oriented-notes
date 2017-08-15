#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


"""
面向对象：


1. python 支持函数式编程，和面向对象编程

2. 函数式编程，面向对象编程实现： 发送邮件功能

3. 类和对象
    a. 创建类
        class 类名：
            def 方法名（self,xxxx）
            pass
    b. 创建对象
        对象 = 类名()

    c. 通过对象执行方法
        对象.方法名(123)

4.
    函数式：
        def fetch(host,username,password,sql):
            pass
        def create(host,username,password,sql):
            pass
        def remove(host,username,password,nid):
            pass
        def modify(host,username,password,name):
            pass

    面向对象：
        class SQLHelper:

            def fetch(self,sql):
                pass
            def create(self,sql):
                pass
            def remove(self,nid):
                pass
            def modify(self,name):
                pass
        obj = SQLHelper()
        obj.hhost = "aaaa"
        obj.uuser = "xxxx"
        obj.ppwd = "12234"

        obj.fetch(......)

--------------->>>: 什么时候用面向对象？当某一些函数具有相同参数时，可以使用面向对象的方式，将参数值一次性封装到对象，以后去对象中取值即可


5. self 是什么鬼？
    self 是一个python自动会传值的参数
    那个对象执行方法，self就是谁


6.  init 的特殊方法
    类中有一个特殊的方法，__init__,类()自动被执行
    __init__(): 构造函数，也称为构造方法

    class SQLHelper:

        def __init__(self,host,username,password):
            self.host = host
            self.username = username
            self.password = password

        def fetch(self,sql):
            pass
        def create(self,sql):
            pass
        def remove(self,nid):
            pass
        def modify(self,name):
            pass

    obj.fetch(......)


7. 面向对象
    三大特性：封装、继承、多态

"""

# 函数式编程，面向对象编程实现： 发送邮件功能

def mail(email,message):
    print("发邮件信息")
    return True
mail("aaa@bb.com","message")


# 面向对象：类，对象

class Foo:
    # 方法
    def email(self,mail,message):
        print("发邮件信息")
        return True
# 调用，1：创建对象，类名()
obj = Foo()
# 2. 通过对象执行方法
obj.email("aaa@bb.com","message")

# def 函数的关键字，class 类的关键字


# 封装对象简单示例_v1

class c1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj


class c2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)

class c3:
    def __init__(self,a1):
        self.money = 123
        self.aaa = a1


c2_obj = c2("aaa",22) # 调用c2
c2_obj.show()  # 调用c2的show方法
# c2_obj 是c2类型
# - name = "aaa"
# - age = 22

c1_obj = c1("hello",c2_obj)  # 将c2类以obj的参数传入c1
print(c1_obj.obj.name)
# c1_boj 是c1类型
# - name = "hello"
# - obj = c2_obj() == c2_obj.name + c2_obj.age

c3_obj = c3(c1_obj)
print(c3_obj.aaa.obj.name) # 通过c3获取c2的name
# 使用c3_obj 执行show方法
c3_obj.aaa.obj.show()

ret = c3_obj.aaa.obj.show()
print(ret) # 输出结果为None,原因，c2中的show()方法 没有返回值，所以输出结果为None
