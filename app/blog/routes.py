"""Blog routes."""
from flask import render_template

from app.blog import bp


@bp.route('/blog-one')
def blog_one():
    return render_template('blog/blog_one.html')


@bp.route('/blog-two')
def blog_two():
    return render_template('blog/blog_two.html')


@bp.route('/everyday-makeup')
def blog_everyday():
    return render_template('blog/blog_everyday.html')

@bp.route('/evening-makeup')
def blog_evening():
    pass

@bp.route('/lifting-makeup')
def blog_lifting():
    pass

@bp.route('/bridal-makeup')
def blog_bridal():
    pass

@bp.route('/photoshoot')
def blog_photoshoot():
    pass

@bp.route('/publications-journals')
def blog_magazines():
    pass
