import requests
from datetime import date
from datetime import timedelta
import pandas as pd
from bs4 import BeautifulSoup
from autoscraper import AutoScraper
url='https://www.flipkart.com/search?q=mobile'

'''commanly used type of object
tag
navigablestring
beautipulsoap
comment'''
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)

soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())

# title=soup.title
# print(type(title.string))


#soup = BeautifulSoup('<p class="boldest">Extremely bold</p>', 'html.parser')
# tag=soup.p
# print(tag.name)

# tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
# print(tag['id'])

#PARAGRAP KI LIST FIND 
# paras=soup.find_all('p')
# print(paras)

#anchors=soup.find_all('a')
# print(anchors)

# for link in anchors:
#     print(link.get('href'))

#print(soup.find('div')['id'])

#print(soup.find('p').get_text())

#print(soup.get_text())

#html_tag = soup.html
#print(type(html_tag.parent))

# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
# print(sibling_soup.prettify())

# head_tag = soup.head
#print(head_tag)
# for i in head_tag.contents:
#      print(i)

# print(len(list(soup.descendants)))
# print(len(list(soup.children)))

        #find all string
# for string in soup.strings:
#     print((repr(string)))

# for i in soup.find_all('li'):
#         print(i.text)

# price=soup.find_all('div',attrs='_2KHMtA')
# for i in price:
#     print(i.text)

product_name=[]
yesterday_p=[]
# isse title or uska data dekh sakte hai
for i in soup.find_all(attrs='_4rR01T'):
         product_name.append(i.text)

# #print(product_name)


                        # yesterday
yesterday_price=[]
for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
        yesterday_p.append(i.text) 
for i in yesterday_p:
        if "," in i:
                i=i[1:]
                index=i.index(',')
                price=i[0:index]+i[index+1:]
                yesterday_price.append(int(price))
        else:
                yesterday_price.append(int(price))
print("yesterday  is")
#print(yesterday_price)
                        
today = date.today()
print("Today is: ", today)
 
# Yesterday date
yesterday = today - timedelta(days = 1)
#print("Yesterday was: ", yesterday) 

     
     

data = {
   "mobile_name":product_name,
  "prices":yesterday_price,
    "d":yesterday
     
   
   
  
  }

     
# # # #load data into a DataFrame object:
df_yesterday = pd.DataFrame(data)
print(df_yesterday)


# # #today
today_p=[]
today_price=[]

for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
        today_p.append(i.text) 
for i in today_p:
        if ',' in i:
                i=i[1:]
                index=i.index(',')
                price=i[0:index]+i[index+1:]
                today_price.append(int(price))
        else:
                today_price.append(int(price))
today_price[23]=9000
#print(today_price)


dATA = {
   "mobile_name":product_name,
   "prices":today_price,
    "D":today
     
   
   
  
}

     
# # # #load data into a DataFrame object:
df_today = pd.DataFrame(dATA)
#print(df_today)

# if today_price<yesterday_price:
#         var="True"
# else:
#         var="false"
        
# DATA = {
#         "mobile_name":product_name,
#         "prices":today_price,
#         'lower_price': var
     

#   }


     
# # # # #load data into a DataFrame object:
Df = pd.DataFrame()
#print(Df)

# print(df_today["prices"])
# print(df_yesterday["prices"])

Df["Result"]=df_today["prices"]<df_yesterday["prices"]
result_list = Df['Result'].tolist()
print(result_list)

def indices(list1, target_value):
        indices_list=[]
        for i in range(len(list1)):
                if list1[i] == target_value:
                        indices_list.append(i)
        return indices_list
#print(indices(result_list, True))
# print(yesterday_price)
# print(today_price)
