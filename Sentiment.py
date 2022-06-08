import csv
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from Web_Scrape import web_scrape

def sentiment(x,y):
    a = web_scrape(y)
    half = len(a)//2
    name = a[0:half]
    purpose = a[half:]
    #combime both lists
    name_purpose = [list(t) for t in zip(name, purpose)]
    print(name_purpose)
    fields = ['Company Name', 'Purpose']

    with open(x, 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(name_purpose)

    df = pd.read_csv(x)
    sentiment = SentimentIntensityAnalyzer()

    scores = []
    for name, values in df.iloc[:, 1].iteritems():
        scores.append(sentiment.polarity_scores(values))

    comp_scores = []
    for i in range(len(scores)):
        comp_scores.append(scores[i]['compound'])

    df['Compound Scores'] = comp_scores
    df = df.sort_values(by = 'Compound Scores', ascending = False)

    return df.to_csv(x)

if __name__ == "__main__":
    sentiment('TEST.csv',51)
