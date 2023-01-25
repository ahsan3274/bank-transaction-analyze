import config
import Functions
import datetime
import pandas as pd
import csv
import os

##variables
tax_year = {'Credit': None, 'Debit': None, 'Cash Withdrawal': None, 'Bank Fees': None}
tax = {'18-19': tax_year, '19-20': tax_year, '20-21': tax_year, '21-22': tax_year}

# Tax Year 18-19
start_year = 2018
end_year = 2019
tax['18-19']['Credit'] = Functions.tax_year_data(start_year, end_year, config.y1)[0]
tax['18-19']['Debit'] = Functions.tax_year_data(start_year, end_year, config.y1)[1]
tax['18-19']['Cash Withdrawal'] = Functions.tax_year_data(start_year, end_year, config.y1)[2]
tax['18-19']['Bank Fees'] = Functions.tax_year_data(start_year, end_year, config.y1)[3]
# 19-20
start_year = 2019
end_year = 2020
tax['19-20']['Credit'] = Functions.tax_year_data(start_year, end_year, config.y1)[0]
tax['19-20']['Debit'] = Functions.tax_year_data(start_year, end_year, config.y1)[1]
tax['19-20']['Cash Withdrawal'] = Functions.tax_year_data(start_year, end_year, config.y1)[2]
tax['19-20']['Bank Fees'] = Functions.tax_year_data(start_year, end_year, config.y1)[3]
# 20-21
start_year = 2020
end_year = 2021
tax['20-21']['Credit'] = Functions.tax_year_data(start_year, end_year, config.y1)[0]
tax['20-21']['Debit'] = Functions.tax_year_data(start_year, end_year, config.y1)[1]
tax['20-21']['Cash Withdrawal'] = Functions.tax_year_data(start_year, end_year, config.y1)[2]
tax['20-21']['Bank Fees'] = Functions.tax_year_data(start_year, end_year, config.y1)[3]
# 21-22
start_year = 2021
end_year = 2022
tax['21-22']['Credit'] = Functions.tax_year_data(start_year, end_year, config.y1)[0]
tax['21-22']['Debit'] = Functions.tax_year_data(start_year, end_year, config.y1)[1]
tax['21-22']['Cash Withdrawal'] = Functions.tax_year_data(start_year, end_year, config.y1)[2]
tax['21-22']['Bank Fees'] = Functions.tax_year_data(start_year, end_year, config.y1)[3]

# all data to csv
open('Users/Ahsan/Documents/Taxes/CSV File Outputs/test.csv', 'w')

# /Users/Ahsan/Documents/Taxes/CSV File Outputs/
