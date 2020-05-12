import pandas as pd
import csv

#Solution suggested in the task content.
#df=pd.read_csv("./train.tsv")
#It doesn't work very well, because not all rows and not all columns are visible. Besides, the dividing character in this file is the tab, which with the formula above is visible as the string '\ t'.

#Below are my suggestions for changes.

#To make all rows visible, we turn on the display of all rows.
pd.set_option('display.max_rows', None)

#To make all columns visible, we turn on the display of all columns.
pd.set_option('display.max_columns', None)

#Without this setting, the above settings are displayed incorrectly (all columns should be in the same line).
pd.set_option('display.width', None)

#To maximize the width in characters of a column (data from the last column will be fully displayed).
pd.set_option('display.max_colwidth', None)

#We set delimiter to indicate dividing character.
df=pd.read_csv("./train.tsv", delimiter='\t')
print(df)




