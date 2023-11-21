from flask import render_template, request, redirect, url_for, jsonify

from app.main_pages import bp
from app.main_pages.forms import BookingForm

@bp.route('/')
def index():
    return render_template('main_pages/index.html',
                           page_title='Визажист-стилист Елена Долгорукая')
@bp.route('/about')
def about():
    return render_template('main_pages/about.html', page_title='Обо мне')

@bp.route('/portfolio')
def portfolio():
    return render_template('main_pages/portfolio.html', page_title='Портфолио')

@bp.route('/price_page')
def price_page():
    return render_template('main_pages/price_page.html', price_page='Цены на услуги')

@bp.route('/contact', methods=['GET', 'POST'])
def contact_page():
    form = BookingForm()
    if request.method == 'POST' and form.validate_on_submit():
        return 'Благодарим за заявку!!!'
    elif request.method == 'POST' and not form.validate_on_submit():
        return jsonify(form.errors), 400
    return render_template('main_pages/contact.html', form=form, page_title='Контакты')
