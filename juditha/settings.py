import os
from typing import Any

from banal import as_bool


def get_env(env: str, default: Any | None = None) -> Any | None:
    return os.environ.get(env, default)


DEBUG = as_bool(get_env("DEBUG", 0))
REDIS_URL = get_env("REDIS_URL", "redis://localhost:6379")
REDIS_PREFIX = get_env("REDIS_PREFIX", "juditha")

JUDITHA_CONFIG = get_env("JUDITHA_CONFIG")

# Api documentation render
TITLE = os.environ.get("TITLE", "Canonicaller")
CONTACT = {
    "name": os.environ.get("CONTACT_AUTHOR", "Simon Wörpel"),
    "url": os.environ.get(
        "CONTACT_URL", "https://github.com/investigativedata/juditha/"
    ),
    "email": os.environ.get("CONTACT_EMAIL", "simon@investigativedata.org"),
}
DESCRIPTION = """
Super fast canonical name lookup. Just do head requests:

    curl -I "http://localhost:8000/Berlin"
    HTTP/1.1 200 OK

    curl -I "http://localhost:8000/Bayern"
    HTTP/1.1 404 Not Found

To get the actual canonized value, do a GET request:

    curl "http://localhost:8000/berlin"
    "Berlin"
"""