### TA-Lib（Technical Analysis Library） 入门

TA-Lib 是一个广泛使用的技术分析库，提供了150多种技术指标和模式识别函数。它支持多种编程语言，包括Python。本文档介绍了TA-Lib中的主要指标组和具体指标。

#### Indicator Groups 🏷️
+ Overlap Studies（重叠研究指标）
+ Momentum Indicators（动量指标）
+ Volume Indicators（成交量指标）
+ Volatility Indicators（波动率指标）
+ Price Transform（价格变换）
+ Cycle Indicators（周期指标）
+ Pattern Recognition（模式识别）

#### Overlap Studies（重叠研究指标）
这些指标通常涉及移动平均线和其他重叠在价格图表上的研究。
```text 
BBANDS               Bollinger Bands（布林带）
DEMA                 Double Exponential Moving Average（双指数移动平均）
EMA                  Exponential Moving Average（指数移动平均）
HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline（希尔伯特变换 - 瞬时趋势线）
KAMA                 Kaufman Adaptive Moving Average（考夫曼自适应移动平均）
MA                   Moving average（移动平均）
MAMA                 MESA Adaptive Moving Average（MESA自适应移动平均）
MAVP                 Moving average with variable period（可变周期移动平均）
MIDPOINT             MidPoint over period（周期中点）
MIDPRICE             Midpoint Price over period（周期中点价格）
SAR                  Parabolic SAR（抛物线SAR）
SAREXT               Parabolic SAR - Extended（抛物线SAR - 扩展）
SMA                  Simple Moving Average（简单移动平均）
T3                   Triple Exponential Moving Average (T3)（三重指数移动平均T3）
TEMA                 Triple Exponential Moving Average（三重指数移动平均）
TRIMA                Triangular Moving Average（三角移动平均）
WMA                  Weighted Moving Average（加权移动平均）
```
#### Momentum Indicators（动量指标）
动量指标用于测量价格变动的速度和变化率，帮助识别趋势的强度和可能的转折点。
```text
ADX                  Average Directional Movement Index（平均定向运动指数）
ADXR                 Average Directional Movement Index Rating（平均定向运动指数评级）
APO                  Absolute Price Oscillator（绝对价格振荡器）
AROON                Aroon（阿隆指标）
AROONOSC             Aroon Oscillator（阿隆振荡器）
BOP                  Balance Of Power（力量平衡）
CCI                  Commodity Channel Index（顺势指标）
CMO                  Chande Momentum Oscillator（钱德动量振荡器）
DX                   Directional Movement Index（定向运动指数）
MACD                 Moving Average Convergence/Divergence（移动平均收敛散度）
MACDEXT              MACD with controllable MA type（可控MA类型的MACD）
MACDFIX              Moving Average Convergence/Divergence Fix 12/26（MACD修正12/26）
MFI                  Money Flow Index（资金流量指数）
MINUS_DI             Minus Directional Indicator（负向定向指标）
MINUS_DM             Minus Directional Movement（负向定向运动）
MOM                  Momentum（动量）
PLUS_DI              Plus Directional Indicator（正向定向指标）
PLUS_DM              Plus Directional Movement（正向定向运动）
PPO                  Percentage Price Oscillator（百分比价格振荡器）
ROC                  Rate of change : ((price/prevPrice)-1)*100（变动率：((价格/前价格)-1)*100）
ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice（变动率百分比：(价格-前价格)/前价格）
ROCR                 Rate of change ratio: (price/prevPrice)（变动率比率：(价格/前价格)）
ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100（变动率比率100刻度：(价格/前价格)*100）
RSI                  Relative Strength Index（相对强弱指数）
STOCH                Stochastic（随机指标）
STOCHF               Stochastic Fast（快速随机指标）
STOCHRSI             Stochastic Relative Strength Index（随机相对强弱指数）
TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA（三重平滑EMA的1日变动率）
ULTOSC               Ultimate Oscillator（终极振荡器）
WILLR                Williams' %R（威廉指标）
```

#### Volume Indicators（成交量指标）
这些指标基于成交量数据，帮助分析市场的买卖压力。
```text
AD                   Chaikin A/D Line（蔡金A/D线）
ADOSC                Chaikin A/D Oscillator（蔡金A/D振荡器）
OBV                  On Balance Volume（平衡成交量）
```

#### Cycle Indicators（周期指标）
这些指标使用希尔伯特变换来识别市场周期和趋势模式。
```text
HT_DCPERIOD          Hilbert Transform - Dominant Cycle Period（希尔伯特变换 - 主周期周期）
HT_DCPHASE           Hilbert Transform - Dominant Cycle Phase（希尔伯特变换 - 主周期相位）
HT_PHASOR            Hilbert Transform - Phasor Components（希尔伯特变换 - 相量组件）
HT_SINE              Hilbert Transform - SineWave（希尔伯特变换 - 正弦波）
HT_TRENDMODE         Hilbert Transform - Trend vs Cycle Mode（希尔伯特变换 - 趋势 vs 周期模式）
```

