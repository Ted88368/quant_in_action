# quant_in_action

### quant_in_action
#### 运行
```shell
pip install virtualenv
virtualenv --version

# 创建虚拟环境
# 默认使用当前目录
virtualenv venv --python=python3.10


# 激活 venv
# OSX/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

pip freeze > requirements.txt
pip install -r requirements.txt
```
#### 工具库
##### 数据源
+ [akshare](https://github.com/akfamily/akshare) 
+ [baostock](http://baostock.com/baostock) 
+ [TuShare](https://tushare.pro/) 积分制度比较麻烦
+ [adata](https://github.com/1nchaos/adata) 免费开源A股量化数据库
+ [efinance](https://github.com/Micro-sheep/efinance) 一个可以快速获取基金、股票、债券、期货数据的 Python 库
+ [yahoofinancials](https://github.com/JECSand/yahoofinancials)
+ [AKShare](https://akshare.akfamily.xyz/introduction.html) AKShare 是基于 Python 的财经数据接口库，目的是实现对股票、期货、期权、基金、外汇、债券、指数、加密货币等金融产品的基本面数据、实时和历史行情数据、衍生数据从数据采集、数据清洗到数据落地的一套工具，主要用于学术研究目的。
 
#### 数据可视化
+ Matplotlib：基础而强大的可视化库
Matplotlib是Python中最基础、最常用的数据可视化库之一。它提供了丰富的绘图函数和工具，可以绘制各种类型的图表，如折线图、柱状图、散点图等。Matplotlib的绘图风格灵活，支持自定义样式和配色，适合用于制作各种类型的图表。
+ Seaborn：基于Matplotlib的高级可视化库
Seaborn是一个基于Matplotlib的高级可视化库，它提供了更加美观和易用的绘图接口。Seaborn内置了多种主题和配色方案，可以轻松地制作出高质量的图表。此外，Seaborn还提供了许多用于数据探索和可视化的函数，如分布图、热力图等，非常适合用于数据分析和数据挖掘。
+ Plotly：交互式数据可视化库
Plotly是一个交互式数据可视化库，它支持创建各种类型的图表，包括散点图、折线图、柱状图、热力图等。Plotly的最大特点是支持交互式操作，用户可以通过鼠标或触摸屏与图表进行交互，如缩放、平移、旋转等。这使得Plotly非常适合用于制作交互式数据报告和仪表盘。
+ Bokeh：用于Web的交互式数据可视化库
Bokeh是一个专门为Web设计的交互式数据可视化库，它可以与各种Web框架集成，如Flask、Django等。Bokeh支持创建各种类型的图表，包括散点图、柱状图、地图等，并且支持实时数据更新和交互式操作。这使得Bokeh非常适合用于制作Web数据可视化应用。
##### 总结
以上几个Python数据可视化库各有特点，Matplotlib和Seaborn适合用于制作各种类型的静态图表，而Plotly和Bokeh则更适合用于制作交互式数据可视化应用。在实际应用中，我们可以根据需求选择合适的库，并结合它们的特点和优势来制作高质量的数据可视化作品。

#### 资料
+ [《量化开源课程》](https://github.com/Ted88368/whale-quant.git) 本项目为量化开源课程，可以帮助人们快速掌握量化金融知识以及使用Python进行量化开发的能力。
+ 《基本面量化投资：运用财务分析和量化策略获取超额收益》
+ 《中低频量化交易策略研发》
+ [《Hands-On-Financial-Trading-with-Python》](https://github.com/Ted88368/Hands-On-Financial-Trading-with-Python)

 ####  策略
 ##### 基本面选股
 
#### 参考项目
+ [startquant](https://github.com/Ted88368/startquant.git)  
+ [利用python对国内各大券商的金工研报进行复现](https://github.com/Ted88368/QuantsPlaybook) 依赖聚宽，但是知识点可以用
+ [pythondict-quant](https://github.com/Ted88368/pythondict-quant) Quant Examples Based on Backtrader。


#### 量化核心
+ 多因子选股
+ 择时
+ 投资组合


#### 参考资料
+ [《主流股票数据源框架横向对比》](https://zhuanlan.zhihu.com/p/637409118)