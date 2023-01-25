import pygsheets
import pandas as pd
import datetime
import pygsheets
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive


#Google
	#authorization
		#sheets
gc = pygsheets.authorize(service_file='/Users/Ahsan/Documents/Taxes/Service account key/potent-comfort-370413-0a4dbc376eae.json')
		#drive
# gauth= GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# drive = GoogleDrive(gauth)

		#open the google spreadsheet 
sh = gc.open_by_key('16snQSjblftK2PCrnQ1-X5ObphB8kQU5OHb_HaJF-MyU')
		#parent folder ID
# tax_folder = {'id':"1XTUSmHt6-4fFOqgrWK2R5RB4shpq19d2"}

# Create empty dataframe
y1 = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance']) #18-19
y2 = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance']) #19-20
y3 = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance']) #20-21
y4 = pd.DataFrame(columns=['Date','Description','Amount','Dr/Cr','Balance']) #21-22
# sm = pd.DataFrame(columns=['Year','Month','Debit','Credit','Difference','Bank Fees']) #22-23

#selecting sheets
ws_1 = sh[0] #18-19
ws_2 = sh[1] #19-20
ws_3 = sh[2] #20-21
ws_4 = sh[3] #21-22
# ws_5 = sh[4] #Summary

#Data frames for each sheets
y1 = pd.DataFrame(ws_1.get_all_records(1,5))         #18-19
y1["Date"] = pd.to_datetime(y1["Date"],format="%d/%m/%Y") #DateTime formatting
y2 = pd.DataFrame(ws_2.get_all_records(1,5))			#19-20
y2["Date"] = pd.to_datetime(y2["Date"],dayfirst=True)
y3 = pd.DataFrame(ws_3.get_all_records(1,5))			#20-21
y3["Date"] = pd.to_datetime(y3["Date"],dayfirst=True)
y4 = pd.DataFrame(ws_4.get_all_records(1,5))			#21-22
y4["Date"] = pd.to_datetime(y4["Date"],dayfirst=True)
# sm = ws_5.get_all_records(0,0)		#summary


year_idx = ['January','February','March','April','May','June','July','August','September','October','November','December']
tax_year_idx = ['July','August','September','October','November','December','January','February','March','April','May','June']



