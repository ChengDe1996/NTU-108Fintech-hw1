import sys

import pandas as pd
input_file = sys.argv[1]
#input_file = 'Daily_2019_08_05.csv'

#read csv file
csvFile = pd.read_csv(input_file, encoding= 'big5', dtype={'到期月份(週別)':str})
#find TX
correct_name = csvFile['商品代號'] =='TX     '
#the right name data
correct_data_temp = csvFile[correct_name]
#correct due month
month = correct_data_temp['到期月份(週別)'].min()
correct_month = csvFile['到期月份(週別)'] == month
#correct transaction time
correct_time = csvFile['成交時間'].between(84500, 134500)

#what we actually need
correct_data = correct_data_temp[correct_month & correct_time]

#initialize
open_value = 0
high_value = 0
low_value = 0
close_value = 0
'''
for i in range(0,len(correct_data)):
	if (open_value == 0 ) and (int(correct_data.iloc[i]['成交時間']) >= 84500):
			open_value = int(correct_data.iloc[i]['成交價格'])
	if (int(correct_data.iloc[i]['成交價格'])> high_value):
			high_value = int(correct_data.iloc[i]['成交價格'])
	if (int(correct_data.iloc[i]['成交價格'])< low_value):
			low_value = int(correct_data.iloc[i]['成交價格'])
'''
open_value = int(correct_data.iloc[0]['成交價格'])
close_value = int(correct_data.iloc[-1]['成交價格'])
high_value = int(correct_data['成交價格'].max())
low_value = int(correct_data['成交價格'].min())
print(int(open_value), int(high_value), int(low_value), int(close_value))







			
