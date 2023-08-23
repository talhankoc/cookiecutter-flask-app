# gunicorn expects the wsgi application to be named app and to be in a file named wsgi.py
from app import app

__all__ = ['app']
