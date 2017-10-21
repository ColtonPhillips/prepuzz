#!/bin/sh
cd compiler
./legendtopalette
./pzr
cd ..
cat out/sorted_legend.txt
osascript applescripts/pasteintoeditor.applescript
