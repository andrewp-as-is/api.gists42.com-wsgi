#!/bin/sh

WORKERS=${WORKERS-3}
gunicorn wsgi:application -b 0.0.0.0:8080 --workers $WORKERS
