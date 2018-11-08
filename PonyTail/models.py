# -*- coding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from uuid import uuid4
from time import time
from flask_admin import expose
from flask import url_for, redirect, render_template, request
from wtforms import form, fields, validators
import flask_admin as admin
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers
from werkzeug.security import generate_password_hash, check_password_hash


def uuid():
    return uuid4().hex

db = SQLAlchemy()

class Shadow(db.Model):
    __tablename__ = 'shadow'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))
    create_time = db.Column(db.BigInteger,default=int(time()), comment='创建时间戳')
    update_time = db.Column(db.BigInteger,default=int(time()), comment='修改时间戳')
    is_deleted = db.Column(db.SmallInteger, comment='是否被删除')
    delete_time = db.Column(db.BigInteger, comment='删除时间戳')
    uuid = db.Column(db.String(32), default=uuid, comment='UUID')

    # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

class User(db.Model ):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), comment='邮件地址', unique=True)
    username = db.Column(db.String(64), comment='用户名')
    name = db.Column(db.String(64), default='',comment='真实姓名')
    nickname = db.Column(db.String(32), comment='花名')
    location = db.Column(db.String(64), comment='地址')
    mobile = db.Column(db.String(11), comment='手机号码')
    ding_talk = db.Column(db.String(32), comment='钉钉号码')
    source = db.Column(db.String(32), comment='账号来源(CC, LDAP)')
    position = db.Column(db.String(32), comment='工作职位')
    last_seen = db.Column(db.BigInteger, comment='最后一次登录时间')
    last_login_ip = db.Column(db.String(20), comment='最后一次登录IP')
    login_count = db.Column(db.Integer, default=0, comment='用户登录次数')
    is_admin = db.Column(db.Boolean, default=False, comment='是否管理员')
    is_locked = db.Column(db.Boolean, default=False, comment='是否锁定')
    is_deleted = db.Column(db.Boolean, default=False, comment='是否删除')
    unique_id = db.Column(db.String(64), unique=True)
    uuid = db.Column(db.String(32), unique=True, index=True, default=uuid, comment='UUID')
    remarks = db.Column(db.Text, comment='备注')
    creator_id = db.Column(db.String(32), comment='创建人')
    modifier_id = db.Column(db.String(32), comment='修改人')
    create_time = db.Column(db.BigInteger, default=int(time()), comment='创建时间')
    update_time = db.Column(db.BigInteger, default=int(time()), comment='修改时间')
    delete_time = db.Column(db.BigInteger, comment='删除时间')

    userprocesslists = db.relationship("UserProcesslist", backref="users")
    def __repr__(self):
        return self.name



 
class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), comment='项目名称')
    customer_id = db.Column(db.String(32), comment='客户ID')
    manager_id = db.Column(db.String(32), comment='项目经理')
    architect_id = db.Column(db.String(32), comment='架构师')
    operator_id = db.Column(db.String(32), comment='运维人员')
    consumer_id = db.Column(db.String(32), comment='客户联系人')
    sales_id = db.Column(db.String(32), comment='销售')
    status = db.Column(db.String(32), comment='项目状态')
    begin_time = db.Column(db.BigInteger, comment='项目开始时间')
    end_time = db.Column(db.BigInteger, comment='项目结束时间')
    sensitivity_level = db.Column(db.Integer, default=19, comment='客户敏感安全度等级')
    create_time = db.Column(db.BigInteger, default=int(time()), comment='创建时间')
    update_time = db.Column(db.BigInteger, default=int(time()), comment='修改时间')
    delete_time = db.Column(db.BigInteger, comment='删除时间')
    creator_id = db.Column(db.String(32), comment='创建人')
    modifier_id = db.Column(db.String(32), comment='修改人')
    is_deleted = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(32), unique=True, index=True, default=uuid)
    remarks = db.Column(db.Text, comment='备注')

    events = db.relationship("Event", backref="projects")
    def __repr__(self):
        return self.name

