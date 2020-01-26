# -*- coding:utf8 -*- 
from flask import Flask
from flask_admin import Admin
from flask_admin import BaseView 
from flask_admin import expose
from flask import url_for, redirect, render_template, request
import json
import os

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='PonyTail', template_mode='bootstrap3')
# Add administrative views here


user = {
'username': 'Booboo Wei',
'bio': 'A girl who loves movies and music.',
}
movies = [
{'name': 'My Neighbor Totoro', 'year': '1988'},
{'name': 'Three Colours trilogy', 'year': '1993'},
{'name': 'Forrest Gump', 'year': '1994'},
{'name': 'Perfect Blue', 'year': '1997'},
{'name': 'The Matrix', 'year': '1999'},
{'name': 'Memento', 'year': '2000'},
{'name': 'The Bucket list', 'year': '2007'},
{'name': 'Black Swan', 'year': '2010'},
{'name': 'Gone Girl', 'year': '2014'},
{'name': 'CoCo', 'year': '2017'},
]

class Happy(BaseView):
    @expose('/')
    def index(self):
        return self.render('happy.html',user=user, movies=movies)

admin.add_view(Happy(name=u'关于我'))

class BodyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('bodyview.html')

admin.add_view(BodyView(name=u'时序数据展示'))




def get_telegraf_exec(**kwargs):
    body_dict = kwargs
    test_str = """echo 'body,name="booboowei" weight={weight},height={height},high_waistline={high_waistline},waistline={waistline},low_waistline={low_waistline},hipline={hipline},thigh_circumference={thigh_circumference},low_thigh_circumference={low_thigh_circumference},calf_circumference={calf_circumference}'
    """.format(
    weight=body_dict['weight'],
    height=body_dict['height'],
    high_waistline=body_dict['high_waistline'],
    waistline=body_dict['waistline'],
    low_waistline=body_dict['low_waistline'],
    hipline=body_dict['hipline'],
    thigh_circumference=body_dict['thigh_circumference'],
    low_thigh_circumference=body_dict['low_thigh_circumference'],
    calf_circumference=body_dict['calf_circumference'],
    )
    with open('/etc/telegraf/telegraf.d/test01.sh', 'w') as f:
        f.write(test_str)

    os.popen("systemctl restart telegraf")
    

class Body(BaseView):
    @expose('/', methods=('POST', 'GET'))
    def index(self):
        if request.method == 'POST':
            weight=request.form.get("weight")
            height=request.form.get("height")
            high_waistline=request.form.get("high_waistline")
            waistline=request.form.get("waistline")
            low_waistline=request.form.get("low_waistline")
            hipline=request.form.get("hipline")
            thigh_circumference=request.form.get("thigh_circumference")
            low_thigh_circumference=request.form.get("low_thigh_circumference")
            calf_circumference=request.form.get("calf_circumference")
            body_dict = {
                "weight":weight,
                "height":height,
                "high_waistline":high_waistline,
                "waistline":waistline,
                "low_waistline":low_waistline,
                "hipline":hipline,
                "thigh_circumference":thigh_circumference,
                "low_thigh_circumference":low_thigh_circumference,
                "calf_circumference":calf_circumference,
            }
            print(json.dumps(body_dict, indent=2))
            get_telegraf_exec(**body_dict)
        return self.render('body.html')

admin.add_view(Body(name=u'健康记录'))



app.run(debug=True,host='0.0.0.0',port=5000)
