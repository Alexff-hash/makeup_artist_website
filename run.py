"""Create an application instance."""
from app import create_app
from config.app_config import LocalLevelConfig
from constants.local_run import RUN_SETTING

app = create_app(LocalLevelConfig)

if __name__ == '__main__':
    app.run(**RUN_SETTING)