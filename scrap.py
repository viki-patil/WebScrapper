import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging


flipkart_url="https://www.flipkart.com/search?q="+"iphone12pro"

urlclient=urlopen(flipkart_url)

#print(urlclient.read())
flipkart_page=urlclient.read()

flipkart_html=bs(flipkart_page,'html.parser')

bigbox=flipkart_html.findAll("div",{"class":"_1AtVbE col-12-12"})

print(len(bigbox))
#/apple-iphone-12-pro-pacific-blue-512-gb/p/itm8a39d6779b04e?pid=MOBFWBYZTHSXKMGW&lid=LSTMOBFWBYZTHSXKMGWYPOFI5&marketplace=FLIPKART&q=iphone12pro&store=tyy%2F4io&srno=s_1_17&otracker=search&otracker1=search&fm=Search&iid=74603202-9f8b-4af7-8f84-456ca5cfe44a.MOBFWBYZTHSXKMGW.SEARCH&ppt=sp&ppn=sp&ssid=a8onkuoce80000001691109874603&qH=712933e6bd68e7b9
del bigbox[0:2]
del bigbox[-3:]
print(len(bigbox))

for i in range(len(bigbox)):
    print(bigbox[i].div.div.div.a['href'])

print(len(bigbox))