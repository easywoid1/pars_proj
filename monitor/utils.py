def format_article(article):
    return {
        'title': article.title,
        'link': article.link,
        'published': article.published,
        'summary': article.summary,
    }
