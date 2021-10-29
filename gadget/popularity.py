import pandas as pd
import numpy as np 
import math

Smartphones=pd.read_csv('smartphone3.csv')
Ratings=pd.read_csv('rating3.csv')

def popularity_recommendation():
    new_df=Ratings.merge(Smartphones,on='smartphone_id')
    new_df= new_df[['smartphone_id','user_id','ratings']]
    a=new_df.groupby(['smartphone_id'])['user_id'].count().reset_index()
    b=a.sort_values(by='user_id', ascending=False)
    popularity_list=b['smartphone_id'].tolist()
    return popularity_list
  

popular_i=popularity_recommendation()
for i in popular_i:
    print(i)
    