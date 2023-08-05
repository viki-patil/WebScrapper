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


#print(len(bigbox))
#
#for i in bigbox:
#    print("https://www.flipkart.com"+i.div.div.div.a['href']+"\n")
#
#print(len(bigbox))

product_link="https://www.flipkart.com"+bigbox[0].div.div.div.a['href']

product_req=requests.get(product_link)
product_html=bs(product_req.text,'html.parser')

print(product_link)

product_boxes=product_html.findAll("div", {"class":"_16PBlm"})

print(len(product_boxes))
del product_boxes[-1:]

print(product_boxes[0].div.div.find("p",{"class":"_2sc7ZR _2V5EHH"}).text)

allreview=[]
for i in product_boxes:
    print("Reviewer Name")
    print(i.div.div.find("p",{"class":"_2sc7ZR _2V5EHH"}).text)
    print("Reviewer Rating")
    print(i.div.div.find("div",{"class":"_3LWZlK _1BLPMq"}).text)
    print("Description")
    print(i.div.div.find("div",{"class":""}).text)

    review={
        "name":i.div.div.find("p",{"class":"_2sc7ZR _2V5EHH"}).text,
        "rating":i.div.div.find("div",{"class":"_3LWZlK _1BLPMq"}).text,
        "description":i.div.div.find("div",{"class":""}).text
    
    }
    allreview.append(review)


print(allreview)


