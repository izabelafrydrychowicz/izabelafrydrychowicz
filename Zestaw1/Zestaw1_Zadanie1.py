import pandas as pd

#Read the file, name the columns.
df_two=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'])

#Calculate the mean of the 'price' column. The result was in the thousands, so change it to PLN. Changing the result to integer numbers.
mean_two=int(df_two['price'].mean()*1000)

#Create a new dataframe with mean price.
data=[{'Mean price':mean_two}]
df_one=pd.DataFrame(data)

#Save dataframe as csv.
df_one.to_csv(r'out0.csv', index=False)