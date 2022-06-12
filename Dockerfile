# syntax=docker/dockerfile:1.3

FROM python:3.10-slim-bullseye as build
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc 

WORKDIR /opt/sample_app
RUN python -m venv /opt/sample_app/venv
ENV PATH="/opt/sample_app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim-bullseye@sha256:557745c5e06c874ba811efe2e002aff21b6cc405b828952fcfa16dea52d56dbb
RUN apt update && apt install --no-install-recommends -y vim nginx \
    && mkdir -p /opt/sample_app/app

WORKDIR /opt/sample_app

COPY --chown=www-data:www-data nginx.default /etc/nginx/sites-available/default
COPY --chown=www-data:www-data --from=build /opt/sample_app/venv ./venv
COPY --chown=www-data:www-data app /opt/sample_app/app/
COPY --chown=www-data:www-data start_server.sh .

# USER www-data:www-data

RUN ln -sf /dev/stdout /var/log/nginx/access.log 
ENV PATH="/opt/sample_app/venv/bin:$PATH"
# ENV PYTHONUNBUFFERED 1

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/sample_app/start_server.sh"]