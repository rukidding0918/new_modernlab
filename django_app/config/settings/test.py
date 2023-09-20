from .base import *

DEBUG = env.bool("DEBUG", default=False)

DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),  # set in docker-compose.yml
        "PORT": env.int("DB_PORT"),  # default postgres port
    }
}
