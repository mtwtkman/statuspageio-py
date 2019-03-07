#!/bin/sh -eu

cmd=$1
shift

case $cmd in
  update) pip install -e .[dev];;
  mypy) mypy statuspageio;;
  lint) pycodestyle statuspageio;;
  *) $cmd $@;;
esac
