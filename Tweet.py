# -*- coding: utf-8 -*-
"""
Created on Tue May 25 06:18:32 2021

@author: ricky
"""

"""
The class Tweet allows to collect a certain number of tweets on a subject with or without the location

The location does not work for the moment
"""

import tweepy
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

class Tweet():
    
    
    
    def __init__(self,api,topic,place,count,languages,date):
        self.api = api
        self.topic= topic
        self.place=place
        self.count=count
        self.nom=Nominatim(user_agent="Richard Chiquet")
        self.languages=languages
        self.date=date
        self.df_tweet=self.set_df_tweet_without_geo()
        self.df_tweet_with_location=None

        
        
    #set the dataframe with tweets on the topic without the location    
    def set_df_tweet_with_geo(self):
        
        L=[]
        search_words = self.topic
        new_search = search_words + " -filter:retweets"
        lg = self.languages
        geo=self.nom.gecode(self.place)
        latitude = str(geo.latitude)
        longitude = str(geo.longitude)
        gec =(latitude,longitude,10)
        
        tweets = tweepy.Cursor(self.api.search,
                           q=new_search,
                           lang = lg,
                           geocode=gec).items(self.count)
        
        for tweet in tweets:
            L.append([tweet.text,len(tweet.text),self.topic,self.date])
        return(pd.DataFrame(np.array(L),columns=["Text","Text lenght","Topic","Date"]))
    
    #set the dataframe with tweets on the topic with the location(does not work for the moment)        
    def set_df_tweet_without_geo(self):
            
        L=[]
        search_words = self.topic
        new_search = search_words + " -filter:retweets"
        lg = self.languages

        tweets = tweepy.Cursor(self.api.search,
                               q=new_search,
                               lang = lg).items(self.count)
            
        for tweet in tweets:
            L.append([tweet.text,len(tweet.text),self.topic,self.date]) 
        return(pd.DataFrame(np.array(L),columns=["Text","Text lenght","Topic","Date"]))
    
    
    
        
        