## 学习hikyuu


### 直接安装
#### Windows

```shell
# 安装路径
#C:\Users\huzhe\.conda\envs\hikyuu

conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/
conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/free/


# conda env remove --name hikyuu
conda create --name hikyuu python=3.10.13

# 安装好后，使用activate激活某个环境 
# conda init powershell 解决activate无法使用的问题
conda activate hikyuu 
# conda activate hikyuu_dev 自己编译版本


conda install pip
# pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ 

# https://github.com/TA-Lib/ta-lib/releases/tag/v0.4.0
pip install ..\TA_Lib-0.4.32-cp310-cp310-win_amd64.whl
python -m pip install TA-Lib

pip install hikyuu
# conda install hikyuu # 找不到的
conda install jupyter_server jupyter notebook

# 运行
jupyter notebook
```
#### Linux
+ [《编译安装》](./编译安装.md) WSL有问题

### 使用
#### 数据导入
+ [下载数据](https://hikyuu.readthedocs.io/zh_CN/latest/quickstart.html#id2)
    ```shell
    # 由于 importdata 命令使用的是 HikyuuTDX 生成的配置文件，所以在第一次执行 importdata 之前需要至少运行过一次 HikyuuTDX。
    # 路径 ~\.hikyuu


    配置好了关掉界面，用importdata
    importdata 
    ```

#### 例子选择
https://nbviewer.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True



### 参考资料
+ [《Hikyuu Quant Framework 文档》](https://hikyuu.readthedocs.io/zh-cn/latest/index.html)
+ [《talib库windows下安装》](https://zhijinyu.com/post/247)