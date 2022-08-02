import csv
import pandas  as pd
class node:
    Serial_No= None
    Keyword = None
    Country = None
    Difficulty = None
    Volume = None
    CPC = None
    CPS = None
    Parent_Keyword = None
    Last_Update = None
    SERP_Features = None
    Global_volume = None
    Traffic_potential = None
    def p(self):
        return self.Difficulty


def data_cleaning():      
    df = pd.read_csv("input.csv")
    df.dropna(axis = 0, how ='any', thresh = None, subset =['Keyword','Volume'], inplace = True)
    df['CPC'] = df['CPC'].fillna(1)
    df['CPS'] = df['CPS'].fillna(0.1)
    df.to_csv("CleanedUpInput.csv")

def nodes():
    df = pd.read_csv('CleanedUpInput.csv')
    del(df['#'])
    with open('CleanedUpInput.csv','r') as f:
        reader = csv.DictReader(f)
        data=list(reader)
    row_list= []
    for index in range(0,len(df['Keyword'])):
        my_list=node()
        my_list.Serial_No = data[index]['Serial_No']
        my_list.Keyword = data[index]['Keyword']
        my_list.Country = data[index]['Country']
        my_list.Difficulty = data[index]['Difficulty']
        my_list.Volume = data[index]['Volume']
        my_list.CPC = data[index]['CPC']
        my_list.CPS = data[index]['CPS']
        my_list.Parent_Keyword = data[index]['Parent_Keyword']
        my_list.Last_Update = data[index]['Last_Update']
        my_list.SERP_Features = data[index]['SERP_Features']
        my_list.Global_volume = data[index]['Global_volume']
        my_list.Traffic_potential = data[index]['Traffic_potential']
        row_list.append(my_list)
        
    return row_list[18].p()
    
# tocheck if the function works properly 
f = open("file2.txt","w")
f.write(nodes())
f.close()
if __name__ == '__main__':
    #data_cleaning()
    nodes()
