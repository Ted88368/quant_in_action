## ZVT快速入门


#### 系统
+ Windows成功
+ Linux未测试
+ MacOS未测试

#### 安装
```shell

# 标准安装作为对比项
conda create -n zvt python=3.9
conda activate zvt
python -m pip install -U zvt==0.12.1

# 或者源码编译
conda create -n zvt_dev python=3.9
conda activate zvt_dev

pip install -r requirements.txt
pip install numpy==1.23 xtquant nbformat
python -m pip install -U .

# 安装路径在 C:\Users\huzhe\.conda\envs\py38\Scripts
``` 

#### 配置
##### 数据下载
+ [下载地址](https://drive.google.com/drive/folders/17Bxijq-PHJYrLDpyvFAm5P6QyhKL-ahn)
+ 配置， 根据默认配置放置数据，然后解压即可
    ```json
     {'data_path': 'C:\\Users\\huzhe\\zvt-home\\data',
        'log_path': 'C:\\Users\\huzhe\\zvt-home\\logs',
        'resource_path': 'C:\\Users\\huzhe\\zvt-home\\resources',
        'tmp_path': 'C:\\Users\\huzhe\\zvt-home\\tmp',
        'ui_path': 'C:\\Users\\huzhe\\zvt-home\\ui',
        'zvt_home': 'C:\\Users\\huzhe\\zvt-home'}
    ```
    
    
    
#### 运行
```shell
zvt
# C:\Users\huzhe\.conda\envs\py38\Scripts\zvt.exe

zvt/src/zvt/main.py
```

#### WebUI
```shell
pip install PyYAML
pip install uvicorn
zvt_server

https://github.com/Ted88368/zvt_ui.git
```

### 数据说明
#### sina



### 参考文档
+ [《zvt》](https://zvt.readthedocs.io/en/latest/)