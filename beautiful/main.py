import requests
from bs4 import BeautifulSoup
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
#print(soup.prettify)

#title=soap.title
#print(type(title.string))

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



#soup me jitni bhi list hai unka data

# for i in soup.find_all('li'):
#         print(i.text)
       

      # ye only ak data de raha hai
       
# for i in soup.find('li'):
#         print(i.text)

# all span text
# comany=soup.find_all('span')
# for i in comany:
#         print(i.text)


#all div ka data
# comany=soup.find_all('div')
# for i in comany:
#          print(i.text)

       # isme sabhi ki price or text aa raha hai

# w=soup.find_all('div',attrs="_30jeq3 _1_WHN1")
# for i in w:
#    print(i.text)


#isse title or uska text bhi aa raha hai
# a=soup.find_all('div',attrs="_4rR01T")
# for i in a:
#         print(i.text)
# image_list=[]
# for item in soup.find_all('img',attrs='_396cs4'):
#      image_list.append(item['src'])
# print(image_list[0])
description_list=[]
for item in soup.find_all('div',attrs='col col-7-12'):
        description_list.append(item.text)
print(description_list[0])






















