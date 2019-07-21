
# 08_Python装饰器

## 装饰器基本理论

装饰器：
* 本质:`函数`
* 功能:`为其他函数添加附加功能`

原则：
1. 不修改被修饰函数的源代码
2. 不修改被修饰函数的调用方式

`装饰器 = 高阶函数 + 函数嵌套 + 闭包`


### 实践1-计算函数执行耗时

```python
import time
def time_count(func):
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

闭包：在一个作用域里放入定义


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

### 函数闭包加上认证功能

### 函数闭包模拟session

## 函数闭包展示器运行流程

## 函数闭包待参数装饰器
