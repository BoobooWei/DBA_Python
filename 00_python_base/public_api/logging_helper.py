# -*- coding: utf-8 -*-

# Build-in Modules
import logging.config
import os

# 3rd-part Modules
import yaml

base_path = os.path.abspath(os.path.dirname(__file__))


def set_logging():
    """配置脚本日志输出格式"""

    # 检查是否存在 日志 存放的目录
    if not os.path.exists(base_path + '/logs'):
        os.mkdir(base_path + '/logs')

    # 检查配置文件是否存在
    config_dir = base_path + '/log_conf.yaml'
    if not os.path.exists(config_dir):
        raise FileNotFoundError('log_conf.yaml not found')

    # 读取配置文件
    with open(config_dir, 'r') as f:
        config = yaml.safe_load(f.read())

    if config:
        # 设置默认配置日志文件位置 默认位置为：/tmp/debug.log && /tmp/warning.log
        if not config.get('handlers').get('debug_file_handler').get('filename'):
            config['handlers']['debug_file_handler']['filename'] = '/tmp/debug.log'
        if not config.get('handlers').get('warning_file_handler').get('filename'):
            config['handlers']['warning_file_handler']['filename'] = '/tmp/warning.log'

        # 配置文件载入 logging 模块
        logging.config.dictConfig(config=config)
    else:
        raise IOError("config.yaml file doesn't exist")

    return logging


app_logging = set_logging()
app_logging.debug("DescribeMetricList ")
app_logging.info("DescribeMetricList ")
app_logging.warning("DescribeMetricList ")
app_logging.error("DescribeMetricList ")
