#!/bin/bash
python3 -m pip install requests
pip install lxml
pip install wget
pip install pandas

python3 epg_filter.py > ./epg_filtered.xml

echo epg_filtered generated.
