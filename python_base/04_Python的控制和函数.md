<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [04_Python的控制和函数](#04python的控制和函数)
	- [控制](#控制)
	- [函数](#函数)
		- [函数的定义](#函数的定义)
		- [函数的创建](#函数的创建)
			- [格式](#格式)
			- [函数名的命名规则：](#函数名的命名规则)
			- [形参和实参](#形参和实参)
		- [函数的参数](#函数的参数)
		- [函数的返回值](#函数的返回值)
		- [作用域](#作用域)
			- [作用域介绍](#作用域介绍)
			- [作用域产生](#作用域产生)
			- [global关键字](#global关键字)
			- [nonlocal关键字](#nonlocal关键字)
			- [小结](#小结)
		- [递归函数](#递归函数)
			- [实践1-阶乘](#实践1-阶乘)
			- [实践2-斐波那契数列](#实践2-斐波那契数列)
		- [内置函数](#内置函数)
			- [重要的内置函数](#重要的内置函数)
		- [函数式编程](#函数式编程)
			- [定义](#定义)
			- [函数式编程的有点](#函数式编程的有点)
			- [实践1-求列表中的正数的平均值](#实践1-求列表中的正数的平均值)
			- [实践2-求阶乘](#实践2-求阶乘)

<!-- /TOC -->

# 04_Python的控制和函数

## 控制

* `if else`

* `for`

* `while`


## 函数

### 函数的定义

函数一词来源于数学，但编程中的`函数`概念，与数学中的函数是有很大不同的，具体区别，我们后面会讲，编程中的函数在英文中也有很多不同的叫法。在BASIC中叫做subroutine(子过程或子程序)，在Pascal中叫做procedure(过程)和function，在C中只有function，在Java里面叫做method。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可

特性:
1. 代码重用
2. 保持一致性
3. 可扩展性


### 函数的创建

#### 格式

Python 定义函数使用 def 关键字，一般格式如下：


```python
def 函数名（参数列表）:
    函数体
```

举例
```python     
def hello():
    print('hello')
```

调用`hello()`

#### 函数名的命名规则：

* 函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号；
* 函数名是区分大小写的。
* 函数名不能是保留字。

#### 形参和实参

* 形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参（实参个数，类型应与实参一一对应）
* 实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参   

区别：

* 形参是虚拟的，不占用内存空间
* 形参变量只有在被调用时才分配内存单元，
* 实参是一个变量，占用内存空间，数据传送单向，实参传给形参，不能形参传给实参

### 函数的参数

|类型|说明|
|:--|:--|
|必需的参数|必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。|
|缺省参数（默认参数）|调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入|
|不定长参数|你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。|

### 函数的返回值

要想获取函数的执行结果，就可以用return语句把结果返回

注意:

* 函数在执行过程中只要遇到return语句，就会停止执行并返回结果，也可以理解为 return 语句代表着函数的结束
* 如果未在函数中指定return,那这个函数的返回值为None  
* return多个对象，解释器会把这多个对象组装成一个元组作为一个一个整体结果输出。

### 作用域

#### 作用域介绍

python中的作用域分4种情况：

* L：local，局部作用域，即函数中定义的变量；
* E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
* G：globa，全局变量，就是模块级别定义的变量；
* B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。

#### 作用域产生

在Python中，只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如if、try、for等）是不会引入新的作用域的。

#### global关键字

当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了，当修改的变量是在全局作用域（global作用域）上的，就要使用global先声明一下。

#### nonlocal关键字

global关键字声明的变量必须在全局作用域上，不能嵌套作用域上，当要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量怎么办呢，这时就需要nonlocal关键字了。

#### 小结

* 变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
* 只有模块、类、及函数才能引入新作用域；
* 对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
* 内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。


### 递归函数

定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

#### 实践1-阶乘

```python
def factorial(n):

    result=n
    for i in range(1,n):
        result*=i

    return result

print(factorial(4))

def factorial_new(n):

    if n==1:
        return 1
    return n*factorial_new(n-1)

print(factorial_new(3))
```

#### 实践2-斐波那契数列

```python
def fibo(n):

    before=0
    after=1
    for i in range(n-1):
        ret=before+after
        before=after
        after=ret

    return ret

print(fibo(3))


def fibo_new(n):

    if n <= 1:
        return n
    return(fibo_new(n-1) + fibo_new(n-2))

print(fibo_new(3))
1
print(fibo_new(30000))
```
maximum recursion depth exceeded in comparison


递归函数的优点:   

1. 是定义简单，逻辑清晰。
2. 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

递归特性:

1. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3. 递归效率不高，递归层次过多会导致栈溢出(在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。)


### 内置函数

https://docs.python.org/3/library/functions.html

|                                                              |                                                              | Built-in Functions                                           |                                                              |                                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`abs()`](https://docs.python.org/3/library/functions.html#abs) | [`delattr()`](https://docs.python.org/3/library/functions.html#delattr) | [`hash()`](https://docs.python.org/3/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/3/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/3/library/functions.html#func-set) |
| [`all()`](https://docs.python.org/3/library/functions.html#all) | [`dict()`](https://docs.python.org/3/library/functions.html#func-dict) | [`help()`](https://docs.python.org/3/library/functions.html#help) | [`min()`](https://docs.python.org/3/library/functions.html#min) | [`setattr()`](https://docs.python.org/3/library/functions.html#setattr) |
| [`any()`](https://docs.python.org/3/library/functions.html#any) | [`dir()`](https://docs.python.org/3/library/functions.html#dir) | [`hex()`](https://docs.python.org/3/library/functions.html#hex) | [`next()`](https://docs.python.org/3/library/functions.html#next) | [`slice()`](https://docs.python.org/3/library/functions.html#slice) |
| [`ascii()`](https://docs.python.org/3/library/functions.html#ascii) | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) | [`id()`](https://docs.python.org/3/library/functions.html#id) | [`object()`](https://docs.python.org/3/library/functions.html#object) | [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) |
| [`bin()`](https://docs.python.org/3/library/functions.html#bin) | [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) | [`input()`](https://docs.python.org/3/library/functions.html#input) | [`oct()`](https://docs.python.org/3/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod) |
| [`bool()`](https://docs.python.org/3/library/functions.html#bool) | [`eval()`](https://docs.python.org/3/library/functions.html#eval) | [`int()`](https://docs.python.org/3/library/functions.html#int) | [`open()`](https://docs.python.org/3/library/functions.html#open) | [`str()`](https://docs.python.org/3/library/functions.html#func-str) |
| [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint) | [`exec()`](https://docs.python.org/3/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/3/library/functions.html#ord) | [`sum()`](https://docs.python.org/3/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/3/library/functions.html#func-bytearray) | [`filter()`](https://docs.python.org/3/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/3/library/functions.html#pow) | [`super()`](https://docs.python.org/3/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/3/library/functions.html#func-bytes) | [`float()`](https://docs.python.org/3/library/functions.html#float) | [`iter()`](https://docs.python.org/3/library/functions.html#iter) | [`print()`](https://docs.python.org/3/library/functions.html#print) | [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/3/library/functions.html#callable) | [`format()`](https://docs.python.org/3/library/functions.html#format) | [`len()`](https://docs.python.org/3/library/functions.html#len) | [`property()`](https://docs.python.org/3/library/functions.html#property) | [`type()`](https://docs.python.org/3/library/functions.html#type) |
| [`chr()`](https://docs.python.org/3/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/3/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/3/library/functions.html#func-list) | [`range()`](https://docs.python.org/3/library/functions.html#func-range) | [`vars()`](https://docs.python.org/3/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/3/library/functions.html#getattr) | [`locals()`](https://docs.python.org/3/library/functions.html#locals) | [`repr()`](https://docs.python.org/3/library/functions.html#repr) | [`zip()`](https://docs.python.org/3/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/3/library/functions.html#compile) | [`globals()`](https://docs.python.org/3/library/functions.html#globals) | [`map()`](https://docs.python.org/3/library/functions.html#map) | [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/3/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr) | [`max()`](https://docs.python.org/3/library/functions.html#max) | [`round()`](https://docs.python.org/3/library/functions.html#round) |                                                              |

#### 重要的内置函数

* `filter(function, sequence)`
* `map(function, sequence) `
* `reduce(function, sequence, starting_value)`　
* `lambda`

### 函数式编程

#### 定义

函数式编程是一种编程范式，我们常见的编程范式有命令式编程（Imperative programming），函数式编程，常见的面向对象编程是也是一种命令式编程。

命令式编程是面向计算机硬件的抽象，有变量（对应着存储单元），赋值语句（获取，存储指令），表达式（内存引用和算术运算）和控制语句（跳转指令），一句话，命令式程序就是一个冯诺依曼机的指令序列。
而函数式编程是面向数学的抽象，将计算描述为一种表达式求值，一句话，函数式程序就是一个表达式。

**函数式编程的本质**

函数式编程中的函数这个术语不是指计算机中的函数，而是指数学中的函数，即自变量的映射。也就是说一个函数的值仅决定于函数参数的值，不依赖其他状态。比如y=x*x函数计算x的平方根，只要x的平方，不论什么时候调用，调用几次，值都是不变的。

纯函数式编程语言中的变量也不是命令式编程语言中的变量，即存储状态的单元，而是代数中的变量，即一个值的名称。变量的值是不可变的（immutable），也就是说不允许像命令式编程语言中那样多次给一个变量赋值。比如说在命令式编程语言我们写“x = x + 1”，这依赖可变状态的事实，拿给程序员看说是对的，但拿给数学家看，却被认为这个等式为假。
函数式语言的如条件语句，循环语句也不是命令式编程语言中的控制语句，而是函数的语法糖，比如在Scala语言中，if else不是语句而是三元运算符，是有返回值的。
严格意义上的函数式编程意味着不使用可变的变量，赋值，循环和其他命令式控制结构进行编程。

**函数式编程关心数据的映射，命令式编程关心解决问题的步骤**，这也是为什么“函数式编程”叫做“函数式编程”。

#### 函数式编程的有点

1. 代码简洁
2. 无副作用

由于命令式编程语言也可以通过类似函数指针的方式来实现高阶函数，函数式的最主要的好处主要是不可变性带来的。没有可变的状态，函数就是`引用透明（Referential transparency）`的和`没有副作用（No Side Effect）`。

#### 实践1-求列表中的正数的平均值

```python
nums = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
num_lt_0 = list(filter(lambda x: x>0, nums))
avg_num = sum(num_lt_0) / len(num_lt_0)
```

#### 实践2-求阶乘

```python
from functools import reduce
print (reduce(lambda x,y: x*y, range(1,6)))
```
