import sys
import pandas as pd
#filename = sys.argv[1]
filename = 'Daily_2019_08_05.csv'
df = pd.read_csv(filename, encoding= 'big5', dtype={'到期月份(週別)':str})
#print(df.shape)
#### filter 商品代號 == TX
is_TX = df['商品代號']=='TX     '
df_TX = df[is_TX]
#print('tx shape:', is_TX.shape)

#### filter 到期月份 == 最近月契約
min_month = df_TX['到期月份(週別)'].min()
is_month = df_TX['到期月份(週別)']==min_month
#print(is_month)
#df_month = df_TX[is_month]
#print('month shape:', df_month.shape)

#### filter 時間 == [08:45~13:45]
in_time = df_TX['成交時間'].between(84500, 134500)
df_in_time = df_TX[is_month & in_time]
#print(df_in_time.shape)
#print('#:', df_in_time['成交價格'].values[0])

#### print results
_open = int(df_in_time['成交價格'].values[0])
_close = int(df_in_time['成交價格'].values[-1])
_high = int(max(df_in_time['成交價格']))
_low = int(min(df_in_time['成交價格']))

print(_open, _high, _low, _close)