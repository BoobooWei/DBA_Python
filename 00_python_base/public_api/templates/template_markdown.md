# 云提供商

{{ provider }}

# 检测项

* 检测项名称：{{ check_name }}
* 检测项英文名：{{ check_script }}

# 案例说明

{% for item in seq -%}
    {{ item }}
{%- endfor %}


{% for item in seq -%}
    {{ item }}
{% endfor %}