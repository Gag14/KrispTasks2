import feedparser

google_news_url="https://news.google.com/news/rss"

def get_headlines(url):

    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    
    return titles


print(get_headlines(google_news_url))