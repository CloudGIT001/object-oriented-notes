#### 第三模块，面向对象笔记 -- wupeiqi版

学习参考链接：http://www.cnblogs.com/wupeiqi/p/4493506.html

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
        
5. self 是什么鬼？
    self 是一个python自动会传值的参数
    那个对象执行方法，self就是谁


6.  init 的特殊方法
    类中有一个特殊的方法，__init__,类()自动被执行
    __init__(): 构造函数，也称为构造方法
    

##### 面向对象 -- 继承


##### 多态：
    python 一般用不到
    
    
##### 面向对象中的类成员
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


##### 成员修饰符
    私有：
        只能类自己本身成员内部可以访问
    共有：
        pass

    ps: 不到万不得已不要在外部强制访问私有成员，_类名__xxxx
    
    
##### 面向对象其他知识点
    - isinstance
    - issubclass
    - 继承2.7
    - 执行父类结构方法
    - 应用：
        自定义类型，对字典进行补充，有序字典
        源码扩展
