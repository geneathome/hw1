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

result=[]
C0A880=[]
C0F9A0=[]
C0G640=[]
C0R190=[]
C0X260=[]

for i in range(len(data)):
    if data[i]['PRES']=='-99.000' or data[i]['PRES']=='-999.000':         
        abc=0;
    else:
        if data[i]['station_id']=='C0A880':
            C0A880.append(float(data[i]['PRES']))
        if data[i]['station_id']=='C0F9A0':
            C0F9A0.append(float(data[i]['PRES']))
        if data[i]['station_id']=='C0G640':
            C0G640.append(float(data[i]['PRES']))
        if data[i]['station_id']=='C0R190':
            C0R190.append(float(data[i]['PRES']))
        if data[i]['station_id']=='C0X260':
            C0X260.append(float(data[i]['PRES']))

if (len(C0A880) == 0):
    result.append(['C0A880','None'])
else:
    result.append(float(sum(C0A880)/len(C0A880)))
if (len(C0F9A0) == 0):
    result.append(['C0F9A0','None'])
else:
    result.append(float(sum(C0F9A0)/len(C0F9A0)))
if (len(C0G640) == 0):
    result.append(['C0G640','None'])
else:
    result.append(float(sum(C0G640)/len(C0G640)))
if (len(C0R190) == 0):
    result.append(['C0R190','None'])
else:
    result.append(float(sum(C0R190)/len(C0R190)))
if (len(C0X260) == 0):
    result.append(['C0X260','None'])
else:
    result.append(float(sum(C0X260)/len(C0X260)))    
    
 
#=======================================


# Part. 4

#=======================================

# Print result


print(result)
#========================================