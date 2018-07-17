# import TextAnalysis
import JSON
import Twitter

twitter_config_file = open("$(homedir())/.twitter/twitter_sentiment1111.json")
tw_config = JSON.parse(twitter_config_file)

# println(tw_config)

Twitter.twitterauth(
            tw_config["consumer_key"],
            tw_config["consumer_secret"],
            tw_config["access_token"],
            tw_config["access_token_secret"])



# duke_tweets = Twitter.get_search_tweets(q = "Trump")
# tw = duke_tweets[1]

# println(tw)

# str = "To be or not to be..."
# sd = StringDocument(str)

# text(sd)

# language(sd)
# name(sd)
# author(sd)
# timestamp(sd)
