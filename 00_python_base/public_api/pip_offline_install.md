# pip 离线安装

1. 首先，在项目中分析出所有依赖的库

  ```python
  pip3 freeze > requirements.txt
  ```

2. 将所有包下载到DIR这个目录中

  ```python
  pip3 download -d DIR -r requirements.txt
  ```

  > 切记，不要在 windows 下载包，然后放到 Linux 上进行安装，这样八成装不上

3. 将文件打包后放到离线服务器上，并进行解压缩

  ```bash
  pip3 install --no-index --find-links=DIR -r requirements.txt
  ```

  

命令说明

  * freeze 将依赖关系分析出来并 使用管道符导入到该文件中
  * download 分析 requirements 文件，将所有包进行下载，通过 d 选项导入 DIR 文件夹
  * --find-links 指定离线安装的文件夹DIR，也就是你下载好的包
  * 注意: --no-index 必须搭配 --find-links 使用
  * --no-index Ignore package index (only looking at --find-links URLs instead).


