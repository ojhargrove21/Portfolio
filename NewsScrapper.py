from bs4 import BeautifulSoup
from googlesearch import search
import requests
from transformers import pipeline
import datetime
import time

import tensorflow
from GoogleNews import GoogleNews
emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
summarizer = pipeline('summarization')
dateStart=datetime.datetime.now() - datetime.timedelta(days=336)
dateStart = datetime.date(2023,5,31)
periodEnd = dateStart-datetime.timedelta(days=3)
dateStartF = str(dateStart.year)+'-'+str(dateStart.month)+'-'+str(dateStart.day)
periodEndF = str(periodEnd.year)+'-'+str(periodEnd.month)+'-'+str(periodEnd.day)

print(dateStartF)
print(periodEndF)
from csv import writer


def getNewsData(day,month,year,day2,month2,year2):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Windows64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
    response = requests.get(f'https://www.google.com/search?q=News&num=30&gl=us&sxsrf=APwXEdcBFuRuIfBxgWGezNrKYrUM_ayjjw%3A1685486613895&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{day}%2F{year}%2Ccd_max%3A{month2}%2F{day2}%2F{year2}&tbm=nws', headers=headers)
    soup=BeautifulSoup(response.content, "html.parser")
    newsresults=[]
    for el in soup.select('div',{'class':'MBeu0'}):
        print(el.get_text())
        newsresults.append(el.get_text())
    return newsresults

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
    print(f"requesting{url}")
    try:
        response = requests.get(url,timeout=5)
        print((response.text))
        return response.text

    except:
        pass
    # response will be provided in JSON format
    return "data not found"
counter = 0
while dateStart<datetime.date(2023,6,9):
    print(dateStartF)
    print(periodEndF)
    query = f'google breaking news after:{dateStartF} before:{periodEndF}'
    dataStr = ''
    year = dateStartF.split('-')[0]
    month = dateStartF.split('-')[1]
    day = dateStartF.split('-')[2]
    yearF = periodEndF.split('-')[0]
    monthF = periodEndF.split('-')[1]
    dayF = periodEndF.split('-')[2]
    # search=f'https://www.google.com/search?q=breaking+news&rlz=1C1UEAD_enUS965US965&sxsrf=APwXEdcGVmzhkyPEQJoWWmYtrqMesPq59w%3A1685376594061&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{day}%2F{year}%2Ccd_max%3A{month}%2F{day+3}%2F{year}&tbm='
    # search=f'https://www.google.com/search?q=news&rlz=1C1UEAD_enUS965US965&biw=1366&bih=617&sxsrf=APwXEdcwraPuAxGoP1oUUW6mBrLkSn5-Yg%3A1685449174856&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{month}%2F{day}%2F{year}%2Ccd_max%3A{month}%2F{day+3}%2F{year}&tbm=nws'
    # req = requests.get(search).content
    # Soup = BeautifulSoup(req, 'html.parser')
    # Titles = []
    # for i in Soup.find_all('a'):
    #     Titles.append(i.text)
    # print(Soup.prettify())
    # print(Titles)
    time.sleep(2)

    titles=getNewsData(day,month,year,dayF,monthF,yearF)

    for para in titles:
        # data.write(para.get_text()+"\n")
        dataStr += para+"\n"

    print(wordFrequency(dataStr))
    wordsFormated = []
    for key, val in wordFrequency(dataStr).items():
        if len(key)<10 and key.isnumeric()==False and len(key)>0:
            wordsFormated.append((key,val))

    emotions = []
    i = 0
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for word,value in wordsFormated:

        emotion_label = emotion(word)
        dic = emotion_label[0]
        d = list(dic.values())
        #print(d)
        #admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment,
        # disapproval, disgust, embarrassment, excitement, fear, gratitude, grief,
        # joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

        if d[0]=='admiration':
            counts[0]+=1
        elif d[0]=='amusement':
            counts[1]+=1
        elif d[0]=='anger':
            counts[2]+=1
        elif d[0]=='annoyance':
            counts[3]+=1
        elif d[0]=='approval':
            counts[4]+=1
        elif d[0]=='caring':
            counts[5]+=1
        elif d[0]=='confusion':
            counts[6]+=1
        elif d[0]=='curiosity':
            counts[7]+=1
        elif d[0]=='desire':
            counts[8]+=1
        elif d[0]=='disappointment':
            counts[9]+=1
        elif d[0]=='disapproval':
            counts[10]+=1
        elif d[0]=='disgust':
            counts[11]+=1
        elif d[0]=='embarrassment':
            counts[12]+=1
        elif d[0]=='excitement':
            counts[13]+=1
        elif d[0]=='fear':
            counts[14]+=1
        elif d[0]=='gratitude':
            counts[15]+=1
        elif d[0]=='grief':
            counts[16]+=1
        elif d[0]=='joy':
            counts[17]+=1
        elif d[0]=='love':
            counts[18]+=1
        elif d[0]=='nervousness':
            counts[19]+=1
        elif d[0]=='optimism':
            counts[20]+=1
        elif d[0]=='pride':
            counts[21]+=1
        elif d[0]=='realization':
            counts[22]+=1
        elif d[0]=='relief':
            counts[23]+=1
        elif d[0]=='remorse':
            counts[24]+=1
        elif d[0]=='sadness':
            counts[25]+=1
        elif d[0]=='surprise':
            counts[26]+=1
        else:
            counts[27]+=1
        print(f'{i}of{len(wordsFormated)}')
        i+=1
        emotions.append((emotion_label,(word,value)))
    print(counts)

    print(wordsFormated)
    print(emotions)
    csum = 0
    for num in counts:
        csum+=num
    countsAvg = [counts[0]/csum,counts[1]/csum,counts[2]/csum,counts[3]/csum,counts[4]/csum,counts[5]/csum,counts[6]/csum,counts[7]/csum,counts[8]/csum,counts[9]/csum,counts[10]/csum,counts[11]/csum,counts[12]/csum,counts[13]/csum,counts[14]/csum,counts[15]/csum,counts[16]/csum,counts[17]/csum,counts[18]/csum,counts[19]/csum,counts[20]/csum,counts[21]/csum,counts[22]/csum,counts[23]/csum,counts[24]/csum,counts[25]/csum,counts[26]/csum,counts[27]/csum]
    PNList = [dateStartF,countsAvg[0],countsAvg[1],countsAvg[2],countsAvg[3],countsAvg[4],countsAvg[5],countsAvg[6],countsAvg[7],countsAvg[8],countsAvg[9],countsAvg[10],countsAvg[11],countsAvg[12],countsAvg[13],countsAvg[14],countsAvg[15],countsAvg[16],countsAvg[17],countsAvg[18],countsAvg[19],countsAvg[20],countsAvg[21],countsAvg[22],countsAvg[23],countsAvg[24],countsAvg[25],countsAvg[26],countsAvg[27]]
    with open('StockSentament.csv', 'a') as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

    # Pass the list as an argument into
    # the writerow()
        print('writing')
        writer_object.writerow(PNList)

    # Close the file object
        f_object.close()
    dateStart=dateStart + datetime.timedelta(days=1)
    periodEnd = dateStart-datetime.timedelta(days=3)
    dateStartF = str(dateStart.year)+'-'+str(dateStart.month)+'-'+str(dateStart.day)
    periodEndF = str(periodEnd.year)+'-'+str(periodEnd.month)+'-'+str(periodEnd.day)
    counter+=1
