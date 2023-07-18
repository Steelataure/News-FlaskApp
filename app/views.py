from flask import render_template, request
from .api import get_news_from_api, ARTICLES_PAR_PAGE  # Importez ARTICLES_PAR_PAGE

def index():
    query = request.args.get('q', default='', type=str)
    category = request.args.get('category', default='', type=str)
    page = int(request.args.get('page', default=1, type=int))
    articles = get_news_from_api(query, category, page, ARTICLES_PAR_PAGE)
    return render_template('index.html', articles=articles, query=query, category=category, page=page, ARTICLES_PAR_PAGE=ARTICLES_PAR_PAGE)
