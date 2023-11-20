from flask import render_template

from app.main_pages import bp

@bp.route('/')
def index():
    return render_template('main_pages/index.html', page_title='Dolgorukaya makeup')
@bp.route('/about')
def about():
    pass

@bp.route('/portfolio')
def portfolio():
    pass

@bp.route('/price_page')
def price_page():
    pass

@bp.route('/contact')
def contact_page():
    pass
