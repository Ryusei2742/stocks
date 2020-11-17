# 株価のデータ分析、BITCOIN

import pandas as pd
import numpy as np
import talib as ta
from pandas_datareader import data
import matplotlib.pyplot as plt
import warnings     #警告を表示させない
warnings.simplefilter('ignore')     #無視


start = '2019-07-01'
end = '2020-07-01'

df = data.DataReader('^N225', 'yahoo', start, end)

date = df.index
close = df['Adj Close']

span01 = 5
span02 = 25
span03 = 50

df['sma01'] = close.rolling(window = span01).mean()
df['sma02'] = close.rolling(window = span02).mean()
df['sma03'] = close.rolling(window = span03).mean()

plt.figure(figsize = (20,10))
plt.subplot(2, 1, 1)

plt.plot(date, close, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
plt.legend()
# plt.show()


# MACD トレンドを見る指標 0以上なら上昇トレンド、0以下なら下降トレンド
# 短期移動平均、長期移動平均、MACDシグナル
df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(close, fastperiod = 12, slowperiod = 26, signalperiod = 9)

plt.figure(figsize = (20,10))
plt.subplot(2, 1, 1)

plt.plot(date, close, label = 'Close', color = '#99b898')
plt.legend()

plt.subplot(2, 1, 2)
plt.fill_between(date, df['macdhist'], color = 'grey', alpha = 0.5, label = 'MACD_hist')
plt.hlines(0, start, end, "grey", linestyles = "dashed")
plt.legend()


# RSI 売られ過ぎ、買われ過ぎを判断する指標 20~30%を下回る...売られ過ぎ、70~80%を上回る...買われ過ぎ

df['RSI'] = ta.RSI(close, timeperiod = span02)

plt.figure(figsize = (20,10))
plt.subplot(2, 1, 1)

plt.plot(date, close, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(date, df['RSI'], label = 'RSI', color = 'grey')
plt.ylim(0, 100)
plt.hlines([30, 50, 70], start, end, "grey", linestyles = "dashed")
plt.legend()
# plt.show()


# ボリンジャーバンド 移動平均などの一定期間の平均に対して、一定期間の標準偏差を足したものと引いたもの　一般的にプラスマイナス標準偏差の2倍を使う

df['upper'], df['middle'], df['lower'] = ta.BBANDS(close, timeperiod = span02, nbdevup = 2, nbdevdn = 2, matype = 0)    #単純移動平均  0...単純移動平均、1...指数移動平均、2...加重移動平均

plt.figure(figsize = (20,10))

plt.plot(date, close, label = 'Close', color = '#99b898')  #終値のプロット
plt.fill_between(date, df['upper'], df['lower'], color = 'grey', alpha = 0.3)  #ボリンジャーバンドの塗りつぶし折れ線グラフのプロット
plt.legend()

# plt.show()


# Bitcoin ビットコ
start = '2017-07-01'
end = '2020-07-01'

df = data.DataReader('BTC-JPY', 'yahoo', start, end)

date = df.index
close = df['Adj Close']

span01 = 5
span02 = 25
span03 = 50

df['sma01'] = close.rolling(window = span01).mean()
df['sma02'] = close.rolling(window = span02).mean()
df['sma03'] = close.rolling(window = span03).mean()
df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(close, fastperiod = 12, slowperiod = 26, signalperiod = 9)
df['RSI'] = ta.RSI(close, timeperiod = span02)
df['upper'], df['middle'], df['lower'] = ta.BBANDS(close, timeperiod = span02, nbdevup = 2, nbdevdn = 2, matype = 0)    #matype単純移動平均  0...単純移動平均、1...指数移動平均、2...加重移動平均


plt.figure(figsize = (20,10))
plt.subplot(5, 1, 1)

plt.plot(date, close, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(5, 1, 2)
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
plt.legend()

plt.subplot(5, 1, 3)
plt.fill_between(date, df['macdhist'], color = 'grey', alpha = 0.5, label = 'MACD_hist')
plt.hlines(0, start, end, "grey", linestyles = "dashed")
plt.legend()

plt.subplot(5, 1, 4)
plt.plot(date, df['RSI'], label = 'RSI', color = 'grey')
plt.ylim(0, 100)
plt.hlines([30, 50, 70], start, end, "grey", linestyles = "dashed")
plt.legend()

plt.subplot(5, 1, 5)
plt.plot(date, close, label = 'Close', color = '#99b898')  #終値のプロット
plt.fill_between(date, df['upper'], df['lower'], color = 'grey', alpha = 0.3)  #ボリンジャーバンドの塗りつぶし折れ線グラフのプロット
plt.legend()

# plt.show()


# 為替 (日本円とUSドル)

start = '2020-01-01'
end = '2020-07-01'

df = data.DataReader('DEXJPUS', 'fred', start, end)
df = df.rename(columns = {'DEXJPUS' : 'Adj Close'})  #renameメソッドでカラム名変更
df = df.dropna()  #NaN削除

date = df.index
close = df['Adj Close']

span01 = 5
span02 = 25
span03 = 50

df['sma01'] = close.rolling(window = span01).mean()
df['sma02'] = close.rolling(window = span02).mean()
df['sma03'] = close.rolling(window = span03).mean()
df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(close, fastperiod = 12, slowperiod = 26, signalperiod = 9)
df['RSI'] = ta.RSI(close, timeperiod = span02)
df['upper'], df['middle'], df['lower'] = ta.BBANDS(close, timeperiod = span02, nbdevup = 2, nbdevdn = 2, matype = 0)    #matype単純移動平均  0...単純移動平均、1...指数移動平均、2...加重移動平均

plt.figure(figsize = (20,10))
plt.subplot(4, 1, 1)

plt.plot(date, close, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(4, 1, 2)
plt.fill_between(date, df['macdhist'], color = 'grey', alpha = 0.5, label = 'MACD_hist')
plt.hlines(0, start, end, "grey", linestyles = "dashed")
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(date, df['RSI'], label = 'RSI', color = 'grey')
plt.ylim(0, 100)
plt.hlines([30, 50, 70], start, end, "grey", linestyles = "dashed")
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(date, close, label = 'Close', color = '#99b898')  #終値のプロット
plt.fill_between(date, df['upper'], df['lower'], color = 'grey', alpha = 0.3)  #ボリンジャーバンドの塗りつぶし折れ線グラフのプロット
plt.legend()

plt.show()









