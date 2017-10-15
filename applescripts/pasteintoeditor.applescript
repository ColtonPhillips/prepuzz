
tell application "Google Chrome"
  activate
  open location "http://dungeonscript.farbs.org/editor.html"
  delay 1.3
end tell

tell application "System Events"
  keystroke tab
  delay 0.1
  keystroke "a" using command down
  delay 0.1
  keystroke "v" using command down
end tell
