import requests
import csv
from datetime import date
from datetime import timedelta
import pandas as pd
from bs4 import BeautifulSoup
url='https://www.flipkart.com/search?q=mobile'
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)

soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())

#title=soap.title
#print(type(title.string)
# head_tag = soup.head
#print(head_tag)

# yesterday_product_name=[]
# yesterday_p=[]
# # isse title or uska data dekh sakte hai
# for i in soup.find_all(attrs='_4rR01T'):
#          yesterday_product_name.append(i.text)

#print(len(yesterday_product_name))


                        # yesterday
# yesterday_price=[]
# for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
#         yesterday_p.append(i.text) 
# for i in yesterday_p:
#         if "," in i:
#                 i=i[1:]
#                 index=i.index(',')
#                 price=i[0:index]+i[index+1:]
#                 yesterday_price.append(int(price))
#         else:
#                 yesterday_price.append(int(price))
#print(yesterday_price) 

           
                    #today
# today_product_name=[]
# for i in soup.find_all(attrs='_4rR01T'):
#          today_product_name.append(i.text)
# #print(len(today_product_name))
# today_p=[]
# today_price=[]

# for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
#         today_p.append(i.text) 
# for i in today_p:
#         if ',' in i:
#                 i=i[1:]
#                 index=i.index(',')
#                 price=i[0:index]+i[index+1:]
#                 today_price.append(int(price))
#         else:
#                 today_price.append(int(price))
# today_price[22]=9000 
# today_price[15]=7000
# # print(len(yesterday_price))   
# # print(len(today_price))  
 
today = date.today()  
yesterday = today - timedelta(days = 1)
# data = {
#    "mobile_name":yesterday_product_name,
#     yesterday:yesterday_price
      
#   }
# df = pd.DataFrame(data) 
# print(df.head()) 
# l1=[]
# l2=[]      
# while True:
#         dd=date.today()
#         # l1=[]
#         # l2=[]
        
#         for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
#                 l1.append(i.text) 
#         for i in l1:
#                 if ',' in i:
#                         i=i[1:]
#                 index=i.index(',')
#                 price=i[0:index]+i[index+1:]
#                 l2.append(int(price))
#         else:
#                 l2.append(int(price))
#         l2 = l2[1:]
        
#         df[dd]=l2
#         print(df.head())
#         break      
 
# # # Yesterday date
# today = date.today() 
# yesterday = today - timedelta(days = 1)
# # data = {
# #    "mobile_name":yesterday_product_name,
# #     today:today_price 
      
# #   }
# # df = pd.DataFrame(data)
# # print(df)
# # #df.to_csv('flipcart.csv')
# # Df = pd.DataFrame()
# #print(Df)

# # Df["Result"]=df[dd]<df[yesterday]
# # #print(Df)
# # result_list = Df['Result'].tolist()
# print(result_list)

# def indices(list1, target_value):
#         indices_list=[]
#         for i in range(len(list1)):
#                 if list1[i] == target_value:
#                         indices_list.append(i)
#         return indices_list
# bool_list=indices(result_list, True)
# # print(bool_list)
#print(yesterday_price)
#print(today_price)
# l1=[]
# for i in bool_list:
#     l1.append( yesterday_product_name[i])
    
#     l1.append(today_price[i])
#     l1.append(yesterday_price[i])
    
#print(l1)
# for i in range(len(today_product_name)):
#         a=yesterday_product_name.index(today_product_name[i])

o1=[]

r2=[]
r3=[]  
final = []
for i in soup.find_all(attrs='_4rR01T'):
        o1.append(i.text)
        
for i in soup.find_all(attrs='_30jeq3 _1_WHN1'):
        r2.append(i.text) 
for i in r2:
        # print(i)

        #print(i)
        if ',' in i:
                i=i[1:]
                index=i.index(',')
                price=i[0:index]+i[index+1:]
                r3.append(int(price))
        else:
                r3.append(int(price))
print((o1))
print(len(r3))
data = {
   "mobile_name":o1,
    today:r3
      
  }
df = pd.DataFrame(data) 
print(df) 
df.to_csv("17.06.2023.csv")