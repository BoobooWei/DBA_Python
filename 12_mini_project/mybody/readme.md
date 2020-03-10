# Readme

## 简介

身体健康值记录的web系统源代码

## 前提和依赖

* python3.7

* influxdb1.7

* telegraf 1.12

1. 安装tick

   ```bash
   https://github.com/BoobooWei/booboo_TimeSeriesDBMS/blob/master/scripts/auto_install_influxdb1.7.sh
   ```

   

2. telegraf配置文件

   ```bash
   [root@oracle01 telegraf.d]# cat exec.conf 
   [[inputs.exec]]
       commands = [
         "/bin/bash /etc/telegraf/telegraf.d/test01.sh",
       ]
       interval = "60s"
       timeout = "5s"
       data_format = "influx"
   ```

   

后续，开发一个钉钉小程序，记录。