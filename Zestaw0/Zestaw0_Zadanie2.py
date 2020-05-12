import pandas as pd


#To make all rows visible, we turn on the display of all rows.
pd.set_option('display.max_rows', None)

#To make all columns visible, we turn on the display of all columns.
pd.set_option('display.max_columns', None)

#Without this setting, the above settings are displayed incorrectly (all columns should be in the same line).
pd.set_option('display.width', None)

#To maximize the width in characters of a column (data from the last column will be fully displayed).
pd.set_option('display.max_colwidth', None)

#Exercise: naming columns:
df=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'])

#Exercise: print one column
print(df['address'])

#Exercise: print two columns
df_two=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'], usecols=['address','price'])
print(df_two)

#Exercise: print all columns (last column fully displayed)
print(df)






