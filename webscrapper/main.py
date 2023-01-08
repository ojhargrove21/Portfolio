import urllib
import re

import datareader as datareader
import requests
from bs4 import BeautifulSoup
import datetime
import yfinance as yf

# providing url
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
d = format(day,'f')
m = format(month,'f')
y = format(year,'f')
date = y+"/"+m+"/"+d
def wordFrequency(string):
    # converting the string into lowercase
    string=string.lower()
    # Whenever we encounter a space, break the string
    string=string.split(" ")
    # Initializing a dictionary to store the frequency of words
    word_frequency={}
    # <a href="https://www.pythonpool.com/python-iterate-through-list/" target="_blank" rel="noreferrer noopener">Iterating</a> through the string
    for i in string:

    # If the word is already in the keys, increment its frequency
        if i in word_frequency:
            word_frequency[i]+=1

    # It means that this is the first occurence of the word
        else:
            word_frequency[i]=1
    return(word_frequency)
def getHTMLdocument(url):

    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text
urlList = ["https://news.yahoo.com/","https://www.yahoo.com/lifestyle","https://finance.yahoo.com/"]
dataStr = ""
linksList = []
data = open('data.txt','w')
links = open('links.txt','w')
for url in urlList:

    # opening the url for reading
    html = getHTMLdocument(url)

    # parsing the html file
    htmlParse = BeautifulSoup(html, 'html.parser')


    # getting all the paragraphs
    for para in htmlParse.find_all("p"):
        data.write(para.get_text()+"\n")
        dataStr += para.get_text()+"\n"
    soup = BeautifulSoup(html, 'html.parser')



    linkMatch = False
    for link in soup.find_all('a',attrs={'href': re.compile("^https://")}):
        # display the actual urls
        for url in linksList:
            if url == link.get('href'):
                linkMatch = True

        if(linkMatch==False):
            linksList.append(link.get('href'))
            links.write(link.get('href')+"\n")

    for l in linksList:
        links.write(l+"\n")
    data.write(dataStr)
links.close()
data.close()
wordList = list(wordFrequency(dataStr).items())
wordList.sort(key = lambda i:i[1])
wordList.reverse()
print(wordList)

def getStockData():
    tickerList = ['GOOG','^DJI','^IXIC','^RUT','^GSPC','CL=F','GC=F','BTC-USD','WFC','TSLA','META','AAPL','PFE','JNJ','MO','NVDA','INTC','AMD','GRMN','TXN']
    i=0
    stockDataList = []
    stockData = open('stockData.txt','r')
    stockDataList=stockData.readlines()
    for tick in tickerList:

        ticker = yf.Ticker(tick).info
        market_price = ticker['regularMarketPrice']
        previous_close_price = ticker['regularMarketPreviousClose']
        fifty_two_week_low = ticker['fiftyTwoWeekLow']
        fifty_two_week_high = ticker['fiftyTwoWeekHigh']
        fifty_two_week_Average = ticker['fiftyDayAverage']
        average_volume = ticker['averageVolume10days']
        day_low = ticker['dayLow']
        day_high = ticker['dayHigh']
        ask = ticker['ask']
        bid = ticker['bid']
        op = ticker['open']
        tradable = ticker['tradeable']




        print('Ticker: '+tick)
        print('Market Price:', market_price)
        print('Previous Close Price:', previous_close_price)
        print("52 low : ",fifty_two_week_low)
        print("52 high : ",fifty_two_week_high)
        print("52 average : ",fifty_two_week_Average)
        print("day low",day_low)
        print("day high",day_high)
        print("average volume : ",average_volume)
        print("ask : ",ask)
        print("bid : ",bid)
        print("open : ",op)
        print("tradable : ",tradable)
        print("day : ",date)
        print("\n")
        mp = format(market_price,'f')
        pc = format(previous_close_price,'f')
        low52 = format(fifty_two_week_low, 'f')
        high52 = format(fifty_two_week_high,'f')
        avg52 = format(fifty_two_week_Average,'f')
        dayLow = format(day_low,'f')
        dayHigh = format(day_high,'f')
        avgVol = format(average_volume,'f')
        #a = format(ask,'f')
        #b = format(bid,'f')
        o = format(op,'f')
        trad = format(tradable,'f')


        stockDataList.append(tick+"|"+mp+"|"+pc+"|"+low52+"|"+high52+"|"+avg52+"|"+dayLow+"|"+dayHigh+"|"+avgVol+"|"+o+"|"+trad+"|"+date+"\n")
        stockData.close()
        stockData = open('stockData.txt','w')

    stockData.writelines(stockDataList)
    stockData.close()
    #print(ticker)

getStockData()
