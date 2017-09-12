# 教程之入坑解围记录
## Requests模块
### 安装
requests模块早已安装完毕  
如果需要安装输入`pip install requests`

### 使用
在网上搜到了requests模块实例，就在文件夹中新建了一个requests.py文件并将实例输入。  
运行报错`AttributeError: module 'requests' has no attribute 'get' `
搜索后网师告知有两种可能：文件名重复或者重装。  
使用`pip install requests -U`重装后依然报错，将文件名修改为`requests test.py`。  
这时报错也改为`python: can't open file 'requests.py': [Errno 2] No such file or directory`。继续搜索发现有可能是因为文件名有空格导致报错，修改文件名为`requests_test.py`运行正常。

### 总结
命名需谨慎。
