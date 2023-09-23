#!/bin/bash
python3 -m pip install requests

python3 epg_filter.py > ./epg_filtered.xml

echo epg_filtered generated.
