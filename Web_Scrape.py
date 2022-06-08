#%%
from lxml import html
import requests
import csv
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

#%%
def web_scrape(n):
    name = []
    purpose = []
    for i in range(n):

        record = requests.get("http://3.89.180.32:8000/random_company")
        cont = html.fromstring(record.content)
        info = cont.xpath('//li/text()')

        li = [elem.split(':') for elem in info] 

        for i in range(len(li)):
            if li[i][0] == 'Name':
                name.append(li[i][1])
            elif li[i][0] == 'Purpose':
                purpose.append(li[i][1])
                break

    return name + purpose
               
#%%
a = web_scrape(51)
print(a)

#%%
#df = pd.read_csv('TEST.csv')

# Companies with Highest Sentiment Scores
#df.head(n = 10)

#Companies with Lowest Sentiment Scores
#df.tail(10)

# %%
if __name__ == "__main__":
    web_scrape(5)
