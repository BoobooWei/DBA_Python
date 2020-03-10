# -*- coding:utf8 -*-

from flask_admin import expose
from flask_admin import BaseView
from flask_admin.contrib.sqla import ModelView
from wtforms import form, fields, validators
from wtforms.fields import SelectField
from wtforms.validators import DataRequired
import flask_login as login


# Add administrative views here
class Happy(BaseView):
    @expose('/')
    def index(self):
        return self.render('happy.html')

class Birthday(BaseView):
    @expose('/')
    def index(self):
        return self.render('birthday.html')





# Create customized model view class

class MyBaseView(ModelView):
    #can_delete = False
    can_view_details = True

    def is_accessible(self):
        return login.current_user.is_authenticated

    #不显示的列
    column_exclude_list = ['uuid','update_time','is_deleted','delete_time']
    
    

class MyModelView(MyBaseView):
    column_labels = {
        'login':u'用户名'
    }
    column_sortable_list = ('login',)
    column_searchable_list = ('login',)
    # 09_展示界面添加过滤框
    column_filters = ('login',)


class MyV_Event(MyBaseView):
    column_labels = {
        'event':u'事件描述',
        'state':u'事件状态',
        'projects.name':u'所属项目',
        'event_type.type_name':u'事件类型',
        'product_type.product_name':u'产品类型',
        'kitchen_url':u'kitchen URL',
        'create_time':u'创建时间'
    }
    # 指定可排序的列
    column_sortable_list = ('state','kitchen_url','create_time')
    column_searchable_list = ('event',)
    column_filters = ('event', 'state', 'projects.name', 'event_type.type_name', 'product_type.product_name', 'create_time')
    # 插入修改列名
    form_args = dict(
        event=dict(label=u'事件描述', validators=[DataRequired()]),
        state=dict(label=u'事件状态', validators=[DataRequired()],),
        project_id=dict(label=u'所属项目', validators=[DataRequired()]),
        event_type_id=dict(label=u'事件类型', validators=[DataRequired()]),
        product_type_id=dict(label=u'产品类型', validators=[DataRequired()]),
        kitchen_url=dict(label=u'kitchen URL'),
        create_time=dict(label=u'创建时间', validators=[DataRequired()])
    )
    # 下拉框选择
    form_choices = {
        'state': [
            (u'进行中', u'进行中'),
            (u'阻塞-客观原因', u'阻塞-客观原因'),
            (u'阻塞-主观原因', u'阻塞-主观原因'),
            (u'完成', u'完成') 
        ]
    }
    # 导出
    column_export_list = ['event']

    #不创建也不编辑的列
    form_excluded_columns = ['userprocesslists','uuid','update_time','is_deleted','delete_time']

class MyV_UserProcesslist(MyBaseView):
    column_labels = {
        'users.name':u'事件处理者',
        'events.event':u'事件描述',
        'info':u'跟进描述',
        'create_time':u'创建时间'
    }
    # 指定可排序的列
    column_sortable_list = ('users.name','events.event','create_time')
    column_searchable_list = ('users.name',)
    column_filters = ('users.name', 'events.event', 'create_time', 'info')
    #不创建也不编辑的列
    form_excluded_columns = ['uuid','update_time','is_deleted','delete_time']

class MyV_EventType(MyBaseView):
    column_labels = {
        'id':u'序号',
        'type_name':u'事件类型',
        'category_id':u'事件分类',
        'tec_id':u'技术分类'
    }
    # 指定可排序的列
    column_sortable_list = ('type_name','category_id','tec_id')
    column_searchable_list = ('type_name',)
    column_filters = ('type_name','category_id','tec_id')
    #不创建也不编辑的列
    form_excluded_columns = ['events','uuid','update_time','is_deleted','delete_time']


class MyV_ProductType(MyBaseView):
    column_labels = {
        'id':u'序号',
        'product_name':u'产品名称',
        'category_id':u'产品所属技术分类',
        'platform_id':u'产品所属平台分类',
    }
    # 指定可排序的列
    column_sortable_list = ('product_name','category_id','platform_id')
    column_searchable_list = ('product_name',)
    column_filters =  ('product_name','category_id','platform_id')
    #不创建也不编辑的列
    form_excluded_columns = ['events','uuid','update_time','is_deleted','delete_time']

