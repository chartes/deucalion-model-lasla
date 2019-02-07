#!/bin/sh
# Timeout of 60sec right now
exec gunicorn -b :5000 --access-logfile - --error-logfile - flaskapp:app --timeout 60
