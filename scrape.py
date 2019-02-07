import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url= requests.get('https://rbi.org.in/Scripts/BS_ViewWssExtractdetails.aspx?id=44732')
soup = BeautifulSoup(url.content, 'html.parser')

for item in table.find_all(class_='tablebg')[0].find_all("th"):
   header = item.text
table_rows=table.find_all("tr")
for tr in table_rows:
        td = tr.find_all("td")
        #row=[i.text for i in td]
        #data1=zip(header,row)
        ##data.append(row)
        #data.append(data1)
#add_data=pd.DataFrame(data)

#add_data.to_sql(con=engine, name='Data', if_exists='append',chunksize=10000)
