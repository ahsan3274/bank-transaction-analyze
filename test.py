import config
import Functions



# file_metadata = {
# 		 'title': 'test',
#  	  'parents': [config.tax_folder],
#  	  'mimeType': 'application/vnd.google-apps.folder'
#  	}
# folder = config.drive.CreateFile(file_metadata)
# folder.Upload()	

# Functions.folder_create('test',config.tax_folder)


# def tax_year_data(start_year,end_year):
# 	folder = folder_create('{0}-{1}'.format(start_year,end_year),config.tax_folder)
# 	tax_folder_id = folder['id']
# 	if(end_year-start_year!=1):
# 		return print('error')
# 	for x in config.tax_year_idx:
# 		cnt=0
# 		monthly = pd.DataFrame(columns=['Date','Description','Amount','Dr/CR','Balance'])
# 		# if cnt<=5:
# 		# 	# sheet_create('{0}-{1}'.format(x,start_year),folder)
# 		# 	# month_sheet=config.gc.open(x)
# 		# 	# monthly = month(x,start_year,tax_year(start_year,end_year,config.y1))
# 		# 	# monthly_transactions = month_sheet.add_worksheet('Monthly Transactions')
# 		# 	# monthly_transactions.set_dataframe(monthly,[0,0])
# 		# 	debit,credit = debit_credit(monthly)
# 		# 	cash_withdrawal = cash_withdraw(monthly)

# 		# 	bank_fees = charges(monthly)
# 		# elif cnt>5:
# 		# 	monthly = month(x,end_year,tax_year(start_year,end_year,config.y1))
# 		# 	debit,credit = debit_credit(monthly)
# 		# 	cash_withdrawal = cash_withdraw(monthly)
# 		# 	bank_fees = charges(monthly)
# 		# cnt=cnt+1	


# #Create Folder
# def folder_create(name,parent_folder):
# 	file_metadata = {
# 	  'title': name,
# 	  'parents': parent_folder,
# 	  'mimeType': 'application/vnd.google-apps.folder'
# 	}
# 	folder = config.drive.CreateFile(file_metadata)
# 	folder.Upload()
# 	return folder	

# #create Sheet
# def sheet_create(name,parent_folder):
# 	config.gc.create(name,parent_folder)