# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.19.01.15.0
Description:
Help:
"""
# Build-in Modules
import os
import codecs
import pathlib

# 3rd-part Modules
from jinja2 import Template


class GetMarkdown:
    def __init__(self, **kwargs):
        self.render_data = kwargs

    def render_template(self):
        template_data = """
# 客户名

{{ customer }}

# 检测报告

* 名称：{{ check_name }}
* 时间：{{ check_time }}

# 报告明细

{% for item in sql_data -%}
    {{ item }}
{%- endfor %}  

{% for item in sql_data -%}
    {{ item }}
{% endfor %} 


{% for item in sql_data %}
    {{ item }}
{%- endfor %} 


{% for item in sql_data %}
    {{ item }}
{% endfor %}     
"""
        template = Template(template_data)
        return template.render(**self.render_data)

    def maker(self, output_dir):
        with codecs.open(os.path.join(output_dir, '{0}.md'.format(self.render_data['customer'])), 'w',
                         'utf-8') as f:
            f.write(self.render_template())


if __name__ == '__main__':
    print("output markdown file")

    params_list = [{
        "customer": '老板电器',
        "check_name": '库表统计',
        "check_time": '2020-04-05 11:00:09',
        "sql_data": ['a', 'b', 'c'],
    }, {
        "customer": 'AIA',
        "check_name": '库表统计',
        "check_time": '2020-04-05 11:00:09',
        "sql_data": ['e', 'f', 'g'],
    }
    ]

    for params in params_list:
        api = GetMarkdown(**params)
        output_dir = "./README/"
        if not pathlib.Path(output_dir).exists():
            os.mkdir(output_dir)
        api.maker(output_dir)
