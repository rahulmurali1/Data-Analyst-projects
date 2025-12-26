import newspaper
import feedparser

def scrap_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        article = newspaper.Article(entry.link)
        article.download()
        article.parse()
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })
        return articles

feed_url = "https://news.un.org/feed/subscribe/en/news/region/global/feed/rss.xml"
articles = scrap_news_from_feed(feed_url)

for article in articles:
    print('Title: ', article['title'])
    print('Author: ', article['author'])
    print('Publish Date: ', article['publish_date'])
    print('Content: ', article['content'])
    print()

with open("news_output.txt", "w", encoding="utf-8") as file:
    for article in articles:
        file.write(f"TITLE: {article['title']}\n")
        file.write(f"AUTHOR: {', '.join(article['author'])}\n")
        file.write(f"DATE: {article['publish_date']}\n\n")
        file.write("CONTENT:\n")
        file.write(article['content'] + "\n")
        file.write("=" * 80 + "\n\n")
