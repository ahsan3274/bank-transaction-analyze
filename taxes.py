import pygsheets
import pandas as pd
import datetime
from pandas import Timestamp

#authorization

gc = pygsheets.authorize(service_file='/Users/Ahsan/Documents/Taxes/Service account key/potent-comfort-370413-0a4dbc376eae.json')

# Create empty dataframe
df_1 = pd.DataFrame() #18-19
df_2 = pd.DataFrame() #19-20
df_3 = pd.DataFrame() #20-21
df_4 = pd.DataFrame() #21-22
df_5 = pd.DataFrame() #22-23


#open the google spreadsheet 
sh = gc.open_by_key('1XTUSmHt6-4fFOqgrWK2R5RB4shpq19d2')

#select the first sheet 
ws_1 = sh[0] #18-19
ws_2 = sh[1] #19-20
ws_3 = sh[2] #20-21
ws_4 = sh[3] #21-22
# ws_5 = sh[4] #Summary

#Data frames for each sheets
df_1 = pd.DataFrame(ws_1.get_all_records(1,5))
df_1["Date"] = pd.to_datetime(df_1["Date"],format="%d/%m/%Y") #DateTime formatting
df_2 = pd.DataFrame(ws_2.get_all_records(1,5))
df_2["Date"] = pd.to_datetime(df_2["Date"],dayfirst=True)
df_3 = pd.DataFrame(ws_3.get_all_records(1,5))
df_3["Date"] = pd.to_datetime(df_3["Date"],dayfirst=True)
df_4 = pd.DataFrame(ws_4.get_all_records(1,5))
df_4["Date"] = pd.to_datetime(df_4["Date"],dayfirst=True)
df_5 = pd.DataFrame(ws_5.get_all_records(1,1))

# print(df_1["Date"])
# print(df_1.dtypes)
# df_1["Date"] = pandas.to

#debit credit seperator
def debit_credit(DataFrame):
	dr_cr =	DataFrame["Dr/Cr"]	
	amount = DataFrame["Amount"]
	sum_dr = 0
	sum_cr = 0
	cnt=0
	for x in dr_cr:
		if x=="Dr":
				sum_dr = sum_dr+amount[cnt] 
		elif x=="Cr":
				sum_cr = sum_cr+amount[cnt] 
		cnt += 1
	return sum_dr, sum_cr



#Date Sort
def datesort(date_start,date_end,DataFrame):
	df = DataFrame
	sorted_df = pd.DataFrame()
	sorted_df.reindex_like(DataFrame)
	date = DataFrame["Date"]
	cnt=0
	for x in date:
		if x.date()>=date_start and x.date()<=date_end:
			row = df.iloc[cnt]
			sorted_df.add(row,axis='rows')
			print(sorted_df)
			print(row)
			# sorted_df = pd.concat([row],sorted_df)
			# print(df.iloc[cnt])	
		cnt +=1
	return sorted_df

print(datesort(Start,End,df_1))
# print(df_1.iloc[1])




