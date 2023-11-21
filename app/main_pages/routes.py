from flask import render_template

from app.main_pages import bp

@bp.route('/')
def index():
    return render_template('main_pages/index.html',
                           page_title='Визажист-стилист Елена Долгорукая')
@bp.route('/about')
def about():
    return render_template('main_pages/about.html', page_title='Обо мне')

@bp.route('/portfolio')
def portfolio():
    pass

@bp.route('/price_page')
def price_page():
    pass

@bp.route('/contact')
def contact_page():
    pass
