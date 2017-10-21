#!/usr/bin/env python3

import re
import os
from PIL import Image
import sys

voxel_dir = "../voxels/"
src_dir = "../src/"
image_dir = "../images/"
out_dir = "../out/"
voxel_dir = "../voxels/"
text_dir = "../texts/"
rules_dir = "../rules/"
levels_dir = "../levels/"
objects_dir = "../objects/"
game_file = "dungeon.predude"
legend_file = "../texts/legend.txt"

def file_to_lines(file_path):
  with open(file_path) as f:
    return f.read().splitlines()

def files_in_folder(extension, folder):
  files = []
  for f in os.listdir(folder):
    if f.endswith(extension):
      files.append(os.path.join(folder, f))
  return files

def addUnique(l,item):
  if item not in l:
    l.append(item)
  return l

def atoi(text):
  return int(text) if text.isdigit() else text

def natural_keys(text):
  return [ atoi(c) for c in re.split('(\d+)', text) ]

def pixels_w_h(image_path):
  im = Image.open(image_path).convert('RGBA')
  return im.load(), im.size[0], im.size[1]

def rgbah(pix, i, j):
  r, g, b, a = pix[i,j]
  curPixel = '#%02x%02x%02x' % (r, g, b)
  return r, g, b, a, curPixel
