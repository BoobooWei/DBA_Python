# 12-修改Flask_admin前端页面添加表格名称

> 2020-03-11 BoobooWei

[TOC]

## 效果图

略

## 代码说明

页面表格一行显示，文字不换行

修改 `/usr/lib/python2.7/site-packages/flask_admin/templates/bootstrap3/admin/model/list.html`文件

```html
{% block body %}
-- 在block body下面添加以下代码
    <div class="panel panel-default">
        <div class="panel-body">
            {% block title %}{% if admin_view.category %}{{ admin_view.category }} - {% endif %}{{ admin_view.name }}{% endblock %}
        {% block model_menu_bar %}
        </div>
    </div>

```

* `admin_view.category`: 当前页面所属的目录和名称
* `admin_view.name`: PonyTail


```python
admin = Admin(app, name='PonyTail', index_view=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap3')
```


## 操作指南
