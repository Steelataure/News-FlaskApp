import requests

def get_news_from_api(query, category, page=1):
    api_key = '3b557069d7d2728b8f2fa00983c28278'
    url = f'https://gnews.io/api/v4/top-headlines?lang=fr&token={api_key}&q={query}&topic={category}&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        return articles
    else:
        return []
