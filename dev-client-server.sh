#!/bin/bash

function cleanup {
  kill $(jobs -p)
}

trap cleanup SIGINT

function run_client {
  pushd client
  npm run dev &
  popd
}

export VITE_DEV_PORT=9997

. venv/bin/activate
run_client
python3 app.py
