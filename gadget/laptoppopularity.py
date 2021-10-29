import pandas as pd
import numpy as np 
import math

Laptop=pd.read_csv('laptop5.csv')
Ratings=pd.read_csv('rating5.csv')

def popularity_recommendation():
    new_df=Ratings.merge(Laptop,on='laptop_id')
    new_df= new_df[['laptop_id','user_id','ratings']]
    a=new_df.groupby(['laptop_id'])['user_id'].count().reset_index()
    b=a.sort_values(by='user_id', ascending=False)
    popularity_list=b['laptop_id'].tolist()
    return popularity_list
  

popular_i=popularity_recommendation()
for i in popular_i:
    print(i)
    