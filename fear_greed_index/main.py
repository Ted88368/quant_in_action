

import os
from pathlib import Path
import pandas as pd
import numpy as np
import akshare as ak
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class FearGreedIndex:
    def __init__(self, start_date='20200101', end_date=datetime.now().strftime('%Y%m%d')):
        self.start_date = start_date
        self.end_date = end_date
        self.df_index = pd.DataFrame()
        
    
    def get_market_data(self):
        """获取基础市场数据"""
        try:
            # 本地缓存目录（每日更新）
            cache_dir = Path('/tmp')
            cache_dir.mkdir(parents=True, exist_ok=True)
            today_str = date.today().strftime('%Y%m%d')

            def _get_cached_df(cache_key: str, loader_callable):
                """从 /tmp 缓存读取或调用 loader_callable 下载并保存。

                cache_key 应该是无空格、无特殊字符的短字符串，用于文件名。
                loader_callable 应返回 pandas.DataFrame 或类似对象。
                """
                safe_name = ''.join(c if c.isalnum() or c in ('_', '-') else '_' for c in cache_key)
                fname = cache_dir / f"akshare_{safe_name}_{self.start_date}_{self.end_date}_{today_str}.csv"
                if fname.exists():
                    try:
                        df = pd.read_csv(fname, index_col=0, parse_dates=True)
                        print(f'使用缓存: {fname}')
                        return df
                    except Exception as e:
                        print(f'读取缓存失败，重新下载: {e}')
                # 否则调用 loader
                try:
                    df = loader_callable()
                except Exception as e:
                    print(f'调用数据源失败: {e}')
                    return None

                # 只有在返回 DataFrame 时才保存
                try:
                    if hasattr(df, 'to_csv'):
                        # 保存索引
                        df.to_csv(fname, index=True)
                        print(f'已缓存到: {fname}')
                except Exception as e:
                    print(f'保存缓存失败: {e}')
                return df

            # 获取沪深300指数数据（兼容不同返回格式）
            symbol = "H30374"
            df_hs300 = _get_cached_df(f"stock_zh_index_hist_csindex_{symbol}",
                                     lambda: ak.stock_zh_index_hist_csindex(symbol=symbol,
                                                                          start_date=self.start_date,
                                                                          end_date=self.end_date))

            if df_hs300 is None:
                raise RuntimeError('无法获取或加载 hs300 指数数据')

            # 规范化日期列/索引
            if '日期' in df_hs300.columns:
                try:
                    df_hs300['日期'] = pd.to_datetime(df_hs300['日期'])
                    df_hs300 = df_hs300.set_index('日期')
                except Exception:
                    # 如果按列转换失败，尝试按能解析的索引处理
                    try:
                        df_hs300.index = pd.to_datetime(df_hs300.index)
                    except Exception:
                        pass
            else:
                # 如果没有 `日期` 列，尝试将索引转为 datetime 或查找可能的日期列名
                date_candidates = [c for c in df_hs300.columns if 'date' in str(c).lower() or '时间' in str(c) or '时间' in str(c)]
                if date_candidates:
                    c = date_candidates[0]
                    try:
                        df_hs300[c] = pd.to_datetime(df_hs300[c])
                        df_hs300 = df_hs300.set_index(c)
                    except Exception:
                        try:
                            df_hs300.index = pd.to_datetime(df_hs300.index)
                        except Exception:
                            pass
                else:
                    try:
                        df_hs300.index = pd.to_datetime(df_hs300.index)
                    except Exception:
                        pass

            # 规范化列名：寻找收盘和涨跌幅列的候选名称
            close_candidates = ['收盘', 'close', '收盘价', 'close_price']
            pct_candidates = ['涨跌幅', 'pct_chg', '涨幅', 'change_pct']

            def find_col(df, candidates):
                for cand in candidates:
                    for col in df.columns:
                        if cand.lower() == str(col).lower() or cand in str(col):
                            return col
                # 模糊匹配：列名包含关键字
                for col in df.columns:
                    name = str(col).lower()
                    for cand in candidates:
                        if any(k in name for k in [cand.lower() if isinstance(cand, str) else cand]):
                            return col
                return None

            close_col = find_col(df_hs300, close_candidates)
            pct_col = find_col(df_hs300, pct_candidates)

            if close_col is None or pct_col is None:
                # 输出调试信息并尝试使用前几列作为替代
                print('警告：未能找到标准的收盘/涨跌幅列，当前列为:', list(df_hs300.columns))
                if len(df_hs300.columns) >= 2:
                    close_col = df_hs300.columns[0]
                    pct_col = df_hs300.columns[1]
                else:
                    raise ValueError('df_hs300 列数不足以提取收盘和涨跌幅')

            df_hs300 = df_hs300.rename(columns={close_col: '收盘', pct_col: '涨跌幅'})
            
            # 获取北向资金数据（兼容不同版本的 akshare 接口名称）
            df_north = None
            candidate_funcs = [
                'stock_hsgt_north_net_flow_in_em',
                'stock_hsgt_north_net_flow_in',
                'stock_hsgt_north_money_flow',
                'stock_hsgt_north_net_inflow',
                'stock_hsgt_money_flow_hsgt',
            ]
            for func_name in candidate_funcs:
                cache_key = f"{func_name}"
                # 如果 ak 中存在该函数，尝试从缓存读取或调用
                if hasattr(ak, func_name):
                    df_north = _get_cached_df(cache_key, lambda func=func_name: getattr(ak, func)())
                    if df_north is not None:
                        break

                # 若 ak 中没有该函数，也尝试从缓存读取（可能之前通过其它机器/脚本生成）
                if df_north is None:
                    # 尝试读取本地缓存（无需函数存在）
                    possible = cache_dir / f"akshare_{func_name}_{self.start_date}_{self.end_date}_{today_str}.csv"
                    if possible.exists():
                        try:
                            df_north = pd.read_csv(possible, index_col=0, parse_dates=True)
                            print(f'使用已有缓存: {possible}')
                            break
                        except Exception:
                            df_north = None

            if df_north is None:
                print('警告：未能通过 akshare 获取北向资金数据，使用空占位（列名: 今日净流入）')
                # 使用与 hs300 相同的索引创建占位 df，避免后续 join 失败
                df_north = pd.DataFrame(index=df_hs300.index)
                df_north['今日净流入'] = np.nan
            else:
                # 尝试标准化列名为 `今日净流入`
                if '日期' in df_north.columns:
                    df_north['日期'] = pd.to_datetime(df_north['日期'])
                    df_north = df_north.set_index('日期')

                # 找到可能表示净流入/资金流向的列并重命名
                netcol = None
                for col in df_north.columns:
                    cname = str(col)
                    if '净' in cname or '流入' in cname or 'net' in cname.lower() or 'inflow' in cname.lower() or '资金' in cname:
                        netcol = col
                        break

                if netcol is None:
                    # 如果没找到合适列，新增占位列
                    df_north['今日净流入'] = np.nan
                else:
                    df_north = df_north.rename(columns={netcol: '今日净流入'})
            
            # 获取市场广度数据（上涨下跌家数），使用缓存
            df_breadth = _get_cached_df('stock_sse_summary', lambda: ak.stock_sse_summary())
            # 这里需要根据实际情况处理数据格式
            
            self.df_index = df_hs300[['收盘', '涨跌幅']].copy()
            self.df_index = self.df_index.rename(columns={'收盘': 'hs300_close', 
                                                         '涨跌幅': 'hs300_pct_chg'})
            
            # 合并北向资金数据
            self.df_index = self.df_index.join(df_north[['今日净流入']], how='left')
            
            return True
            
        except Exception as e:
            print(f"数据获取失败: {e}")
            return False
        
    def calculate_indicators(self):
        """计算各个情绪指标"""
        if self.df_index.empty:
            print("请先获取市场数据")
            return False

        try:
            df = self.df_index.copy()

            # 1. 市场动量指标 (20日波动率)
            df['volatility_20d'] = df['hs300_pct_chg'].rolling(20).std() * np.sqrt(252)
            # 标准化到0-100（波动率越高，恐惧情绪越高）
            df['momentum_score'] = 100 - (df['volatility_20d'] / df['volatility_20d'].quantile(0.8) * 100).clip(0, 100)

            # 2. 价格强度指标 (股价相对于均线的位置)
            df['ma_20'] = df['hs300_close'].rolling(20).mean()
            df['price_strength'] = (df['hs300_close'] / df['ma_20'] - 1) * 100
            # 标准化处理
            df['strength_score'] = (df['price_strength'] - df['price_strength'].min()) / (
                df['price_strength'].max() - df['price_strength'].min()) * 100

            # 3. 北向资金情绪（简化处理）
            if '今日净流入' in df.columns:
                df['north_flow_ma'] = df['今日净流入'].rolling(5).mean()
                df['north_score'] = (df['今日净流入'] - df['今日净流入'].rolling(20).min()) / (
                    df['今日净流入'].rolling(20).max() - df['今日净流入'].rolling(20).min()) * 100
                df['north_score'] = df['north_score'].fillna(50)  # 缺失值设为中性

            # 处理缺失值
            df = df.fillna(method='ffill')

            self.df_indicators = df
            return True

        except Exception as e:
            print(f"指标计算失败: {e}")
            return False
    
    def composite_index(self, weights=None):
        """合成恐贪指数"""
        if weights is None:
            weights = {'momentum_score': 0.3, 'strength_score': 0.4, 'north_score': 0.3}

        try:
            df = self.df_indicators.copy()

            # 计算加权综合指数
            df['fear_greed_index'] = 0
            for indicator, weight in weights.items():
                if indicator in df.columns:
                    df['fear_greed_index'] += df[indicator] * weight

            # 平滑处理
            df['fear_greed_index'] = df['fear_greed_index'].rolling(5).mean()

            # 分类标签
            df['sentiment'] = pd.cut(df['fear_greed_index'], 
                                   bins=[0, 20, 40, 60, 80, 100],
                                   labels=['极度恐惧', '恐惧', '中性', '贪婪', '极度贪婪'])

            self.df_result = df[['fear_greed_index', 'sentiment']].copy()
            return True

        except Exception as e:
            print(f"指数合成失败: {e}")
            return False

    def visualize_index(self, days=120):
        """可视化恐贪指数"""
        if not hasattr(self, 'df_result'):
            print("请先合成指数")
            return

        df_plot = self.df_result.tail(days)

        plt.figure(figsize=(12, 8))
        plt.style

        # 创建颜色映射
        colors = []
        for value in df_plot['fear_greed_index']:
            if value <= 20:
                colors.append('#FF6B6B')  # 红色-极度恐惧
            elif value <= 40:
                colors.append('#FFA5A5')  # 浅红-恐惧
            elif value <= 60:
                colors.append('#CCD1D1')  # 灰色-中性
            elif value <= 80:
                colors.append('#A5D6A7')  # 浅绿-贪婪
            else:
                colors.append('#66BB6A')  # 绿色-极度贪婪

        # 绘制指数曲线
        plt.bar(df_plot.index, df_plot['fear_greed_index'], color=colors, alpha=0.7)
        plt.plot(df_plot.index, df_plot['fear_greed_index'], color='#34495E', linewidth=1)

        # 添加参考线
        plt.axhline(y=20, color='#FF6B6B', linestyle='--', alpha=0.5, label='极度恐惧(20)')
        plt.axhline(y=80, color='#66BB6A', linestyle='--', alpha=0.5, label='极度贪婪(80)')
        plt.axhline(y=50, color='#7F8C8D', linestyle='-', alpha=0.3, label='中性(50)')

        plt.title(f'恐贪指数 (最近{days}天)', fontsize=15, fontweight='bold')
        plt.ylabel('恐贪指数')
        plt.ylim(0, 100)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 打印当前情绪状态
        current = self.df_result.iloc[-1]
        print(f"\n当前恐贪指数: {current['fear_greed_index']:.1f}")
        print(f"市场情绪: {current['sentiment']}")
        print(f"更新日期: {self.df_result.index[-1].strftime('%Y-%m-%d')}")


# 初始化并运行
fgi = FearGreedIndex(start_date='20250101')

# 获取数据
if fgi.get_market_data():
    # 计算指标
    if fgi.calculate_indicators():
        # 合成指数
        if fgi.composite_index():
            # 可视化结果
            fgi.visualize_index(days=60)
            
            # 保存结果
            fgi.df_result.to_csv('fear_greed_index.csv')
            print("恐贪指数计算完成，结果已保存至文件")

# 查看历史极值点
def analyze_extremes(df_result, threshold=20):
    """分析极端情绪点"""
    extremes = df_result[
        (df_result['fear_greed_index'] <= threshold) | 
        (df_result['fear_greed_index'] >= 100 - threshold)
    ]
    return extremes

if hasattr(fgi, 'df_result'):
    extreme_points = analyze_extremes(fgi.df_result)
    print(f"\n发现{len(extreme_points)}个极端情绪点")
    print(extreme_points.tail(10))