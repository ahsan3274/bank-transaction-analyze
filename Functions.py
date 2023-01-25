import config
import pandas as pd
import datetime
import pygsheets
from pydrive.drive import GoogleDrive

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
	sorted_df = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
	date = DataFrame["Date"]
	cnt=0
	i=0
	for x in date:
		if x.date()>=date_start and x.date()<=date_end:
			sorted_df.loc[i]=(df.iloc[cnt])
			i+=1		
		cnt=cnt+1

	return sorted_df

#Tax_Year
def tax_year(start_year,end_year,DataFrame):
	start= datetime.date(start_year,7,1)
	end= datetime.date(end_year,6,30)
	yearly = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
	yearly = datesort(start,end,DataFrame)
	return yearly

#Month
def month(month,year,DataFrame):
	month_idx = {
		'January':1,
		'February':2,
		'March':3,
		'April':4,
		'May':5,
		'June':6,
		'July':7,
		'August':8,
		'September':9,
		'October':10,
		'November':11,
		'December':12
	}
	month_days = {
		'January':31,
		'February':28,   #leap year unaccounted
		'March':31,
		'April':30,
		'May':31,
		'June':30,
		'July':31,
		'August':31,
		'September':30,
		'October':31,
		'November':30,
		'December':31
	}

	start= datetime.date(year,month_idx[month],1)
	end= datetime.date(year,month_idx[month],month_days[month ])
	monthly = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
	monthly = datesort(start,end,DataFrame)
	return monthly


#Cash Withdrawals
def cash_withdraw(DataFrame):
	df=DataFrame
	sorted_df = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
	description = DataFrame['Description']
	cnt=0
	i=0
	for x in description:
		if 'ATM Cash Withdrawal' in x:
			sorted_df.loc[i]=(df.iloc[cnt])
			i+=1
		cnt +=1

	return sorted_df

#Bank Charges
def charges(DataFrame):
	df=DataFrame
	sorted_df = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
	description = DataFrame['Description']
	cnt=0
	i=0
	for x in description:
		if 'Charges' in x:
			sorted_df.loc[i]=(df.iloc[cnt])
			i+=1
		cnt +=1

	return sorted_df


	
#Tax Year
def tax_year_data(start_year,end_year,df):	
	if(end_year-start_year!=1):
		return print('error')
	monthly_credit = {}
	monthly_debit = {}
	monthly_cash_withdrawal = {}
	monthly_bank_fees = {}
	cnt=0
	for x in config.tax_year_idx:
		monthly = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance'])
		if cnt<=5:
			monthly = month(x,start_year,tax_year(start_year,end_year,df))
			debit,credit = debit_credit(monthly)
			monthly_credit[x]= credit
			monthly_debit[x]= debit
			monthly_cash_withdrawal[x]=cash_withdraw(monthly)
			monthly_bank_fees[x]=charges(monthly)
		elif cnt>5:
			monthly = month(x,end_year,tax_year(start_year,end_year,df))
			debit,credit = debit_credit(monthly)
			monthly_credit[x]= credit
			monthly_debit[x]= debit
			monthly_cash_withdrawal[x]= cash_withdraw(monthly)
			monthly_bank_fees[x]=charges(monthly)
		cnt=cnt+1
	return monthly_credit,monthly_debit,monthly_cash_withdrawal,monthly_bank_fees






