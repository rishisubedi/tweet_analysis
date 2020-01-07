# importing the tweepy module
import tweepy
# importing the csv and the re module
import csv, re
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def remove_special_char(tweet):
    return ' '.join(re.sub(r'[^a-zA-Z0-9 ]', r"", tweet).split())
    return tweet





class Sentiment:
    # class for the authentication

    def __init__(self):
        self.recent = []
        self.tweet_in_text = []

    def get_location(self):
        geolocator = Nominatim(user_agent="OpenStreetMap")  # can use other app
        location = geolocator.geocode("Election")
        print((location.latitude, location.longitude))

    def twitter(self):
        # authenticating
        consumer_key = "q2kf6wd7cZg3Xq4QHVDeW5uqm"

        consumer_secret = "MMlASPsEFQ0taqpJHYNdX7ms9ymJKqQCKyxvV4SWasIXEQp323"

        access_token = "1342197739-kPXMcjcNZjgHtN3r3Lr1iA3XFd2b8vj25BkFPAY"

        access_token_secret = "MLmXWceQx7PgIuH9NCsGMMJvPSQdvHyBDnPazWlN6eT7L"

        # Authentication module for accessing the twitter

        make_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        make_auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(make_auth)

        recent = input("Enter a keyword : ")
        no_of_items = int(input("Enter the numeric value: "))
        # search a tweet in the twitter
        self.recent = tweepy.Cursor(api.search, q=recent, lang="en").items(no_of_items)

        # creating a file
        file_tweet = open('tweet.csv', 'a')

        # use of the csv writer
        write = csv.writer(file_tweet)

        # labelling the data to find the polarity
        polarity = 0
        positive = 0
        weak_positive = 0
        strong_positive = 0
        weak_negative = 0
        strong_negative = 0
        negative = 0
        neutral = 0

        # looping through the tweets
        for tweet in self.recent:
            # Appending the tweets to the temp in the csv
            filtered_tweet = remove_special_char(tweet.text).encode('utf-8')
            # filter only the twitter text
            print(filtered_tweet)
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity  # finding the polarities

            if analysis.sentiment.polarity == 0:
                neutral += 1
            elif 0 < analysis.sentiment.polarity <= 0.4:
                weak_positive += 1
            elif 0.4 < analysis.sentiment.polarity <= 0.8:
                positive += 1
            elif 0.8 < analysis.sentiment.polarity < 1:
                strong_positive += 1
            elif -0.4 < analysis.sentiment.polarity <= 0:
                weak_negative += 1
            elif -0.8 < analysis.sentiment.polarity <= -0.4:
                negative += 1
            elif -1 < analysis.sentiment.polarity <= -0.8:
                strong_negative += 1

        # writing the user choice of tweet in the csv file
        headers = ["Tweet", "Polarity", "Review","Location"]
        data = [tweet_in_text, polarity, analysis.sentiment,self.get_location()]
        row = no_of_items
        with open('tweet.csv', 'w', newline='') as header_csv:
            writer = csv.writer(header_csv)
            # header into the csv
            writer.writerow(row for row in headers)
            # data in csv files
            for tweet in range(row):
                writer.writerow([row for row in data])

        if polarity == 0:
            print("Tweet consist of Neutral review")
        elif 0 < polarity <= 1:
            print("Tweet consist of positive review")
        elif -1 < polarity <= 0:
            print("Tweet consist of negative review")


# main function
if __name__ == '__main__':
    from textblob import TextBlob

    sa = Sentiment()
    sa.twitter()

