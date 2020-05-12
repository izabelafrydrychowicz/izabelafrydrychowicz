import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'])

#Using the following command we get list of all columns with their data types and memory usage.
print(df.info())
#Exercise: what type of data is it?
#Cena - ciągłe
#Liczba pokoi - dyskretne
#Wielkość mieszkania - ciągłe
#Piętro - dyskretne
#Adres - jakościowe (niemierzalne)
#Opis - jakościowe (niemierzalne)