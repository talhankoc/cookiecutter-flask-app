echo "Starting server..."
(gunicorn --config "gunicorn.conf.py") &
nginx -c /code/nginx.conf