import requests

ARTICLES_PAR_PAGE = 10  # Mettez ici le nombre d'articles à afficher par page

def get_news_from_api(query, category, page=1, articles_per_page=10):
    api_key = '3b557069d7d2728b8f2fa00983c28278'
    url = f'https://gnews.io/api/v4/top-headlines?lang=fr&token={api_key}&q={query}&topic={category}&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        start_idx = (page - 1) * articles_per_page
        end_idx = start_idx + articles_per_page
        return articles[start_idx:end_idx]
    else:
        return []
