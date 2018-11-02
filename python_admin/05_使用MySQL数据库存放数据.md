# 05_使用MySQL数据库存放数据

> 2018-11-02 大宝



## 1. 安装MySQL数据库

> 使用root用户安装

```shell
yum install -y mariadb-server
systemctl start mariadb
```

## 2. 创建数据库myweb

```bash
mysql -e "create database myweb"
```

## 3. 添加应用程序授权

修改root密码，应用程序将使用本地root用户的权限。如果你熟悉数据库，可以将新建一个小权限的数据库用户。

```bash
mysqladmin -uroot password 'myweb'
```

## 4. 新建用户表

用户表用来保存系统登陆用户信息，包括用户名和密码。

```bash
mysql -uroot -pmyweb myweb -e "create table AdminUser (id int primary key auto_increment, name varchar(255) not null ,password varchar(255) not null)"
```

## 5. 插入用户和密码信息

手动插入两条记录

```bash
mysql -uroot -pmyweb myweb -e "insert into AdminUser values (null,'zyadmin','123'),(null,'booboo','123')"
```

## 6. 查看表中的信息

```bash
mysql -uroot -pmyweb myweb -e "select * from AdminUser"
```

## 7. 操作指南

```bash
[root@am_01 ~]# yum install -y mariadb-server
[root@am_01 ~]# systemctl start mariadb
[root@am_01 ~]# mysql -e "create database myweb"
[root@am_01 ~]# mysql -uroot -pmyweb -e 'show databases'
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| myweb              |
| performance_schema |
| test               |
+--------------------+
[root@am_01 ~]# mysql -uroot -pmyweb myweb -e "create table AdminUser (id int primary key auto_increment, name varchar(255) not null ,password varchar(255) not null)"
[root@am_01 ~]# mysql -uroot -pmyweb myweb -e "insert into AdminUser values (null,'zyadmin','123'),(null,'booboo','123')"
[root@am_01 ~]# mysql -uroot -pmyweb myweb -e "select * from AdminUser"
+----+---------+----------+
| id | name    | password |
+----+---------+----------+
|  1 | zyadmin | 123      |
|  2 | booboo  | 123      |
+----+---------+----------+
```

## 8. 准备好应用连接数据库的信息

* 用户名： `root`
* 密码： `myweb`
* 数据库地址： `127.0.0.1`
* 监听端口：`3360`
* 连接数据库：`myweb`
* 表名：`AdminUser`

```python
DATABASE_NAME='myweb'
DATABASE_HOST='127.0.0.1'
DATABASE_USER='root'
DATABASE_PORT='3306'
DATABASE_PASSWORD='myweb'
```