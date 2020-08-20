
import csv


#input_file = sys.argv[1]
input_file = 'Daily_2019_08_06.csv'

with open(input_file, newline = '', encoding = 'big5') as csvFile:
	rows = csv.DictReader(csvFile)
	month = 100000000
	for row in rows:
		if len(row['到期月份(週別)'])>12:
			continue
		if(int(row['到期月份(週別)'])< month):
			month = int(row['到期月份(週別)'])
	newFile = []
	for row in rows:
		if row['商品代號'][:2] == 'TX':
			if int(row['成交時間']) >= 84500 and int(row['成交時間']) <= 134500:
				if (int(row['到期月份(週別)'][:6]) == month):
					newFile.append(row)

	print(len(newFile))
	open_value = 0
	high_value = 0
	low_value = 1000000
	close_value = 0

	for row in newFile:
		if (open_value == 0 ) and (int(row['成交時間']) >= 84500):
			open_value = row['成交價格']
		if (int(row['成交價格'])> high_value):
			high_value = int(row['成交價格'])
		if (int(row['成交價格'])< low_value):
			low_value = int(row['成交價格'])

	close_value = int(newFile[len(newFile)-1]['成交價格'])
	print(len(newFile))
	print(int(open_value), int(high_value), int(low_value), int(close_value))







			
