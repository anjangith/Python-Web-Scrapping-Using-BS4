#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[86]:


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[4]:


url="https://www.cricbuzz.com/cricket-news/editorial/stats-analysis"
newsurl="https://www.indiatoday.in/news.html"
stockurl="https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html"


# In[5]:


r=requests.get(url)
n=requests.get(newsurl)
q=requests.get(stockurl)


# In[6]:


soup=BeautifulSoup(r.content,'html5lib')
noop=BeautifulSoup(n.content,'html5lib')
doop=BeautifulSoup(q.content,'html5lib')


# In[7]:


p=soup.find_all(class_="cb-nws-hdln-ancr text-hvr-underline")


# In[8]:


s=soup.find_all(class_="cb-nws-intr")

print("\n____________________________Source:CrickBuzz________________________________")


# In[9]:


for i in range(10):
    print(p[i].text)
    print(s[i].text)
    print("\n")


# In[10]:


x=noop.find_all('span',{'class':'widget-title'})


# In[11]:


title1=x[0].next.text
sec1=x[0].next.next.next.find_all('p')
head1=x[0].next.next.next.next.next.text

title2=x[1].next.text
sec2=x[1].next.next.next.find_all('p')
head2=x[1].next.next.next.next.next.text

title3=x[2].next.text
sec3=x[2].next.next.next.find_all('p')
head3=x[2].next.next.next.next.next.text

title4=x[3].next.text
sec4=x[3].next.next.next.find_all('p')
head4=x[3].next.next.next.next.next.text


title5=x[4].next.text
sec5=x[4].next.next.next.find_all('p')
head5=x[4].next.next.next.next.next.text

title6=x[5].next.text
sec6=x[5].next.next.next.find_all('p')
head6=x[5].next.next.next.next.next.text

print('\n Source:_______________INDIA TODAY___________________')


# In[12]:


print(title1+"\n")
print(" "+head1)
for i in sec1:
    print (i.text.encode('utf-8'))
    
print("\n")
    
print(title2+"\n")
print(" "+head2)
for i in sec2:
    print (i.text.encode('utf-8'))

print("\n")
    
print(title3+"\n")
print(" "+head3)
for i in sec3:
    print (i.text.encode('utf-8'))

print("\n")
    
print(title3+"\n")
print(" "+head3)
for i in sec3:
    print (i.text.encode('utf-8'))

print("\n")
    
print(title4+"\n")
print(" "+head4)
for i in sec4:
    print (i.text.encode('utf-8'))

print("\n")
    
print(title4+"\n")
print(" "+head4)
for i in sec4:
    print (i.text.encode('utf-8'))

print("\n")
    
print(title5+"\n")
print(" "+head5)
for i in sec5:
    print (i.text.encode('utf-8'))    

print("\n")
    
print(title6+"\n")
print(" "+head6)
for i in sec6:
    print (i.text.encode('utf-8'))
    
print("\n")
    
    

    


# In[15]:

print("Stock prices: Source-Money Control")
table=doop.find('table',class_="tbldata14 bdrtpg")


# In[87]:


m=[]
x=table.find_all('tr')

for index,row in enumerate(x):
    if(index==0):
        k=row.find_all('th')
        m.insert(index,[k[0].text,k[1].text,k[2].text,k[3].text,k[4].text,k[5].text])
        
        
       
    else:
        l=row.find_all('td')
        m.insert(index,[l[0].b.text,l[1].text,l[2].text,l[3].text,l[4].text,l[5].text])
        
       
       
       


# In[88]:


df=pd.DataFrame(m);
print(df)


# In[ ]:




