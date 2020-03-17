# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061152.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

target_data = []
C0A880_result=[]
C0F9A0_result=[]
C0G640_result=[]
C0R190_result=[]
C0X260_result=[]

for rowtop in data:
    if(rowtop['PRES']!='-99.000')and (rowtop['PRES']!='-999.00'):         #ignore them
        if(rowtop['station_id']=='C0A880'):
            C0A880_result.append(float(rowtop['PRES']))
        if(rowtop['station_id']=='C0F9A0'):
            C0F9A0_result.append(float(rowtop['PRES']))
        if(rowtop['station_id']=='C0G640'):
            C0G640_result.append(float(rowtop['PRES']))
        if(rowtop['station_id']=='C0R190'):
            C0R190_result.append(float(rowtop['PRES']))
        if(rowtop['station_id']=='C0X260'):
            C0X260_result.append(float(rowtop['PRES']))

COA880sum=sum(C0A880_result)
C0F9A0sum=sum(C0F9A0_result)
C0G640sum=sum(C0G640_result)
C0R190sum=sum(C0R190_result)
C0X260sum=sum(C0X260_result)

if len(C0A880_result) ==0:                                                  
    target_data.append(['C0A880','None'])
else:
    target_data.append(['C0A880',COA880sum/len(C0A880_result)])
if len(C0F9A0_result) ==0:
    target_data.append(['C0F9A0','None'])
else:
    target_data.append(['C0F9A0',C0F9A0sum/len(C0F9A0_result)])
    
if len(C0G640_result) ==0:
    target_data.append(['C0g640','None'])
else:   
    target_data.append(['C0G640',C0G640sum/len(C0G640_result)])

    
if len(C0A880_result) ==0:
    target_data.append(['C0R190','None'])
else:
    target_data.append(['C0R190',C0G640sum/len(C0R190_result)])

    
if len(C0A880_result) ==0:
    target_data.append(['C0X260','None'])
else:
    target_data.append(['C0X260',C0X260sum/len(C0X260_result)])

        

#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================