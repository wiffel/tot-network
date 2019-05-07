import os

from .local import Local
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Test(Local):
    # SQLite as database for local tests
    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///db.sqlite',
        ),

    }
    ACCESS_LOG_FILE = os.path.join(BASE_DIR, 'temp-access.log')
    LOGGING = Local.LOGGING
    LOGGING['handlers']['access_log']['filename'] = ACCESS_LOG_FILE
