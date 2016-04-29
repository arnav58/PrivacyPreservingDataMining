import itertools
import csv
import plotly
import re
import sqlite3
print plotly.__version__  # version >1.9.4 required
import plotly.graph_objs as go


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'dataWithAge.csv'

fo=open(fname,"rb")
reader=csv.reader(fo)

data=[]
temp=[]
for row in reader:
    data.append(row)
    num_item=len(row)

#print data


minSupport=int(raw_input("Enter minimum support:"))

def count(item):

	count=0

	for t in data:
		if set(item) <= set(t):
			count=count+1

	return count

def getL(C):

	l=[]

	for i in C:
		if count([i])>=minSupport:
			l.append(i)

	return l

def item(C):

	L=[]

	for i in C:
		if count(i)>=minSupport:
			L.append(i)

	return L

def subset(L,k):

	a=list(itertools.combinations(L,k))
	b=[]

	for i in a:
		b.append(list(i))

	return b


items=[]

for t in data:
	for i in t:
		if i not in items:
			items.append(i)

C=[]
L=[]

C.append(items)
L.append(getL(C[0]))

i=0

while L[i]:
	C.append(subset(L[0],i+2))
	i=i+1
	L.append(item(C[i]))


def getIndex(data):
    for i in range(0,len(data)):
        if data[i].find('-')>0:
            return i

    return -1

def getIndexOfInsurance(data):
    for i in range(0,len(data)):
        if re.match("^[A-Za-z]*$",data[i]):
            return i

    return -1

frequentAge=dict()
frequentInsurance=dict()

if num_item==3:
    for i in L:
        for j in i:
            if len(j)==num_item:
                print j
                index=getIndex(j)

                if j[index] in frequentAge.keys():
                    frequentAge[j[index]]= frequentAge[j[index]] + 1
                else:
                     frequentAge[j[index]]=1

for i in L:
    for j in i:
        if len(j)==num_item:
            print j
            index=getIndexOfInsurance(j)

            if j[index] in frequentInsurance.keys():
                frequentInsurance[j[index]]= frequentInsurance[j[index]] + 1
            else:
                frequentInsurance[j[index]]=1

print frequentAge
print frequentInsurance

if num_item==3:
    plotly.offline.plot({
        "data": [{
            'labels': frequentAge.keys(),
            'values': frequentAge.values(),
            'type': 'pie',
            'marker': {'colors': ['rgb(50,57,65)', 'rgb(203,213,217)', 'rgb(53,98,114)', 'rgb(241,52,50)']},
            'hoverinfo': 'label+percent+name',
            'textinfo': 'none',
            'name': 'Age Groups',
            'domain': {'x': [0.2, .6],
                       'y': [0, .49]},
        },
            {
                'labels': frequentInsurance.keys(),
                'values': frequentInsurance.values(),
                'type': 'pie',
                'marker': {'colors': ['rgb(0,255,165)', 'rgb(0,255,255)', 'rgb(0,165,255)', 'rgb(53,98,114)']},
                'hoverinfo': 'label+percent+name',
                'textinfo': 'none',
                'name': 'Insurance Type',
                'domain': {'x': [0.2, .6],
                           'y': [.51, 1]},
            }
        ],
        "layout": go.Layout(
            title="Results")
    })

else:
    plotly.offline.plot({
        "data": [
            {
                'labels': frequentInsurance.keys(),
                'values': frequentInsurance.values(),
                'type': 'pie',
                'marker': {'colors': ['rgb(50,57,65)', 'rgb(203,213,217)', 'rgb(53,98,114)', 'rgb(241,52,50)']},
                'hoverinfo': 'label+percent+name',
                'textinfo': 'none',
                'name': 'Insurance Type',
            }
        ],
        "layout": go.Layout(
            title="Results")
    })


