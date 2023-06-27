import mariadb as mdb
import requests
from bs4 import BeautifulSoup
from datetime import timedelta

page = 1
while True:
        url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=3d9d4e4b-5669-4298-a12c-4da8977181f2&page=1"

        r =requests.get(url)
        #print(r)

        htmlcontent = r.content
        soup = BeautifulSoup(r.content,"html.parser")
        # for link in soup.find_all(class_="yFHi8N"):

        Name1 = []
        price1 = []

        for listing in soup.find_all(class_='_4rR01T'):
            Name1.append(listing.text)

        for listing in soup.find_all(class_='_30jeq3 _1_WHN1'):
            a = (listing.text)
            a = a[1:]
            if "," in a:
                
                index = a.index(",")
                amount = a[0:index] + a[index+1:]
                price1.append(int(amount))
            else:
                price1.append(int(amount))
        conn = mdb.connect(
            user="root",
            password="1234",
            host="localhost",
            port=3307,
            database='demo'

        )
        cur = conn.cursor()

        # for Name, Price in zip(Name1, price1

    # Get Cursor
    
        for Name, Price in zip(Name1, price1):
        # print(Name ,Price)
            query = "insert into mobiles (Name,Price) value(%s,%s)"

            data = (Name, Price)
            cur.execute(query,data)

        page +=1 
        url.replace("url.index(url[-1])",'page')


        print(cur.rowcount, "record inserted.")
        if page ==339:
         break
        conn.commit()


# Connect to the databas
conn = mdb.connect(
    user="root",
    password="1234",
    host="localhost",
    port=3307,
    database='demo'

)

# Create a cursor object
cur = conn.cursor()

# Execute a query
query = "SELECT * FROM mobiles"
cur.execute(query)

# Retrieve the data
data = cur.fetchall()
print((data))


import pandas as pd
df = pd.DataFrame(data) 
print(df) 
df.to_csv("20-06-2023 1.csv")

# conn.commit()
cur.close()
conn.close()
