# 株価のデータ分析


from pandas_datareader import data
# データの集計や加工などの機能
import pandas as pd
# グラフを描く機能
import matplotlib.pyplot as plt
import numpy as np


start = '2019-11-04'
end = '2020-11-04'

df = data.DataReader('^N225', 'yahoo', start, end)
# print(df.head(10))
df.dtypes
df.index
# print(df.index)

date = df.index
price = df['Adj Close']

# plt.plot(date, price)
# plt.show()


span01 = 5
span02 = 25
span03 = 50

df['sma01'] = price.rolling(window = span01).mean()    # サンプリングの間隔指定
df['sma02'] = price.rolling(window = span02).mean()
df['sma03'] = price.rolling(window = span03).mean()

pd.set_option('display.max_rows', None) #ターミナルに省略せずに表示
# print(df.head(100))

plt.figure(figsize = (20, 8))                  #グラフの大きさ
plt.plot(date, price, label = 'Nikkei225', color = '#99b898')          #x軸とy軸と凡例
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')

plt.title('N225', color = 'blue', backgroundcolor = 'white', size = 40, loc = 'center')     #タイトル
plt.xlabel('date', color = 'black', size = 30)
plt.ylabel('price', color = 'black', size = 30)

# plt.legend()
# plt.show()


plt.figure(figsize = (20, 10))
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')

# plt.legend()
# plt.show()


plt.figure(figsize = (20, 10))
plt.subplot(2, 1, 1)    #縦、横、位置

plt.plot(date, price, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
plt.legend()

# plt.show()


df = data.DataReader('6098.JP', 'stooq')
# print(df.head())
df = df.sort_index()
df.index >= '2019-07-01 00:00:00'
df[df.index >= '2019-07-01 00:00:00']
df[df.index <= '2020-07-01 00:00:00']
# print(df[(df.index >= '2019-07-01 00:00:00') & (df.index <= '2020-07-01 00:00:00')])

df = df[(df.index >= '2019-07-01 00:00:00') & (df.index <= '2020-07-01 00:00:00')]

date = df.index
price = df['Close']

span01 = 5
span02 = 25
span03 = 50

df['sma01'] = price.rolling(window = span01).mean()    # サンプリングの間隔指定
df['sma02'] = price.rolling(window = span02).mean()
df['sma03'] = price.rolling(window = span03).mean()

plt.figure(figsize = (20, 10))
plt.subplot(2, 1, 1)    #縦、横、位置

plt.plot(date, price, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
plt.legend()

# plt.show()


start = '2019-07-01'
end = '2020-07-01'
company_code = '6502.JP'

# ユニクロやGUなどがグループ会社のファーストリテイリング


df = df[(df.index >= start) & (df.index <= end)]
df = data.DataReader(company_code, 'stooq')

date = df.index
price = df['Close']

span01 = 5
span02 = 25
span03 = 50

df['sma01'] = price.rolling(window = span01).mean()
df['sma02'] = price.rolling(window = span02).mean()
df['sma03'] = price.rolling(window = span03).mean()

plt.figure(figsize = (20,10))
plt.subplot(2, 1, 1)

plt.plot(date, price, label = 'Close', color = '#99b898')
plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
plt.legend()

# plt.show()


def company_stock(start, end, company_code):
    df = data.DataReader(company_code, 'stooq')
    df = df[(df.index >= start) & (df.index <= end)]

    date = df.index
    price = df['Close']

    span01 = 5
    span02 = 25
    span03 = 50

    df['sma01'] = price.rolling(window = span01).mean()
    df['sma02'] = price.rolling(window = span02).mean()
    df['sma03'] = price.rolling(window = span03).mean()

    plt.figure(figsize = (20,10))
    plt.subplot(2, 1, 1)

    plt.plot(date, price, label = 'Close', color = '#99b898')
    plt.plot(date, df['sma01'], label = 'sma01', color = '#e84a5f')
    plt.plot(date, df['sma02'], label = 'sma02', color = '#ff847c')
    plt.plot(date, df['sma03'], label = 'sma03', color = '#feceab')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.bar(date, df['Volume'], label = 'Volume', color = 'grey')
    plt.legend()

    plt.show()

company_stock('2019-06-01', '2020-06-01', '6502.JP')
company_stock('2017-01-01', '2020-06-01', '6502.JP')
company_stock('2017-01-01', '2020-06-01', '7203.JP')




















