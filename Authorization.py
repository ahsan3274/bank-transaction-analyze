import pygsheets


#authorization
gc = pygsheets.authorize(service_file='/Users/Ahsan/Documents/Taxes/Service account key/potent-comfort-370413-0a4dbc376eae.json')
#open the google spreadsheet 
sh = gc.open_by_key('16snQSjblftK2PCrnQ1-X5ObphB8kQU5OHb_HaJF-MyU')


