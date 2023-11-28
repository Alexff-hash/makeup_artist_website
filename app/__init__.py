"""The app module, containing the app factory function."""
import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask

from app.misc.log import log


def create_app(*config_cls) -> Flask:
    config_cls = [
        config() if isinstance(config, type) else config for config in config_cls
    ]

    log(
        message="Flask application initialized with {}".format(
            ",".join([config.__class__.__name__ for config in config_cls])
        ),
        keyword='INFO',
    )

    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    from app.errors import bp as bp_errors
    flask_app.register_blueprint(bp_errors)

    from app.main_pages import bp as bp_main_pages
    flask_app.register_blueprint(bp_main_pages)

    from app.blog import bp as bp_blog
    flask_app.register_blueprint(bp_blog)

    if not flask_app.debug and not flask_app.testing:
        if flask_app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            flask_app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/makeup_art_web.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            flask_app.logger.addHandler(file_handler)

        flask_app.logger.setLevel(logging.INFO)
        flask_app.logger.info('Website startup')

    return flask_app