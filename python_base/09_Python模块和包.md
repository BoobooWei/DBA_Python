<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [09_Python模块和包](#09python模块和包)
	- [模块(`Module`)的概念](#模块module的概念)
		- [模块的好处](#模块的好处)
		- [模块的种类](#模块的种类)
	- [模块导入方法](#模块导入方法)
		- [`import` 语句](#import-语句)
		- [`from…import` 语句](#fromimport-语句)
		- [`From … import *` 语句](#from-import-语句)
		- [运行本质](#运行本质)
	- [包(`Package`)](#包package)
		- [注意点（important）](#注意点important)
			- [第一点](#第一点)
			- [第二点](#第二点)
		- [第三点](#第三点)
	- [time模块](#time模块)
	- [参考](#参考)

<!-- /TOC -->

# 09_Python模块和包

## 模块(`Module`)的概念

在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个`.py`文件就称之为一个模块（`Module`）。

### 模块的好处

最大的好处是大大提高了代码的可维护性。

其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

### 模块的种类

* python标准库
* 第三方模块
* 应用程序自定义模块

注意：

1. 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
2. 但是也要注意，尽量不要与内置函数名字冲突。

## 模块导入方法

### `import` 语句

```python3
import module1[, module2[,... moduleN]
```

当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？答案就是解释器有自己的搜索路径，存在`sys.path`里。　　

```python3
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu',
'/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']　　
```

**因此若像我一样在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。**

### `from…import` 语句

```python3
from modname import name1[, name2[, ... nameN]]
```

这个声明不会把整个`modulename`模块导入到当前的命名空间中，只会将它里面的`name`1或`name2`单个引入到执行这个声明的模块的全局符号表。

### `From … import *` 语句


```python3
from modname import *
```

这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。

### 运行本质　

```python3
import test
from test import add　　
```

无论`1`还是`2`，首先通过`sys.path`找到`test.py`,然后执行`test`脚本（全部执行）;
区别是:
* `1`会将`test`这个变量名加载到名字空间
  * 而`2`只会将add这个变量名加载到名字空间　　

## 包(`Package`)

如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（`Package`）。

举个例子，一个`abc.py`的文件就是一个名字叫`abc`的模块，一个`xyz.py`的文件就是一个名字叫`xyz`的模块。

现在，假设我们的`abc`和`xyz`这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名：

引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，`view.py`模块的名字就变成了`hello_django.app01.views`，类似的，`manage.py`的模块名则是`hello_django.manage`。

请注意，每一个包目录下面都会有一个`__init__.p`y的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录(文件夹)，而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为`__init__.py`本身就是一个模块，而它的模块名就是对应包的名字。

调用包就是执行包下的`__init__.py`文件

### 注意点（important）


#### 第一点

手动将程序执行的路径加入`sys.path`

```python3
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import hello
hello.hello1()
```

#### 第二点

```python3
if __name__=='__main__':
    print('ok')
```

“Make a .py both importable and executable”

如果我们是直接执行某个`.py`文件的时候，该文件中那么`__name__ == '__main__'`是`True`,但是我们如果从另外一个`.py`文件通过`import`导入该文件的时候，这时`__name__`的值就是我们这个`py`文件的名字而不是`__main__`。

这个功能还有一个用处：调试代码的时候，在`if __name__ == '__main__'`中加入一些我们的调试代码，我们可以让外部模块调用的时候不执行我们的调试代码，但是如果我们想排查问题的时候，直接执行该模块文件，调试代码能够正常运行！

### 第三点

`/Users/yuanhao/Desktop/whaterver/project/web/module/cal.py`

```python3
def add(x,y):
    return x+y
```

`/Users/yuanhao/Desktop/whaterver/project/web/module/main.py`

```python3
import cal      #from module import cal

def main():

    cal.add(1,2)
```


`/Users/yuanhao/Desktop/whaterver/project/web/bin.py`

```python3
from module import main

main.main()
```


1. `from module import main` 改成 `from . import main`同样可以，这是因为`bin.py`是我们的执行脚本，`sys.path`里有`bin.py`的当前环境。即`/Users/yuanhao/Desktop/whaterver/project/web`这层路径，无论`import what` ,  解释器都会按这个路径找。
所以当执行到`main.py`时，`import cal`会找不到，因为`sys.path`里没有`/Users/yuanhao/Desktop/whaterver/project/web/module`这个路径，而`from  module/.  import cal` 时，解释器就可以找到了。

## time模块




## 参考

[参考文章](https://www.cnblogs.com/yuanchenqi/articles/5732581.html)
