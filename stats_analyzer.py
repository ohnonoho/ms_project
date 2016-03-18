
# coding: utf-8

# In[97]:

import csv
import collections
import numpy as np


# In[ ]:




# In[98]:

filename = 'data/train.csv'
trip_type = collections.Counter()
visit_number = collections.Counter()
weekday = collections.Counter()
upc = collections.Counter()
scan_count = collections.Counter()
department_description = collections.Counter()
fine_line_number = collections.Counter()

dicts = []
dicts.append(trip_type)
dicts.append(visit_number)
dicts.append(weekday)
dicts.append(upc)
dicts.append(scan_count)
dicts.append(department_description)
dicts.append(fine_line_number)

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    reader.next()  # skip the header
    for row in reader:
        for i in range(0, len(row)):
            dicts[i][row[i]] = dicts[i][row[i]] + 1

    print("train data total number: " + str(reader.line_num))
    print("trip_type total number: " + str(len(trip_type)))
    print("visit_number total number: " + str(len(visit_number)))
    print("weekday total number: " + str(len(weekday)))
    print("upc total number: " + str(len(upc)))
    print("scan_count total number: " + str(len(scan_count)))
    print("department_description total number: " + str(len(department_description)))
    print("fine_line_number: " + str(len(fine_line_number)))



# In[ ]:




# In[99]:

# count each TripType distributation
filename = 'data/train.csv'
types = collections.Counter()
    
prev = '-1'
with open(filename, 'r') as f2:
    reader = csv.reader(f2, delimiter=',', quotechar='"')
    reader.next()  # skip the header

    for row in reader:
        if prev == row[1]:# skip records with same VisitNum
            continue
        
        prev = row[1]        
        types[row[0]] = types[row[0]] + 1
    
    top = 10
    print('most common ' + str(top) + ' tripTypes:')
    mostCommonTypes = []
    
    for i in range(0,top):
        mostCommonTypes.append(types.most_common(top)[i][0])
        print(str(types.most_common(top)[i][0]) + ' '
              + str(types.most_common(top)[i][1]) + ' '
              + "%.3f" % (types.most_common(top)[i][1] / (sum(types.values()) * 1.0)))
        
    print(mostCommonTypes)


# In[100]:

# count each TripType's DepartmentDescription distributation
filename = 'data/train.csv'
daysPerType = {}
    
prev = '-1'
with open(filename, 'r') as f2:
    reader = csv.reader(f2, delimiter=',', quotechar='"')
    reader.next()  # skip the header

    for row in reader:
        if prev == row[1]:# skip records with same VisitNum
            continue
        
        #prev = row[1]        
        if row[0] not in daysPerType:
            daysPerType[row[0]] = collections.Counter()
            
        daysPerType[row[0]][row[5]] = daysPerType[row[0]][row[5]] + 1
    
    for i in range(0, 1000):
        if str(i) in mostCommonTypes:
            key = str(i)
            if (daysPerType[key].most_common(1)[0][1]/ (sum(daysPerType[key].values())*1.0 )) > 0.1:
                print('Type ' + key + ':' 
             + str(daysPerType[key].most_common(1)[0]) + ' '
             + "%.3f" % (daysPerType[key].most_common(1)[0][1]/ (sum(daysPerType[key].values())*1.0 )))


# In[101]:

# count each TripType's weekday distributation
filename = 'data/train.csv'
daysPerType = {}
    
prev = '-1'
with open(filename, 'r') as f2:
    reader = csv.reader(f2, delimiter=',', quotechar='"')
    reader.next()  # skip the header

    for row in reader:
        if prev == row[1]:# skip records with same VisitNum
            continue
        if row[0] not in mostCommonTypes: # count only mostCommonTypes
            continue
            
        prev = row[1]        
        if row[0] not in daysPerType:
            daysPerType[row[0]] = collections.Counter()
            
        daysPerType[row[0]][row[2]] = daysPerType[row[0]][row[2]] + 1
    
    
    for i in range(0, 1000):
        if str(i) in mostCommonTypes:
            key = str(i)
            print('Type ' + key + ':' + str(daysPerType[key].most_common(3)))
        
    


# In[102]:

# count TripType on each weekday
filename = 'data/train.csv'
typesPerDay = []
for i in range(0,7):
    typesPerDay.append(collections.Counter())
    
prev = '-1'
with open(filename, 'r') as f2:
    reader = csv.reader(f2, delimiter=',', quotechar='"')
    reader.next()  # skip the header

    for row in reader:
        if prev == row[1]:# skip records with same VisitNum
            continue

        
        prev = row[1]
        if row[2] == 'Monday':
            typesPerDay[0][row[0]] = typesPerDay[0][row[0]] + 1
        elif row[2] == 'Tuesday':
            typesPerDay[1][row[0]] = typesPerDay[1][row[0]] + 1
        elif row[2] == 'Wednesday':
            typesPerDay[2][row[0]] = typesPerDay[2][row[0]] + 1
        elif row[2] == 'Thursday':
            typesPerDay[3][row[0]] = typesPerDay[3][row[0]] + 1
        elif row[2] == 'Friday':
            typesPerDay[4][row[0]] = typesPerDay[4][row[0]] + 1
        elif row[2] == 'Saturday':
            typesPerDay[5][row[0]] = typesPerDay[5][row[0]] + 1
        elif row[2] == 'Sunday':
            typesPerDay[6][row[0]] = typesPerDay[6][row[0]] + 1
    
    for i in range(0, 7):
        print(sum(typesPerDay[i].values()))
        print("MostCommonType on day " +str(i) + str(typesPerDay[i].most_common(5)))
        
    


# In[ ]:



