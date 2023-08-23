# See documentation for further details
# https://docs.gunicorn.org/en/stable/settings.html#config

# A WSGI application path in pattern $(MODULE_NAME):$(VARIABLE_NAME).
wsgi_app = "wsgi:app"
# The socket to bind
bind = "0.0.0.0:8000"
# The number of worker processes for handling requests
workers = 4
# Redirect error info to system logs
errorlog = "-"
