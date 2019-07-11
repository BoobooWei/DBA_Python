<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [05_Python的文件操作](#05python的文件操作)
	- [文件处理模式](#文件处理模式)
		- [在python中的操作流程](#在python中的操作流程)
		- [`f=open('a.txt','r')`的过程分析](#fopenatxtr的过程分析)
		- [重点](#重点)
			- [回收文件资源](#回收文件资源)
			- [编码问题](#编码问题)
		- [python中的file与open](#python中的file与open)
			- [打开文件的模式](#打开文件的模式)
				- [常用模式](#常用模式)
			- [拓展模式](#拓展模式)
		- [了解U模式与换行符](#了解u模式与换行符)
			- [U模式](#u模式)
			- [总结](#总结)
	- [操作文件的方法](#操作文件的方法)
		- [需要掌握的方法](#需要掌握的方法)
- [了解](#了解)
	- [文件内光标移动](#文件内光标移动)
		- [文件内光标移动单位](#文件内光标移动单位)
		- [注意](#注意)
	- [习题](#习题)
		- [练习1：利用b模式编写一个cp工具](#练习1利用b模式编写一个cp工具)
		- [练习2：基于`seek()`实现`tail -f`功能](#练习2基于seek实现tail-f功能)
		- [练习3：文件的修改](#练习3文件的修改)
		- [方式一](#方式一)
		- [方式二](#方式二)
		- [练习4：计算](#练习4计算)
		- [练习4：替换修改文件内容](#练习4替换修改文件内容)

<!-- /TOC -->

# 05_Python的文件操作

> 参考
> * [博客](https://www.cnblogs.com/linhaifeng/articles/5984922.html)

## 文件处理模式

操作文件的流程：

1. 打开文件，得到文件句柄并赋值给一个变量
2. 通过句柄对文件进行操作
3. 关闭文件


### 在python中的操作流程

1. 打开文件，得到文件句柄并赋值给一个变量

```python
f = open('a.txt','r',encoding='utf-8')
```

默认打开模式就为`r`

2. 通过句柄对文件进行操作

```python
data=f.read()
```

3. 关闭文件
```python
f.close()
```

### `f=open('a.txt','r')`的过程分析

1. 由应用程序向操作系统发起系统调用open(...)

2. 操作系统打开该文件，并返回一个文件句柄给应用程序

3. 应用程序将文件句柄赋值给变量f

### 重点

#### 回收文件资源

打开一个文件包含两部分资源：操作系统级打开的文件+应用程序的变量。在操作完毕一个文件时，必须把与该文件的这两部分资源一个不落地回收，回收方法为：
1. `f.close()` 回收操作系统级打开的文件
2. `del f` 回收应用程序级的变量

其中`del f`一定要发生在`f.close()`之后，否则就会导致操作系统打开的文件还没有关闭，白白占用资源，**而python自动的垃圾回收机制决定了我们无需考虑`del f`，这就要求我们，在操作完毕文件后，一定要记住f.close()**

虽然我这么说，但是很多同学还是会很不要脸地忘记`f.close()``,对于这些不长脑子的同学，我们推荐傻瓜式操作方式：使用`with`关键字来帮我们管理上下文

```python
with open('a.txt','w') as f:
    pass

with open('a.txt','r') as read_f,open('b.txt','w') as write_f:
    data=read_f.read()
    write_f.write(data)
```

#### 编码问题

f=open(...)是由操作系统打开文件，那么如果我们没有为open指定编码，那么打开文件的默认编码很明显是操作系统说了算了，操作系统会用自己的默认编码去打开文件，在windows下是`gbk`，在linux下是`utf-8`。
这就用到了上节课讲的字符编码的知识：若要保证不乱码，`文件以什么方式存的，就要以什么方式打开`。

```python
f=open('a.txt','r',encoding='utf-8')
```

### python中的file与open

#### 打开文件的模式

`文件句柄 = open('文件路径', '模式')`

模式可以是以下方式以及他们之间的组合：

```python
Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newline mode (for backwards compatibility; should not be used in new code)
```

##### 常用模式

打开文件的模式有(默认为文本模式)

|模式|说明|
|:--|:--|
|r | 只读模式【默认模式，文件必须存在，不存在则抛出异常】|
|w | 只写模式【不可读；不存在则创建；存在则清空内容】|
|a | 之追加写模式【不可读；不存在则创建；存在则只追加内容】|

对于非文本文件，我们只能使用b模式，"b"表示以字节的方式操作（而所有文件也都是以字节的形式存储的，使用这种模式无需考虑文本文件的字符编码、图片文件的jgp格式、视频文件的avi格式）
* rb
* wb
* ab

注:
1. 以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码
2. linux中无需使用b，因为一切皆为文件，默认都是bits存放

#### 拓展模式

|模式|说明|
|:--|:--|
| + |表示可以同时读写某个文件|
| r+ |读写【可读，可写】|
| w+ |写读【可读，可写】|
| a+ |写读【可读，可写】|
| x |只写模式【不可读；不存在则创建，存在则报错】|
| x+ | 写读【可读，可写】|


### 了解U模式与换行符

[回车与换行的来龙去脉](http://www.cnblogs.com/linhaifeng/articles/8477592.html)

#### U模式

```python
'U' mode is deprecated and will raise an exception in future versions
of Python.  It has no effect in Python 3.  Use newline to control
universal newlines mode.
```

#### 总结

在python3中使用默认的newline=None即可，换行符无论何种平台统一用`\n`即可

## 操作文件的方法

### 需要掌握的方法

* f.read() 读取所有内容,光标移动到文件末尾
* f.readline() 读取一行内容,光标移动到第二行首部
* f.readlines() 读取每一行内容,存放于列表中

f.write('1111\n222\n') #针对文本模式的写,需要自己写换行符
f.write('1111\n222\n'.encode('utf-8')) #针对b模式的写,需要自己写换行符
f.writelines(['333\n','444\n']) #文件模式
f.writelines([bytes('333\n',encoding='utf-8'),'444\n'.encode('utf-8')]) #b模式

#了解
f.readable() #文件是否可读
f.writable() #文件是否可读
f.closed #文件是否关闭
f.encoding #如果文件打开模式为b,则没有该属性
f.flush() #立刻将文件内容从内存刷到硬盘
f.name

## 文件内光标移动

### 文件内光标移动单位

* 字符为单位：如打开为文本模式时，`read(3)`代表读取3个字符
* 字节为单位：其他如`seek()`，`tell()`，`truncate()`

### 注意

1. `seek()`有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
2. `truncate()`是截断文件，所以文件的打开方式必须可写，但是不能用`w`或`w+`等方式打开，因为那样直接清空文件了，所以要在`r+`或`a`或`a+`等模式下测试效果

## 习题

### 练习1：利用b模式编写一个cp工具

要求如下：
1. 既可以拷贝文本又可以拷贝视频，图片等文件
2. 用户一旦参数错误，打印命令的正确使用方法，如`usage: cp source_file target_file`

提示：可以用`import sys`，然后用`sys.argv`获取脚本后面跟的参数

```python
import sys
if len(sys.argv) != 3:
    print('usage: cp source_file target_file')
    sys.exit()

source_file,target_file=sys.argv[1],sys.argv[2]
with open(source_file,'rb') as read_f,open(target_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)
        ```
### 练习2：基于`seek()`实现`tail -f`功能

```python
import time
with open('test.txt','rb') as f:
    f.seek(0,2)
    while True:
        line=f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)
```


### 练习3：文件的修改

文件的数据是存放于硬盘上的，因而只存在覆盖、不存在修改这么一说，我们平时看到的修改文件，都是模拟出来的效果，具体的说有两种实现方式：

### 方式一

将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）


```python
import os

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    data=read_f.read() #全部读入内存,如果文件很大,会很卡
    data=data.replace('alex','SB') #在内存中完成修改

    write_f.write(data) #一次性写入新文件

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')
```

### 方式二

将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件


```python
import os

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('alex','SB')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')
```

### 练习4：计算

文件a.txt内容为：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数。

  ```shell
  apple 10 3
  tesla 100000 1
  mac 3000 2
  lenovo 30000 3
  chicken 10 3
  ```

### 练习4：替换修改文件内容

把文件中的alex都替换成SB。
