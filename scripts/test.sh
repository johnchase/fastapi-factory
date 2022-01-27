#!/usr/bin/env bash

set -e
set -x

pytest --cov=app --cov-report=term-missing app/tests "${@}" && black ./ --target-version py36 --check  && flake8
