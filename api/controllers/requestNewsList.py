from crypto_news_api import CryptoControlAPI

API_AUTH = 'b8d3767b03073fb38780eb1de50198ea'

# Connect to the CryptoControl API
api = CryptoControlAPI(API_AUTH)

# Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
proxyApi = CryptoControlAPI(API_AUTH, "http://cryptocontrol_proxy/api/v1/public")

# Enable the sentiment datapoints
api.enableSentiment()

# Get top news
print(api.getTopNews())

# get latest russian news
print(api.getLatestNews("po"))

# get top bitcoin news
print(api.getTopNewsByCoin("bitcoin"))

# get top EOS tweets
print(api.getTopTweetsByCoin("eos"))

# get top Ripple reddit posts
print(api.getLatestRedditPostsByCoin("ripple"))

# get reddit/tweets/articles in a single combined feed for NEO
print(api.getTopFeedByCoin("neo"))

# get latest reddit/tweets/articles (seperated) for Litecoin
print(api.getLatestItemsByCoin("litecoin"))

# get details (subreddits, twitter handles, description, links) for ethereum
print(api.getCoinDetails("ethereum"))