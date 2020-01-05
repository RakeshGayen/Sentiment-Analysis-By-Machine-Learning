from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = "VGd44jeIukmEx9YNMfLy8km9t"
consumerSecret = "UCiZGBeGmIOi9NnWqz7id4Dn1PzA7jGpDj2DCmRV021PPQEG9V"
accessToken = "1048139889005535232-lUvtbLGhvb3wPHp35qu8eMk025WISf"
accessTokenSecret = "O8VigYboHMa8m9Tr62ZU3osPZ3RDFNyi0kQQiaYDwh6zj"


auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth,set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("Enter keyword to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0




for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity


    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)


positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + "Tweets.")

if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print(" Positive")



labels = ['Positive ['+str(positive)+'%]', 'Neutral [' +str(neutral)+'%]', 'Negative [' +str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.title('How poeple are reacting on '+searchTerm+'by analyzing '+str(noOfSearchTerms)+'Tweets.')
plt.axis('equal')
plt.tight_layout()
plt,show()
