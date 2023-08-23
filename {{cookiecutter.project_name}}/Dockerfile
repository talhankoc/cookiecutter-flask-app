FROM python:3.10-buster

# Install and setup nginx
RUN apt-get update \
    && apt-get install nginx -y --no-install-recommends
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
# set working directory
WORKDIR /code
# this is needed for python imports to work
ENV PYTHONPATH "/code:${PYTHONPATH}"

COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/sh", "start_server.sh"]