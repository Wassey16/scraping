import csv
import pandas as pd 

df = pd.read_csv("sample.csv")
df.dropna(axis = 0, how ='any', thresh = None, subset =['Keyword','Volume'], inplace = True)
df['CPC'] = df['CPC'].fillna(1)
df['CPS'] = df['CPS'].fillna(0.1)
with open('sample.csv','r') as f:
        reader = csv.DictReader(f)
        data=list(reader)
ch='-'
my_list=[]
for index in range(0,len(df['Keyword'])):#len(df['Keyword'])):
    my_str=data[index]['Volume']
    if ch in my_str:
        new_str = my_str.split("-")
        a = new_str[0]
        b = new_str[1]
        if a > b:
            my_list.append(a)
        else:
            my_list.append(b)
    else:
        my_list.append(my_str)
df.drop(['Volume'], inplace = True,axis = 1)
df['Volume']=pd.Series(my_list)
df.to_csv("new_CleanInput.csv")
# my = ali.split('-')
# a=my[0]
# b=my[1]
# print(a,b)
# if a > b:
#     c=a
# else:
#     c=b
# print(c)
#df.to_csv("new_CleanedUpInput.csv")

 