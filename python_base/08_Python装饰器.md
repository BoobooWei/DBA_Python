<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [08_Python装饰器](#08python装饰器)
	- [装饰器基本理论](#装饰器基本理论)
		- [实践1-计算函数执行耗时](#实践1-计算函数执行耗时)
		- [高阶函数的定义](#高阶函数的定义)
		- [函数嵌套](#函数嵌套)
		- [函数闭包](#函数闭包)
	- [函数闭包装饰器基本实现](#函数闭包装饰器基本实现)
		- [函数闭包加上返回值](#函数闭包加上返回值)
		- [函数闭包加上参数](#函数闭包加上参数)
		- [函数闭包加上解压序列](#函数闭包加上解压序列)
		- [函数闭包加上认证功能](#函数闭包加上认证功能)
		- [函数闭包模拟session](#函数闭包模拟session)
	- [函数闭包展示器运行流程](#函数闭包展示器运行流程)
	- [函数闭包待参数装饰器](#函数闭包待参数装饰器)

<!-- /TOC -->

# 08_Python装饰器

## 装饰器基本理论

装饰器：
* 本质:`函数`
* 功能:`为其他函数添加附加功能`

原则：
1. 不修改被修饰函数的源代码
2. 不修改被修饰函数的调用方式

`装饰器 = 高阶函数 + 函数嵌套 + 闭包`


### 实践1-计算函数执行耗时

```python
import time
def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数运行时间为 {}'.format(str(end_time - start_time)))
        return res
    return wrapper        

@time_count
def cal(a_list):
  time.sleep(1)
  return list(map(lambda x: x+1, a_list))

response = cal([1,2,3])
print(response)
```

### 高阶函数的定义

1. 函数接收的参数是一个函数名
2. 函数的返回值是一个函数名
3. 满足上述条件任意一个，都可称为高阶函数

```python
def a():
  return "This is a"

def b(func):
  a = func()
  print("This is b")
  return a   

res = b(a)
print(res)  
```

### 函数嵌套

参数为字符串

```python
def b(name):
  print("This is b")
  def a(name):
    return "This is {}".format(name)
  res = a(name)  
  return res  

res = b('booboo')
print(res)
```

参数有函数和字符串

```python
def test():
  print("This is test")

def b(func, name):
  print("This is b")
  func()
  def a(name):
    return "This is {}".format(name)
  res = a(name)  
  return res  

res = b(test,'booboo')
print(res)
```



### 函数闭包

`局部变量`或`嵌套函数`仅限于在`函数体内`使用。但在一些情况下，可以将`函数内部的嵌套函数引入到全局环境中使用`，**Python将引入到全局环境中使用的嵌套函数及其环境变量构建成一个封闭的包，该包内的环境变量不受外部环境的影响，这就是我们将要讨论的闭包**。

前面我们了解了嵌套函数的作用域仅限于其父函数体内，如果在父函数体外调用其嵌套的函数，就会超出嵌套函数的作用域。

```python
def line_conf():
    def line(x):
        return 2 * x + 1
    print(line(5))

line_conf()
print(line(5))        
```

超出了line嵌套函数的作用域。

```bash
In [1]: def line_conf():
   ...:     def line(x):
   ...:         return 2 * x + 1
   ...:     print(line(5))
   ...:
   ...: line_conf()
   ...: print(line(5))
11
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-f2a0935498c1> in <module>
      5
      6 line_conf()
----> 7 print(line(5))

NameError: name 'line' is not defined
```

上面的代码定义了line_conf函数，在line_conf函数体内有嵌套定义了计算直线方程的函数line。依据前面学过的知识，我们会推断出在line_conf函数体内调用line函数是合法的，但在line_conf函数体外调用line函数是非法的，因为在line_conf函数体外调用line函数已经超越了line函数的作用域。上面代码的执行结果也验证了我们的推断。


在Python语言中，当父函数体内定义了嵌套函数后，父函数可以把定义的嵌套函数作为嵌套函数的引用返回给调用者。

函数的引用是什么呢？当我们定义一个函数时，不管是父函数还是父函数体内的嵌套函数。Python解释器都会为定义的函数分配内存空间，用于存储函数的代码、使用的变量等等，该内存的地址被赋值给函数名称所标识的存储单元，函数调用者可以通过函数名称所标识的存储单元找到函数的内存地址，并执行该函数。

由此看来，函数名称也是一个变量，它存储了函数的内存地址。函数的内存地址既能赋值给函数名称，也可以通过函数名称赋值给其它变量，只不过其它变量存储的不是函数的直接内存地址，而是函数名称的内存地址。例如前面代码定义的line函数，可以把line函数名称的地址赋值给变量a和b，执行a、b、line的效果都是一样的。

```python
def line_conf():
    def line(x):
        return 2 * x + 1
    a = line
    b = line
    print(line(5))
    print(a(5))
    print(b(5))

line_conf()        
```

运行结果

```bash
In [2]: def line_conf():
   ...:     def line(x):
   ...:         return 2 * x + 1
   ...:     a = line
   ...:     b = line
   ...:     print(line(5))
   ...:     print(a(5))
   ...:     print(b(5))
   ...:
   ...: line_conf()
11
11
11
```

上面的代码把line函数名称分别赋值给局部变量a和b，分别执行line（5）、a（5）、b（5），其执行结果是相同的。由此可以证明，变量a和b与line指向同一个函数。在这种情况下，我们说a和b是line函数的引用。

理解了什么是函数的引用后，我们就很容易理解把函数作为一个引用返回给调用者了。当父函数把父函数体内的嵌套函数名称返回给调用者时，实际上是把嵌套函数名称的内存地址返回给调用者，调用者将返回的函数名称内存地址赋值给接收变量，调用者通过接收的变量就可以执行接收变量所引用的函数。

```python
def line_conf():
    def line(x):
        return 2 * x + 1
    return line

my_line = line_conf()
print(my_line(5))        
```


上面的代码把line_conf函数内部定义的line嵌套函数返回给调用者，调用者将line嵌套函数的内存地址赋值给my_line变量，最后执行my_line所引用的line函数。执行结果如下所示。


```bash
In [3]: def line_conf():
   ...:     def line(x):
   ...:         return 2 * x + 1
   ...:     return line
   ...:
   ...: my_line = line_conf()
   ...: print(my_line(5))
11
```

现在我们已经实现了把父函数中的嵌套函数引入到全局环境中，嵌套函数可以在父函数体外被调用。这已经是闭包的概念了，嵌套函数作为一个独立的执行环境被外部引用，此时被外部环境独立引用的嵌套函数已经脱离了父函数体，构成一个独立的运行环境。

我们都知道，局部变量在函数执行完成后就被销毁了。那么，如果在line函数中使用了line_conf的变量，当line_conf函数执行完成后，返回到全局环境的line函数还能使用line_conf的中的变量吗？

```python
def line_conf():
    b = 15
    def line(x):
        return 2 * x + b
    return line

b = 5
my_line = line_conf()
print(my_line(5))        
```

在上面的代码中，line函数使用了其父函数声明的变量b，变量b在line函数的定义之外，此时b为line的环境变量。当line函数作为line_conf函数的返回值时，变量b的取值已经和line函数绑定在一起，也就是说父函数和line函数绑定的变量b的值已经没有关系了，变量b即使再有变化，也不会影响到line函数的计算结果。在这种情况下，我们说line函数和它的环境变量b构成了一个闭包，闭包是一个独立的运行环境，不受外部环境的影响和约束。上面的代码输出结果为25，而不是15。

运行结果

```bash
In [4]: def line_conf():
   ...:     b = 15
   ...:     def line(x):
   ...:         return 2 * x + b
   ...:     return line
   ...:
   ...: b = 5
   ...: my_line = line_conf()
   ...: print(my_line(5))
25
```

下面是简单使用闭包的例子，模拟一个计数器。

```python
def counter(startr_at=0):
    count = [startr_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr

count = counter(0)
print(count())

count = counter(5)
print(count())          
```

上面的代码定义了counter函数，它所做的事情就是接收一个初始值并开始计数，初始值赋值给列表count的一个成员。然后在内部定义一个嵌套函数incr，incr使用了父函数的局部变量count，count也是incr函数的环境变量，这样就创建了一个闭包，因为incr函数包含了counter函数中局部变量的作用域。下面是上面代码执行后的输出结果。

```bash
In [5]: def counter(startr_at=0):
   ...:     count = [startr_at]
   ...:     def incr():
   ...:         count[0] += 1
   ...:         return count[0]
   ...:     return incr
   ...:
   ...: count = counter(0)
   ...: print(count())
   ...:
   ...: count = counter(5)
   ...: print(count())
1
6
```

闭包可以将函数和它需要的数据关联起来而不受外部影响。从这点来看，闭包和面向对象基本类似，面向对象也是将数据和行为封装成一个类。在一些情况下使用类也许是最好的方式，闭包更适合函数式编程，函数式编程我们将放在后面讨论。


```python
def test():
  print("This is Test")

def b(func):
  def a():
    func()
    print("BooBoo")
  return a  

test = b(test)
test()
```


## 函数闭包装饰器基本实现

```python
def b(func):
  def a():
    func()
    print("BooBoo")
  return a  

@b
def test():
  print("This is Test")

test()
```

`@b` 相当于`test = b(test)`

### 函数闭包加上返回值


```python
def b(func):
  def a():
    res = func()
    print("BooBoo")
    return res
  return a  

@b
def test():
  print("This is Test")
  return 'test'

res = test()
print(res)
```

### 函数闭包加上参数

```python
def b(func):
  def a(name):
    res = func(name)
    print("BooBoo")
    return res
  return a  

@b
def test(name):
  print("This is {}".format(name))
  return 'test'

res = test('booboo')
print(res)
```

### 函数闭包加上解压序列


解压序列:如果只需要第一个和最后一个，可以通过解压序列直接获取开头和结尾

```bash
I = [10,3,2,3,5,1,2,3,5,8,9]
a,*_,b = I
a
Out[4]: 10
b
Out[5]: 9
a,b,c,*m,last = I
a
Out[7]: 10
b
Out[8]: 3
c
Out[9]: 2
m
Out[10]: [3, 5, 1, 2, 3, 5, 8]
last
Out[11]: 9
```

a,b交换

```bash
a,b=1,2
a,b=b,a
a
Out[17]: 2
b
Out[18]: 1
```

### 函数闭包加上认证功能


```python
# -*- coding:utf-8 -*-

users = [{
    "username": "tom",
    "password": "123"
}]


def auth_func(func):
    def wrapper(*args, **kwargs):
        # 验证功能
        check = 0
        username = input("username:").strip()
        password = input("password:").strip()
        for user in users:
            if username == user["username"] and password == user["password"]:
                check = 1
                break
        if check == 1:
            func(*args, **kwargs)
        else:
            print("认证失败")

    return wrapper


@auth_func
def index():
    print("欢迎来到京东主页")


@auth_func
def home(name):
    print("欢迎回家 {}".format(name))


@auth_func
def shopping_car(name):
    print("%s 的购物车中有[%s, %s, %s]" % (name, "奶茶", "妹妹", "牙刷"))


index()
home("booboo")
shopping_car("booboo")
```

运行结果

```bash
username:booboo
password:123
认证失败
username:tom
password:123
欢迎回家 booboo
username:tom
password:123
booboo 的购物车中有[奶茶, 妹妹, 牙刷]
```

### 函数闭包模拟session

## 函数闭包展示器运行流程

## 函数闭包待参数装饰器
