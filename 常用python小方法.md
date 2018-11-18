# 常用小方法

[TOC]

## 去除网页标签

```python
import re
import sys

a_string="""
<div>
    
    <p>【背景】 客户采购我司CMS服务，请协调对接人</p>
    
    
    <p>【希望驻云做什么】 客户采购我司CMS服务，请协调对接人</p>
    
    
    <p>【期望完成时间】 2018/10/31 12:00</p>
    
    
      <p>【是否需要上门】 否</p>
      
    

    
      <p>【联系人】 刘茂鹏</p>
    
    
      <p>【联系方式】 1</p>
    
</div>"""

a = re.sub(r'</?(div|p)>','',a_string)
b = []
for i in a.split('\n'):
    if i.strip() != '':
        b.append(i.strip())
print('\n'.join(b))


背景】 客户采购我司CMS服务，请协调对接人
【希望驻云做什么】 客户采购我司CMS服务，请协调对接人
【期望完成时间】 2018/10/31 12:00
【是否需要上门】 否
【联系人】 刘茂鹏
【联系方式】 1
```


## 生产依赖包

```bash
pip freeze > requirements.txt
```
