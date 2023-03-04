import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_SEARCH_API_KEY = os.environ.get('YOUR_MASTER_KEY_VALUE')
    APP_SEARCH_API_KEY_BLOG = os.environ.get('YOUR_MASTER_KEY_VALUE')
    APP_SEARCH_BASE_ENDPOINT = os.environ.get('APP_SEARCH_BASE_ENDPOINT') or 'http://109.205.61.211'
    APP_SEARCH_USE_HTTPS = os.environ.get('APP_SEARCH_USE_HTTPS') or 'False'
    POSTS_PER_PAGE = 10
