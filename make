#!/bin/sh
cd compiler
./legendtopalette
./pzr
cd ..
osascript applescripts/pasteintoeditor.applescript
