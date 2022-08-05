import csv
import pandas as pd
def remove_duplicate():
    data  = pd.read_csv('group_input_new.csv')
    length = len(data["Keyword"])
    ckeyword = data["Keyword"]
    clink= data["Link"]
    Links = []
    i = 0
    d=0
    while i < length :
        mylist = []
        key = ckeyword[i] 
        for j in range(i , length):
            next_key = ckeyword[j]
            if key == next_key : 
                link = clink[j]
                mylist.append(link)
                print(mylist)
                
            else:
                i = j 
                Links.append(mylist)
                break
            if j == length - 1 :
                Links.append(mylist)
                i=j+1         
    data.drop(['Link','Position','Title','Snippet','Primary Intents','Secondary Intents','Client Ranking URL','Client Ranking Position','Client URL Ranking Count','CPC','CPS','Difficulty','Current Traffic','Potential Traffic','Current Value','Potential Value','Fibonacci Helper','Value Opportunity','Volume Opportunity','Competitor Score','Competitor ranking count','Related Results Count'] , inplace = True, axis = 1)
    data.drop_duplicates(subset=['Keyword'],inplace =True )
    data.reset_index(drop  = True, inplace = True)
    data['Links'] = pd.Series(Links)
    data.to_csv('new_input.csv')
 
class nodes():
    keyword = None
    volume = None 
    links = None 




def node():   
    df = pd.read_csv('new_input.csv')
    del(df['#'])
    with open('new_input.csv','r') as f:
        reader = csv.DictReader(f)
        data=list(reader)
    row_list= []
    for index in range(0,len(df['Keyword'])):
        my_list=nodes()
        my_list.keyword = data[index]['Keyword']
        my_list.volume = data[index]['Volume']
        my_list.links = data[index]['Links']
    row_list.append(my_list)


if __name__ == "__main__":
    #remove_duplicate()
    node()