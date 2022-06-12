#!/usr/bin/env bash
# start-server.sh
(cd app; gunicorn wsgi --user www-data --bind 127.0.0.1:8010 --workers 3 --worker-class=gevent) &
nginx -g "daemon off;"
