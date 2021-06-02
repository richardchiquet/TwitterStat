# -*- coding: utf-8 -*-
"""
Created on Tue May 25 05:46:54 2021

@author: ricky
"""


"""
This programme collect trends in a city
then it collects tweet on different trends and saved them in a dataframe
then a dictionary of itaration of words
then some stats on these iterations are save in a csv

Everytime that programme is launched a new line is created on the csv.
"""


import tweepy
from Trends import TrendsCity
from datetime import datetime
from Tweet import Tweet
from copy import copy
import pandas as pd
from simple_map import Simple_map
import numpy as np
import time
import statistics as st

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

final_df=None

#Parameter
city="Paris"
trends_iteration=10
Number_tweets_per_trend=50
language_of_tweets="fr"
minimum_lengh_per_word=5



if __name__ == '__main__':

    #Trends collect in a certain city
    Trends_Paris = TrendsCity(api, city, trends_iteration)
    print(Trends_Paris.df_trends_city)
    
    topics = Trends_Paris.L_trends
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %HH%M")
    first=True
    topic_treated=0
    
    
    #Tweets collect
    for topic in topics:
        if first==True:
            tweets_topic = Tweet(api, topic[0], city, Number_tweets_per_trend, language_of_tweets, date_time)
            
            tweets_topic.set_df_tweet_without_geo()
            final_df_tweet=tweets_topic.df_tweet
            first=False
            topic_treated+=1
            print("Topic treated:"+str(topic_treated)+"("+topic[0]+")")
        else:
            tweets_topic = Tweet(api,topic[0],city,Number_tweets_per_trend,language_of_tweets,date_time) 
            df_tweet=copy(tweets_topic.df_tweet)
            final_df_tweet =pd.concat([final_df_tweet,df_tweet],ignore_index=True,sort=False)
            topic_treated+=1
            print("Topic treated:"+str(topic_treated)+"("+topic[0]+")")
    
    
    #Definition of a dictionary of itaration of words
    first = True
    
    for i in final_df_tweet.index:
        if first==True:
            text = final_df_tweet["Text"][i]
            map_Word=Simple_map(text,minimum_lengh_per_word)
            first=False
        else:
            text = final_df_tweet["Text"][i]
            map_Word.add_txt(text)
    
    #Some data that can be useful to save
    date_time = now.strftime("%m/%d/%Y, %HH%M")
    map_Word.set_df()
    map_Word.set_list()
    df = copy(map_Word.df)
    L = map_Word.list
    

    L_temp=[[len(L),st.mean(L),max(L),st.median(L),st.median_high(L),st.median_low(L),date_time]]
    
    
    
    df_temp=pd.DataFrame(np.array(L_temp),columns=["different word number","Mean","Max","Median","MedianH","MedianL","Date/Hour"])
    #final_df = pd.concat([final_df,df_temp],ignore_index=True,sort=False)
    
    df_temp.to_csv('dataV1.csv',sep='|',mode='a',header=False)
