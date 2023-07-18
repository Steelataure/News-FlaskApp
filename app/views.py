from flask import render_template, request
from api import get_news_from_api

def index():
    query = request.args.get('q', default='', type=str)
    category = request.args.get('category', default='', type=str)
    articles = get_news_from_api(query, category)
    return render_template('index.html', articles=articles)
