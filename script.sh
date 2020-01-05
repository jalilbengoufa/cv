#!/bin/bash
inotifywait -e close_write,moved_to,create -m . |
while read -r directory events filename; do
  if [ "$filename" = "index-page-1-fr.html" ]; then
    python toPDF.py
  fi
  if [ "$filename" = "index-page-2-fr.html" ]; then
    python toPDF.py
  fi
done