class EventType(db.Model):
    __tablename__ = 'event_type'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(64), comment='事件类型')
    category_id = db.Column(db.String(32), comment='技术分类 0 数据库 1 网络 2 安全')
    tec_id = db.Column(db.String(32), comment='事件分类 0 咨询类 1 实施类 2 故障类 3 优化类')
    create_time = db.Column(db.BigInteger,default=int(time()), comment='创建时间戳')
    update_time = db.Column(db.BigInteger,default=int(time()), comment='修改时间戳')
    is_deleted = db.Column(db.SmallInteger, comment='是否被删除')
    delete_time = db.Column(db.BigInteger, comment='删除时间戳')
    uuid = db.Column(db.String(32), default=uuid, unique=True, comment='UUID')

    events = db.relationship("Event", backref="event_type")
    def __repr__(self):
        return self.type_name

class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), comment='产品名称')
    category_id = db.Column(db.String(32), comment='产品所属技术分类 0 数据库 1 网络 2 安全')
    platform_id = db.Column(db.String(32), comment='产品所属平台分类 0 本地 1 阿里云 2 亚马逊云 3 腾讯云 4 华为云')
    uuid = db.Column(db.String(32), default=uuid, comment='UUID')
    create_time = db.Column(db.BigInteger,default=int(time()), comment='创建时间戳')
    update_time = db.Column(db.BigInteger,default=int(time()), comment='修改时间戳')
    is_deleted = db.Column(db.SmallInteger, comment='是否被删除')
    delete_time = db.Column(db.BigInteger, comment='删除时间戳')

    events = db.relationship("Event", backref="product_type")
    def __repr__(self):
        return self.product_name

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255), comment='事件')
    state = db.Column(db.String(32), comment='事件状态 0 进行中 1 阻塞-客观原因 2 阻塞-主观原因 3 完成')
    project_id = db.Column(db.String(32), comment='项目uuid')
    event_type_id = db.Column(db.String(32), comment='事件类型id')
    product_type_id = db.Column(db.String(32), comment='产品类型id')
    kitchen_url = db.Column(db.String(255), comment='kitchen URL连接')
    uuid = db.Column(db.String(32), default=uuid, comment='UUID')
    create_time = db.Column(db.BigInteger,default=int(time()), comment='创建时间戳')
    update_time = db.Column(db.BigInteger,default=int(time()), comment='修改时间戳')
    is_deleted = db.Column(db.SmallInteger, comment='是否被删除')
    delete_time = db.Column(db.BigInteger, comment='删除时间戳')
    project_id = db.Column(db.String(32), db.ForeignKey('projects.uuid'))
    event_type_id = db.Column(db.String(32), db.ForeignKey('event_type.uuid'))
    product_type_id = db.Column(db.String(32), db.ForeignKey('product_type.uuid'))
    
    userprocesslists = db.relationship("UserProcesslist", backref="events")
    def __repr__(self):
        return self.event




class UserProcesslist(db.Model):
    __tablename__ = 'user_processlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), comment='事件处理者id')
    event_id = db.Column(db.String(32), comment='事件id')
    info = db.Column(db.Text, comment='描述')
    create_time = db.Column(db.BigInteger,default=int(time()), comment='创建时间戳')
    update_time = db.Column(db.BigInteger,default=int(time()), comment='修改时间戳')
    is_deleted = db.Column(db.SmallInteger, comment='是否被删除')
    delete_time = db.Column(db.BigInteger, comment='删除时间戳')
    uuid = db.Column(db.String(32), default=uuid, comment='UUID')
    event_id = db.Column(db.String(32), db.ForeignKey('events.uuid'))
    user_id = db.Column(db.String(32), db.ForeignKey('users.uuid'))




# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])
    #password = fields.StringField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        #if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(Shadow).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(Shadow).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(Shadow).get(user_id)

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = Shadow()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            #user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

