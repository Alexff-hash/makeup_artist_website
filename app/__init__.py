"""The app module, containing the app factory function."""
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

    from app.main_pages import bp as bp_main_pages
    flask_app.register_blueprint(bp_main_pages)

    from app.blog import bp as bp_blog
    flask_app.register_blueprint(bp_blog)

    return flask_app