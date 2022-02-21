from datetime import datetime, timedelta
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
PRICE_DELTA = 0.05
STOCK_API_KEY = "K6U5MQ4DO3RRHQ4V"
STOCK_URL = "https://www.alphavantage.co/query?"

NEWS_API_KEY = "81ec7f7bdd2f485ab7d29e40afee8a51"
NEWS_URL = "https://newsapi.org/v2/everything?"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_price_delta(delta):
    params = dict(function="TIME_SERIES_DAILY",
                  symbol=STOCK,
                  outputsize="compact",
                  apikey=STOCK_API_KEY)
    response = requests.get(url=STOCK_URL, params=params)
    response.raise_for_status()
    yesterday = datetime.strptime(response.json()['Meta Data']['3. Last Refreshed'], "%Y-%m-%d")
    before_yesterday = (yesterday - timedelta(days=1)).strftime("%Y-%m-%d")
    yesterday = yesterday.strftime("%Y-%m-%d")
    close_before_yesterday = float(response.json()['Time Series (Daily)'][before_yesterday]["4. close"])
    close_yesterday = float(response.json()['Time Series (Daily)'][yesterday]["4. close"])
    return True if abs((close_yesterday-close_before_yesterday)/close_before_yesterday) > PRICE_DELTA else False

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_articles(topic):
    params = dict(q=topic,
                  searchIn="title",
                  sortBy="publishedAt",
                  pageSize=3,
                  apiKey=NEWS_API_KEY)
    response = requests.get(url=NEWS_URL, params=params)
    response.raise_for_status()
    for article in response.json()['articles']:
        print(article['title'])
    
def main():
    if stock_price_delta(PRICE_DELTA):
        get_news_articles(COMPANY_NAME)
        

if __name__ == "__main__":
    main()