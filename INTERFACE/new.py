
from ast import keyword
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import pprint
import requests
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
#nltk.download('stopwords')
#print('hi')
def stopwords_remove(para):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(para)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence=[i for i in filtered_sentence if len(i)>=2]
  return filtered_sentence


def select_regect(para,word):
    keyword=word.split(" ")
    for j in keyword:
        for i in para:
           if str(i.lower())==str(j.lower()):
                return True
    return False 
#filtering the key_word       


def paragraph(para,key_word):
    filter_para=stopwords_remove(para)
    sent=select_regect(filter_para,str(key_word))
    if sent == True:
       return para
    else:
         return "no keyword found"

def solution(a_text,key_word):
    a=[]
    stop_words=stopwords_remove(a_text)
    a=select_regect(stop_words,str(key_word))
    return a



def reverse_date(date):
   date=str(date)
   date=date.split("-")
   s=""
   s=date[1]+"/"+date[2]+"/"+date[0]
   return s               

def company_details(c_name,key_word,date1,date2):
            try :
                text=""
                googlenews=GoogleNews(start=str(date1) ,end=str(date2))
                googlenews.search(c_name)
                results=googlenews.result(sort = True)
                for i in range(len(results)):
                    website = results[i]["link"]
                    article = Article(website)
                    article.download()
                    article.parse()
                    article.nlp()
                    a_text=article.text
                    b=solution(a_text,key_word)
                    if b==True:
                        text+=a_text
                return text
            except:
                if len(text)!=0:
                    return text
                else:
                    return 'no news found or please check start date and end date.'
#df=pd.DataFrame(results)
#b=solution(df,key_word)
                
#df = company_details ('ABB','south',"05/01/2022","05/30/2022")
#print(df)
#['06/14/2022', '06/24/2022']
#date  = reverse_date('06/14/2022')
#print(date)

