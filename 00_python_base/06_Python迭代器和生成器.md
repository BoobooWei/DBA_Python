<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [06_Python迭代器和生成器](#06python迭代器和生成器)
	- [迭代器协议](#迭代器协议)
	- [for循环工作机制](#for循环工作机制)
		- [实践1-调用列表的`__iter__()`方法查看其类型是什么？](#实践1-调用列表的iter方法查看其类型是什么)
		- [实践2-列表迭代器是否真的存在`__next__()`方法?](#实践2-列表迭代器是否真的存在next方法)
		- [实践3-for循环列表迭代器打印每一个元素](#实践3-for循环列表迭代器打印每一个元素)
		- [实践4-通过索引去遍历列表的每一个元素](#实践4-通过索引去遍历列表的每一个元素)
	- [`next()`方法](#next方法)
		- [实践1-通过`next()`获取列表的每一个元素](#实践1-通过next获取列表的每一个元素)
	- [三元运算](#三元运算)
	- [列表解析](#列表解析)
		- [实践1-生成1000万个数字](#实践1-生成1000万个数字)
	- [生成器表达式](#生成器表达式)
		- [实践1-生成1000万个数字](#实践1-生成1000万个数字)
	- [生成器](#生成器)
		- [实践1-普通函数实现斐波拉契数列](#实践1-普通函数实现斐波拉契数列)
		- [实践2-生成器实现斐波拉契数列](#实践2-生成器实现斐波拉契数列)
	- [总结](#总结)

<!-- /TOC -->

# 06_Python迭代器和生成器

## 迭代器协议

* 迭代器协议：对象必须提供一个`netx`方法，执行该方法要么返回迭代中的下一项，要么就引起一个`StopIteration`异常，
以终止迭代（只能往后不能往前退）
* 可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个`__iter__()`方法）
* 协议：是一种约定，可迭代对象实现了迭代器协议，python的内部工具（
如for循环，sum，min，max函数等）是用迭代器协议访问对象。


## for循环工作机制

> for循环的本质：循环所有对象，全都是使用迭代器协议。

对象（字符串、列表、字典、集合、文件）内部存在`__iter__()`方法，
例如`I = [1, 2, 3]`

I 为 列表，`I.__iter__()`为 可迭代对象。


### 实践1-调用列表的`__iter__()`方法查看其类型是什么？

```python
I = [1, 2, 3]
type(I.__iter__())
```

运行结果

```bash
Out[6]: list_iterator
```

通过type()查看`I.__iter__()`为列表迭代器。

### 实践2-列表迭代器是否真的存在`__next__()`方法?

```python
I = [1, 2, 3]
I_iter = I.__iter__()
I_iter.__next__()
Out[13]: 1
I_iter.__next__()
Out[14]: 2
I_iter.__next__()
Out[15]: 3
I_iter.__next__()
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3325, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-16-f51388b0da92>", line 1, in <module>
    I_iter.__next__()
StopIteration
```

### 实践3-for循环列表迭代器打印每一个元素


```python
I = [1, 2, 3]
I_iter = I.__iter__()
for i in I_iter:
    print(i)

1
2
3
```

通过for循环列表迭代器打印列表中的每一个元素。


### 实践4-通过索引去遍历列表的每一个元素

```python
I = [1, 2, 3]
i = 0
while i < len(a):
    print(a[i])
    i = i+1

0
1
2
```

> 既然通过索引可以遍历列表中所有的元素，为什么还要用迭代的方式呢？

* 迭代对象可以节省内存空间；
* 不是所有对象都像list一样是有顺序有索引的。

## `next()`方法

> `next()`本质就是调用了可迭代对象的`__next__()方法`

### 实践1-通过`next()`获取列表的每一个元素

```python
I = [1, 2, 3]
I_iter = I.__iter__()
next(I_iter)
Out[13]: 1
next(I_iter)
Out[14]: 2
next(I_iter)
Out[15]: 3
next(I_iter)
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3325, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-16-44acb255902a>", line 1, in <module>
    next(I_iter)
StopIteration
```

## 三元运算

```python
name = 'superman'
'Hero' if name == 'superman' else 'Batman'
Out[18]: 'Hero'
```

## 列表解析

一般写法

```python
man_list = []
for i in range(10):
    man_list.append(i)

man_list
Out[21]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表解析，将所有的元素都放到了内存中。

```python
[i for i in range(10)]
Out[22]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

三元表达式，可以小于三元，但是不能大于三元。

```python
[i for i in range(10) if i > 5]
Out[24]: [6, 7, 8, 9]
```

### 实践1-生成1000万个数字

```python
[i for i in range(1000)]
```

## 生成器表达式

* 把列表解析的`[]`换成`()`得到的就是生成器表达式；
* 列表解析与生成器表达式都是

### 实践1-生成1000万个数字

```python
(i for i in range(1000))
```


## 生成器

一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator）；如果函数中包含yield语法，那这个函数就会变成生成器；

```python
def func():
    yield 1
    yield 2
    yield 3
    yield 4
```

上述代码中：func是函数称为生成器，当执行此函数func()时会得到一个迭代器。

```python
>>> temp = func()
>>> temp.__next__()
1
>>> temp.__next__()
2
>>> temp.__next__()
3
>>> temp.__next__()
4
>>> temp.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### 实践1-普通函数实现斐波拉契数列

```python
def fib(max):
    n, a, b = 0, 0, 1
    res = []
    while n < max:
        res.append(b)
        a, b = b, a + b
        n = n + 1
    return res
res = fib(6)
print(res)
for i in res:
    print(i)
    执行结果
[1, 1, 2, 3, 5, 8]
1
3
8
```


### 实践2-生成器实现斐波拉契数列


```python
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print(res)
for i in res:
    print(i)
    执行结果
<generator object fib2 at 0x000001EF306570F8>
1
3
8
```

可以看出返回的`<generator object fib2 at 0x000001EF306570F8> `是一个生成器对象，并且生成器内部的东西没有马上执行，而是执行到yield的时候就返回一个迭代器。


## 总结

迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件

特点：

访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
不能随机访问集合中的某个值 ，只能从头到尾依次访问
访问到一半时不能往回退
便于循环比较大的数据集合，节省内存


* 推导式有, 列表推导式, 字典推导式, 集合推导式, 没有元组推导式
* 生成器表达式: `(结果 for 变量量 in 可迭代对象 if 条件筛选)`
* 生成器表达式可以直接获取到⽣成器对象. ⽣成器对象可以直接进行for循环. ⽣成器具有惰性机制.
* 集合推导式和字典推导式很是类似,记住一个小技巧能够快速区分那个是字典那个是集合
* 字典推导式前面的结果是有个冒号,而集合的前面结果就是单纯的结果
