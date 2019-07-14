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

既然通过索引可以遍历列表中所有的元素，为什么

## 三元运算

## 列表解析

## 生成器表达式