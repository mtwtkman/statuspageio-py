#!/bin/sh

name="statuspageio.py"
cmd=$1
shift

case $cmd in
  build) docker build -t $name .;;
  run) docker run -ti --rm --env-file .env --mount type=bind,source=`pwd`,target=/source $name $@;;
esac
