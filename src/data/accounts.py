from src.utils.config import get_env


TEST_ACCOUNTS = {
    "default": {
        "username": get_env("USERNAME_1", ""),
        "password": get_env("PASSWORD_1", ""),
    },
    "alt": {
        "username": get_env("USERNAME_2", ""),
        "password": get_env("PASSWORD_2", ""),
    },
    "third": {
        "username": get_env("USERNAME_3", ""),
        "password": get_env("PASSWORD_3", ""),
    },
}
