# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:39:37 2021

@author: ricky
"""
 

"""
The class TrendsCity allows to collect trends in a certain place (as city)

In that file there is a fonction (AvailableCity) which allows to knows which places can be used with the class TrendsCity
"""

import pandas as pd
import numpy as np
import time





class TrendsCity():
    def __init__(self,api,city,loop):
        self.api = api
        self.city=city
        self.loop = loop
        self.L_trends=[]
        self.df_trends_city=self.set_df_trends_City()
        self.pourcent=0
        
    
    def get_Woeid(self):
                               
        df_city = AvailableCity(self.api)
        niceline = df_city.loc[df_city["CityName"]==self.city]
        woeid = niceline.loc[niceline.index[0],:]["Woeid"]
        return woeid
    
    def set_df_trends_City(self):
                               
        woeid = self.get_Woeid()
        trendsInCity = self.api.trends_place(woeid)[0]
        self.pourcent=100
        
        
        for k in range(self.loop):
            L_test=[]
            time.sleep(1)
            trendsInCity = self.api.trends_place(woeid)[0]
            p=0            
            for trend in trendsInCity["trends"]:
                if k==0:
                    self.L_trends.append([trend["name"],trend["tweet_volume"]])
                    if trend["tweet_volume"]==None:
                        self.pourcent-=2
                        
                elif self.L_trends[p][1] == None and trend["tweet_volume"]!=None:
                    self.L_trends[p][1] = trend["tweet_volume"]
                    self.pourcent+=2
                p+=1                
            for L_trend in self.L_trends:{L_test.append(L_trend[1])}
            if None not in L_test:print("break");break
            print("Trends Filling Rate :"+str(self.pourcent))
        
        df =pd.DataFrame(np.array(self.L_trends),columns=["Trends_name","Tweet_Volume"])
        return df
    
    
    


def AvailableCity(api):
    Trends_available = api.trends_available()
    cities=[]
    for trend in Trends_available:
        cities.append([trend["name"],trend["country"],trend["countryCode"],trend["woeid"]])

    df_city = pd.DataFrame(np.array(cities),columns=['CityName','CountryName', 'CountryCode','Woeid'])
    return(df_city)
        

