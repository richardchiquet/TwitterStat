# -*- coding: utf-8 -*-
"""
Created on Mon May 31 00:42:02 2021

@author: ricky
"""

"""
The class Simple_map take a string in parameter and create a dictionary which count the iteration by word
limite allows to exclude words which are too short

"""

import numpy as np
import pandas as pd

class Simple_map():
    
    
    def __init__(self,txt,limit):
        self.txt=txt
        self.limit=limit
        self.dict_word={}
        self.set_dict_word()
        self.df=None
        self.list=[]
    
    
    
    #set the dictionary with the String in argument
    def  set_dict_word(self):
        split =self.txt.split()
        for word in split:
            if len(word)>=self.limit:
                if word not in self.dict_word:
                    self.dict_word[word]=1
                else:
                    self.dict_word[word]+=1
    
    
    #add String to Dictionnary
    def add_txt(self,txt):
        split =txt.split()
        for word in split:
             if len(word)>=self.limit:
                if word not in self.dict_word:
                    self.dict_word[word]=1
                else:
                    self.dict_word[word]+=1
                    
    
    #define a list which has only iteration
    def set_list(self):
        for key, value in self.dict_word.items():
            self.list.append(value)
                    
    #set the dataFrame with the dictionnay
    def set_df(self):
        
        L_temp=[]
        
        for key, value in self.dict_word.items():
            temp = [key,int(value)]
            L_temp.append(temp)
            
        self.df=pd.DataFrame(np.array(L_temp),columns=["Word","Iteration"])
        
                    
                    