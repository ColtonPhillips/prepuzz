#!/usr/bin/env python3

import os

def file_to_lines(file_path):
  with open(file_path) as f:
    return f.read().splitlines()

def files_in_folder(extension, folder):
  files = []
  for f in os.listdir(folder):
    if f.endswith(extension):
      files.append(os.path.join(folder, f))
  return files