#### Price Transform（价格变换）
这些函数将价格数据转换为不同的表示形式，用于进一步分析。
```text
AVGPRICE             Average Price（平均价格）
MEDPRICE             Median Price（中位价格）
TYPPRICE             Typical Price（典型价格）
WCLPRICE             Weighted Close Price（加权收盘价格）
```
#### Volatility Indicators（波动率指标）
这些指标测量价格变动的幅度，帮助评估市场的波动性。
```text
ATR                  Average True Range（平均真实波幅）
NATR                 Normalized Average True Range（标准化平均真实波幅）
TRANGE               True Range（真实波幅）
```
#### Pattern Recognition（模式识别）
这些函数识别日本烛台模式和其他价格模式，用于预测价格走势。
```text
CDL2CROWS            Two Crows（两只乌鸦）
CDL3BLACKCROWS       Three Black Crows（三只黑乌鸦）
CDL3INSIDE           Three Inside Up/Down（三内部上涨/下跌）
CDL3LINESTRIKE       Three-Line Strike（三线打击）
CDL3OUTSIDE          Three Outside Up/Down（三外部上涨/下跌）
CDL3STARSINSOUTH     Three Stars In The South（南方三星）
CDL3WHITESOLDIERS    Three Advancing White Soldiers（三白兵）
CDLABANDONEDBABY     Abandoned Baby（弃婴）
CDLADVANCEBLOCK      Advance Block（推进块）
CDLBELTHOLD          Belt-hold（捉腰带线）
CDLBREAKAWAY         Breakaway（脱离）
CDLCLOSINGMARUBOZU   Closing Marubozu（收盘光头光脚）
CDLCONCEALBABYSWALL  Concealing Baby Swallow（藏婴吞没）
CDLCOUNTERATTACK     Counterattack（反击）
CDLDARKCLOUDCOVER    Dark Cloud Cover（乌云盖顶）
CDLDOJI              Doji（十字星）
CDLDOJISTAR          Doji Star（十字星）
CDLDRAGONFLYDOJI     Dragonfly Doji（蜻蜓十字星）
CDLENGULFING         Engulfing Pattern（吞没模式）
CDLEVENINGDOJISTAR   Evening Doji Star（黄昏十字星）
CDLEVENINGSTAR       Evening Star（黄昏之星）
CDLGAPSIDESIDEWHITE  Up/Down-gap side-by-side white lines（向上/向下跳空并排白线）
CDLGRAVESTONEDOJI    Gravestone Doji（墓碑十字星）
CDLHAMMER            Hammer（锤头）
CDLHANGINGMAN        Hanging Man（吊人）
CDLHARAMI            Harami Pattern（孕线模式）
CDLHARAMICROSS       Harami Cross Pattern（十字孕线模式）
CDLHIGHWAVE          High-Wave Candle（高波蜡烛）
CDLHIKKAKE           Hikkake Pattern（陷阱模式）
CDLHIKKAKEMOD        Modified Hikkake Pattern（修正陷阱模式）
CDLHOMINGPIGEON      Homing Pigeon（归巢鸽）
CDLIDENTICAL3CROWS   Identical Three Crows（相同三乌鸦）
CDLINNECK            In-Neck Pattern（颈内线模式）
CDLINVERTEDHAMMER    Inverted Hammer（倒锤头）
CDLKICKING           Kicking（踢）
CDLKICKINGBYLENGTH   Kicking - bull/bear determined by the longer marubozu（踢 - 由较长光头光脚决定多空）
CDLLADDERBOTTOM      Ladder Bottom（梯底）
CDLLONGLEGGEDDOJI    Long Legged Doji（长腿十字星）
CDLLONGLINE          Long Line Candle（长线蜡烛）
CDLMARUBOZU          Marubozu（光头光脚）
CDLMATCHINGLOW       Matching Low（匹配低点）
CDLMATHOLD           Mat Hold（垫肩）
CDLMORNINGDOJISTAR   Morning Doji Star（早晨十字星）
CDLMORNINGSTAR       Morning Star（启明星）
CDLONNECK            On-Neck Pattern（颈上线模式）
CDLPIERCING          Piercing Pattern（刺穿模式）
CDLRICKSHAWMAN       Rickshaw Man（黄包车夫）
CDLRISEFALL3METHODS  Rising/Falling Three Methods（上升/下降三法）
CDLSEPARATINGLINES   Separating Lines（分离线）
CDLSHOOTINGSTAR      Shooting Star（流星）
CDLSHORTLINE         Short Line Candle（短线蜡烛）
CDLSPINNINGTOP       Spinning Top（陀螺）
CDLSTALLEDPATTERN    Stalled Pattern（停滞模式）
CDLSTICKSANDWICH     Stick Sandwich（棍棒三明治）
CDLTAKURI            Takuri (Dragonfly Doji with very long lower shadow)（高价位十字星）
CDLTASUKIGAP         Tasuki Gap（手袋跳空）
CDLTHRUSTING         Thrusting Pattern（推模式）
CDLTRISTAR           Tristar Pattern（三星模式）
CDLUNIQUE3RIVER      Unique 3 River（独特三河）
CDLUPSIDEGAP2CROWS   Upside Gap Two Crows（向上跳空两乌鸦）
CDLXSIDEGAP3METHODS  Upside/Downside Gap Three Methods（向上/向下跳空三法）
```