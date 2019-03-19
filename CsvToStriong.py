
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("F:\\Dev\\localmessage.xlsx") 

# Set which language transaltion 
# Use Iso language and country codes
# for English - 'en-US'
# for Candian French - 'fr-CA'
# for English - 'es-MX'
language="es-MX"
selectedLanColIndex=0
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 

for languageColIndex in range(sheet.ncols):
	print(sheet.cell_value(0,languageColIndex))
	if(str(sheet.cell_value(0,languageColIndex)) == language):
		selectedLanColIndex=languageColIndex
		break
	
print(selectedLanColIndex)

# output text file
text_file = open(language+"-translationMapping.txt", "w")

#<string name="app_name">UAT-Aliquot</string>  sample converted string from excel
# "BUILDING_GET_SUCCESS": "Building fetched successfully." backend

for i in range(sheet.nrows): 
	# for IOS
	# text_file.write(repr(sheet.cell_value(i,0))+" = "+repr(sheet.cell_value(i, 1)))    
	# for Android
	 text_file.write('<string name="'+str(sheet.cell_value(i,0))+'">'+str(sheet.cell_value(i, selectedLanColIndex))+'</string>')
	# for Backend(Node.js)
	text_file.write('"'+str(sheet.cell_value(i,0))+'":"'+str(sheet.cell_value(i, selectedLanColIndex))+'",')
	text_file.write("\n")
		
text_file.close()
