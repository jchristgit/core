from pydoc import locate

from django.conf import settings
from django.utils.functional import SimpleLazyObject

backend = SimpleLazyObject(lambda: locate(settings.CONFIG["BACKEND"])())


def load():
    backend.load(defaults=settings.DEFAULT_CONFIG)


def get(key):
    return backend.get(key)


def set(key, value):
    backend.set(key, value)


def get_all():
    return backend.get_all()


def get_all_non_sensitive():
    sensitive = backend.get("sensitive_fields")
    config = backend.get_all()
    for field in sensitive:
        del config[field]
    return config


def is_sensitive(key):
    return key in backend.get("sensitive_fields")
