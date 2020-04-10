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

# 3rd-part Modules
from jinja2 import Template


class GetMarkdown:
    def __init__(self, **kwargs):
        self.provider = kwargs['provider']
        self.check_script = kwargs['check_script']
        self.check_name = kwargs['check_name']
        self.seq = kwargs['seq']

    def render_template(self, TEMPLATE_DIR):
        with codecs.open(TEMPLATE_DIR + '/' + 'template_markdown.md', 'r', 'utf-8') as f:
            template_data = f.read()
            template = Template(template_data)

            render_data = {
                'check_name': self.check_name,
                'check_script': self.check_script,
                'provider': self.provider,
                'seq': self.seq,
            }

            return template.render(**render_data)

    def maker(self, template_dir, output_file_dir):
        with codecs.open(os.path.join(output_file_dir,'{0}.md'.format(self.check_script)), 'w', 'utf-8') as f:
            f.write(self.render_template(template_dir))


if __name__ == '__main__':
    print("output markdown file")

    params_list = [{
        "check_name": 'cc',
        "check_script": 'aa',
        "provider": 'aliyun',
        "seq": ['a', 'b', 'c'],
    }]
    for params in params_list:
        api = GetMarkdown(**params)
        template_dir = "./templates"
        output_file_dir = "./README"
        api.maker(template_dir, output_file_dir)
