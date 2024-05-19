#!/usr/bin/env bash

echo "Starting"

flask db upgrade

echo "Ok"

exec "$@"