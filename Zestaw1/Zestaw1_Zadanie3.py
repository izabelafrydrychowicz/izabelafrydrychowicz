import pandas as pd
import csv
import numpy as np

#Read the file, name the columns.
df=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'])

#Create dictionary for descriptions from description.csv file.
descriptionDictionary={}

#Open description.csv file. We will look for the appropriate value in this dictionary.
with open('description.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #Add values to dictionary.
        descriptionDictionary[row[0]]=row[1]

#Create a new list with description. We will add this list as a column to df.
descriptions=[]

#Check which floor and assign the appropriate value from the description.csv file (from dictionary).
for row in df['floor_number']:
    if str(row) in descriptionDictionary.keys():
        value=descriptionDictionary[str(row)]
    else:
        value=''
    descriptions.append(value)

#Add new column to df with descriptions.
df['description']=descriptions

#Create a new csv file.
df.to_csv(r'out2.csv', index=False)