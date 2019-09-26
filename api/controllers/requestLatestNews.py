from crypto_news_api import CryptoControlAPI

API_AUTH = 'b8d3767b03073fb38780eb1de50198ea'

# Connect to the CryptoControl API
api = CryptoControlAPI(API_AUTH)
# Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
proxyApi = CryptoControlAPI(API_AUTH, "http://cryptocontrol_proxy/api/v1/public")

infosSelect = {
    'title':[],
    'description':[],
    'source':{
        'favicon':[]
    },
    'url':[]
}
def latest_news(lang="po"):
    data = api.getLatestNews(lang)

    response = []
    for index, article in enumerate(data):
        info = {
            'id': index+1,
            'title': article['title'],
            'description': article['description'],
            'date': article['publishedAt'],
            'source': {
                'favicon': article['source']['favicon']
            },
            'url': article['url'],
            'image_article': article['originalImageUrl']
        }

        response.append(info)
    
    return response

if __name__ == "__main__":
    print(latest_news())