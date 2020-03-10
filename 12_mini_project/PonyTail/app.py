# -*- coding:utf8 -*-

from config import DevConfig
from flask import Flask
from flask_admin import Admin
from flask_admin import BaseView
from flask_admin import expose
from flask_babelex import Babel
from flask_admin.contrib.sqla import ModelView
from flask import url_for, redirect, render_template, request
from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_admin import helpers
from werkzeug.security import generate_password_hash, check_password_hash


import models
import views 


db = models.db
app = Flask(__name__)
app.config.from_object(DevConfig)
babel = Babel(app)
db.init_app(app)


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
models.init_login(app)

admin = Admin(app, name='PonyTail', index_view=models.MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap3')
admin.add_view(views.Happy(name=u'Happy', category = u'工作之愉'))
admin.add_view(views.Birthday(name='Birthday', category = u'工作之愉'))

admin.add_view(views.MyV_Event(models.Event, db.session, name=u'事件管理',category=u'工作管理'))
admin.add_view(views.MyV_UserProcesslist(models.UserProcesslist, db.session, name=u'工作记录管理',category=u'工作管理'))
admin.add_view(views.MyV_EventType(models.EventType, db.session, name=u'事件类型管理', category=u'分类管理'))
admin.add_view(views.MyV_ProductType(models.ProductType, db.session, name=u'产品类型管理', category=u'分类管理'))
admin.add_view(views.MyModelView(models.Shadow,db.session,name=u'账号管理'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)  


