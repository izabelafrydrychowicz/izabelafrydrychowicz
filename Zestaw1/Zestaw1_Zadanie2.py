import pandas as pd

#Read the file, name the columns.
df=pd.read_csv("./train.tsv", delimiter='\t', names=['price', 'number_of_rooms', 'size_of_the_apartment', 'floor_number', 'address', 'description'])

#Add column with price per square meter.
df['price_per_square_meter']=df['price']/df['size_of_the_apartment']

#Calculate mean for price per square meter.
mean_price_per_square_meter=df['price_per_square_meter'].mean()

#Create variable for first condition (= or > than 3 rooms).
three_rooms=df['number_of_rooms'] >= 3

#Crwate variable for second condition (less than mean price per square meter).
less_than_mean=df['price_per_square_meter'] < mean_price_per_square_meter

#Create dataframe with both conditions and with selected columns.
df_two=pd.DataFrame(df[three_rooms & less_than_mean], columns=['price','number_of_rooms','price_per_square_meter'])

#Create a file.
df_two.to_csv(r'out1.csv', index=False, header=False)


