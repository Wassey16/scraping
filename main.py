
import numpy as np
import pandas  as pd
class node:
    Serial_No= None
    Keyword = None
    Country = None
    Difficulty = None
    Volume = None
    CPC = None
    CPC = None
    Parent_Keyword = None
    Last_Update = None
    SERP_Features = None
    Global_volume = None
    Traffic_potential = None


def data_cleaning():      
    df = pd.read_csv("input.csv")
    df.dropna(axis = 0, how ='any', thresh = None, subset =['Keyword','Volume'], inplace = True)
    df['CPC'] = df['CPC'].fillna(1)
    df['CPS'] = df['CPS'].fillna(0.1)
    df.to_csv("CleanedUpInput.csv")

def nodes():
    data = pd.read_csv('CleanedUpInput.csv')
    del(data['#'])
    my_list=node()
    row_list= []
    for index, rows in data.iterrows():
        my_list=[rows.Serial_No,rows.Keyword,rows.Country,rows.Difficulty,rows.Volume,rows.CPC,rows.CPS,rows.Parent_Keyword,rows.Last_Update,rows.SERP_Features,rows.Global_volume,rows.Traffic_potential]
        row_list.append(my_list)
    print(row_list[:10])
if __name__ == '__main__':
    #data_cleaning()
    nodes()