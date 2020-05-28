#!/bin/bash
inotifywait -e close_write,moved_to,create -m html |
while read -r directory events filename; do
  if [ "${filename##*.}" == "html" ]; then
    python toPDF.py
  fi
done