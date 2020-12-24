# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:21:47 2020

@author: Fakhar
"""

import requests 
from bs4 import BeautifulSoup
import csv
import pandas as pd

def linkCreate():
    total_pages = 664 # here put the value of n+1
    urls=[]
    base = 'https://www.whitehouse.gov/briefings-statements/page/'
    
    for x in range(1,total_pages):
            z = base + str(x)
            urls.append(z)
            
    df = pd.DataFrame(urls)
    df.to_csv('link.csv')
       

def getTag(n):
    df = pd.read_csv('link.csv')
    saved_column = df['link']
    urls=[]
    for x in range(0,n):
        result = requests.get(saved_column[x])
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        for h2_tag in soup.find_all('h2'):
            a_tag = h2_tag.find('a')
            try:
                urls.append(a_tag.attrs['href'])
            except:
                pass 
                
        df = pd.DataFrame(urls)
        df.to_csv('file2.csv', index='false', header='false')
        



                