import os

from dotenv import load_dotenv


load_dotenv()


def get_env(key, default=None):
    return os.getenv(key, default)


def get_locale(default="en-US"):
    return get_env("APP_LOCALE", default)
