## TA-Lib（Technical Analysis Library） 入门


#### 安装TA-Lib
##### OSX
```shell    
# 安装TA-Lib
brew install ta-lib
pip install TA-Lib
```
#### Linux
Download [ta-lib-0.6.4-src.tar.gz](https://github.com/ta-lib/ta-lib/releases/tag/v0.6.4) and:
```
untar and cd
./configure --prefix=/usr
make
sudo make install

python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ta-lib
```


#### 文档
+ [《talib-document》](https://github.com/Ted88368/talib-document)

#### 参考资料
+ [《量化交易的瑞士军刀：TA-Lib技术指标库详解》](https://mp.weixin.qq.com/s/ZSp_YFD0WcfbJh4xGy8hQA)
+ [《ta-lib》](https://ta-lib.github.io/ta-lib-python/doc_index.html)