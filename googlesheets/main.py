import gspread
import datetime
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
def request():
 productlist=[]
 for i in range(2,5):
  content=requests.get( f'https://www.amazon.com/s?k=charger&page={i}&crid=OYCBNTAXXYCO&qid=1719298781&sprefix=charger%2Caps%2C562&ref=sr_pg_{i}',headers=headers).text
  html_tags=BeautifulSoup(content,"lxml")
  products=html_tags.find_all("div",class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small gsx-ies-anchor sg-col-12-of-16")

  for index,product in enumerate(products):
         product_name=product.find("span", class_="a-size-medium a-color-base a-text-normal").text
         href=product.find( "a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")['href']
         reviews=product.find("span",class_="a-size-base s-underline-text").text
         buyers_no=product.find("span",class_="a-size-base a-color-secondary").text
         data=[product_name,"https://www.amazon.com"+href,reviews,buyers_no.split(" ")[0]]
         productlist.append(data)
 return productlist

def output(data):
    gc=gspread.service_account(filename='code.json')
    sh=gc.open('scrapetosheet').sheet1
    header=["product_name","href","reviews","buyers_no"]
    sh.append_row(header)
    sh.append_rows(data)
    return








data=request()
output=output(data)