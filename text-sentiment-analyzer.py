import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


comment = "This is such a “Mojang” way to introduce renewable shulker shells, it’s obvious they heard the complaints of these not being renewable. Really happy to see mojang truly care about its players"

# Get text from user
text = input("What sentence would you like to analyze? \n\n")

if (text):
        comment = text

analyser = SentimentIntensityAnalyzer()

score = analyser.polarity_scores(comment)

df1 = pd.DataFrame(list(score.items()), columns=['Sentiment Metric', 'Score'])
print("\n")
print(df1)
print("\n")

sentiment1 = score.get('compound')
if sentiment1 >= 0.05:
        print("The sentence has a positive sentiment :)")
elif sentiment1 > -0.05 and sentiment1 <0.05:
        print("The sentence has a neutral sentiment :|")
elif sentiment1 <= -0.05 : #or else
        print("The sentence has a negative sentiment :(")