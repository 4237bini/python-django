import pandas as pd
import numpy as np 
import math

Smartwatch=pd.read_csv('smartwatch4.csv')
Ratings=pd.read_csv('rating4.csv')

def popularity_recommendation():
    new_df=Ratings.merge(Smartwatch,on='smartwatch_id')
    new_df= new_df[['smartwatch_id','user_id','ratings']]
    a=new_df.groupby(['smartwatch_id'])['user_id'].count().reset_index()
    b=a.sort_values(by='user_id', ascending=False)
    popularity_list=b['smartwatch_id'].tolist()
    return popularity_list
  

popular_i=popularity_recommendation()
for i in popular_i:
    print(i)
    