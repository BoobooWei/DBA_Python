# DBA_Python

## 说明

这是个人的Python学习笔记，高阶。

|目录|说明|
|:--|:--|
|[00_python_base](00_python_base)|Python 基本功进阶版|
|[01_python_net](01_python_net)|Python 网络开发|
|[02_python_threads](02_python_threads)|Python 并发编程|
|[11_flask_admin](11_flask_admin)|Flask_admin手把手搭建Web网站|
|[12_mini_project](12_mini_project)|该目录中保存了一些迷你小项目的源代码|

## 常用bash命令

> 用于快速生成Readme中文件链接

```bash
ll | awk '{print $9}'| grep md | awk -F'.' '{print $1}'|awk '{print "["$1"]("$1".md)\n"}'
```

