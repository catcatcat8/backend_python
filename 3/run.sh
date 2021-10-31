#!/bin/bash

gunicorn --workers=4 wsgi:app
