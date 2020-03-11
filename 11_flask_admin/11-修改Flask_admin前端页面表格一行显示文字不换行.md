# 11-修改Flask_admin前端页面表格一行显示文字不换行

> 2020-03-11 BoobooWei

[TOC]

## 效果图

略

## 代码说明

页面表格一行显示，文字不换行

修改 `/usr/lib/python2.7/site-packages/flask_admin/templates/bootstrap3/admin/model/list.html`文件

```html
   <table class="table table-striped table-bordered table-hover model-list" 
   <table class="table table-striped table-bordered table-hover model-list" style="white-space:nowrap">
```

`style="white-space:nowrap"`: 代表文字不自动换行

## 操作指南

### 找到flask_admin使用的前端模版路径

通过查看`sys.path`找到要修改的页面所在目录

`/Users/booboowei/python_project/fms/venv/lib/python2.7/site-packages/flask_admin/templates/bootstrap3/admin`

```bash
(venv) 02:24 PM :fms booboowei$ python
Python 2.7.10 (default, Aug 17 2018, 19:45:58) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import sys
>>> sys.path
['', '/Users/booboowei/python_project/fms/venv/lib/python27.zip', '/Users/booboowei/python_project/fms/venv/lib/python2.7', '/Users/booboowei/python_project/fms/venv/lib/python2.7/plat-darwin', '/Users/booboowei/python_project/fms/venv/lib/python2.7/plat-mac', '/Users/booboowei/python_project/fms/venv/lib/python2.7/plat-mac/lib-scriptpackages', '/Users/booboowei/python_project/fms/venv/lib/python2.7/lib-tk', '/Users/booboowei/python_project/fms/venv/lib/python2.7/lib-old', '/Users/booboowei/python_project/fms/venv/lib/python2.7/lib-dynload', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/Users/booboowei/python_project/fms/venv/lib/python2.7/site-packages']
(venv) 02:28 PM :templates booboowei$ cd /Users/booboowei/python_project/fms/venv/lib/python2.7/site-packages/flask_admin/templates/bootstrap3/admin
(venv) 02:29 PM :admin booboowei$ ll
total 80
-rw-r--r--   1 booboowei  staff   1.4K Mar 11 14:16 actions.html
-rw-r--r--   1 booboowei  staff   3.9K Mar 11 14:16 base.html
drwxr-xr-x   5 booboowei  staff   160B Mar 11 14:16 file
-rw-r--r--   1 booboowei  staff    67B Mar 11 14:16 index.html
-rw-r--r--   1 booboowei  staff   4.0K Mar 11 14:16 layout.html
-rw-r--r--   1 booboowei  staff   8.5K Mar 11 14:16 lib.html
-rw-r--r--   1 booboowei  staff    34B Mar 11 14:16 master.html
drwxr-xr-x  12 booboowei  staff   384B Mar 11 14:16 model
drwxr-xr-x   4 booboowei  staff   128B Mar 11 14:16 rediscli
-rw-r--r--   1 booboowei  staff    89B Mar 11 14:16 static.html
```


### 修改页面`model/list.html`

```bash
(venv) 02:29 PM :admin booboowei$ cd model/
(venv) 02:30 PM :model booboowei$ ll
total 88
-rw-r--r--  1 booboowei  staff   705B Mar 11 14:16 create.html
-rw-r--r--  1 booboowei  staff   1.4K Mar 11 14:16 details.html
-rw-r--r--  1 booboowei  staff   1.0K Mar 11 14:16 edit.html
-rw-r--r--  1 booboowei  staff   410B Mar 11 14:16 inline_field_list.html
-rw-r--r--  1 booboowei  staff   153B Mar 11 14:16 inline_form.html
-rw-r--r--  1 booboowei  staff   2.2K Mar 11 14:16 inline_list_base.html
-rw-r--r--  1 booboowei  staff   4.0K Mar 11 14:16 layout.html
-rwxr-xr-x  1 booboowei  staff   7.4K Mar 11 14:16 list.html
drwxr-xr-x  5 booboowei  staff   160B Mar 11 14:16 modals
-rw-r--r--  1 booboowei  staff   1.7K Mar 11 14:16 row_actions.html

```