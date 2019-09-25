from crypto_news_api import CryptoControlAPI

API_AUTH = 'b8d3767b03073fb38780eb1de50198ea'

# Connect to the CryptoControl API
api = CryptoControlAPI(API_AUTH)

# Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
proxyApi = CryptoControlAPI(API_AUTH, "http://cryptocontrol_proxy/api/v1/public")

def latest_news(lang="po"):
    return api.getLatestNews(lang)