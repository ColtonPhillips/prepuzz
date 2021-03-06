#usr/bin/env python3

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

def atoi(text):
  return int(text) if text.isdigit() else text

def natural_keys(text):
  return [ atoi(c) for c in re.split('(\d+)', text) ]

def file_to_lines(file_path):
  with open(file_path) as f:
    return f.read().splitlines()

def sorted_files_in_folder(extension, folder):
  files = []
  folder_dir_list = os.listdir(folder)
  folder_dir_list.sort(key=natural_keys)
  for f in folder_dir_list:
    if f.endswith(extension):
      files.append(os.path.join(folder, f))
  return files

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

def pixels_whc(image_path):
  im = Image.open(image_path).convert('RGBA')
  pix = im.load()
  w = im.size[0]
  h = im.size[1]
  out_l_l = [[0 for x in range(w)] for x in range(h)] 
  col_set = []
  for j in range(h):
    for i in range(w):
      r, g, b, a, hcolor = rgbah(pix,i,j) 
      if a != 0:
        addUnique(col_set, hcolor)
  col_set.sort()
  return pix, w, h, col_set

def rgbah(pix, i, j):
  r, g, b, a = pix[i,j]
  curPixel = '#%02x%02x%02x' % (r, g, b)
  return r, g, b, a, curPixel

def print_hcolor_list(hcolor_list):
  line = ""
  for item in hcolor_list:
    line += item + " "
  print (line)

def print_sprite_object(col_set,pix,w,h):
  for j in range (h):
    line = ""
    for i in range (w):
      r, g, b, a, hcolor = rgbah(pix,i,j)
      if (a == 0):
        line += "."
      else:
        line += str(col_set.index(hcolor))
    print(line)

def write_list_to_file(li,fi):
  out_string = '\n'.join(li)
  with open(fi, 'w') as out_file:
      out_file.write(out_string)

def multipleReplace(text, wordDict):
  for key in wordDict:
    text = text.replace(key, wordDict[key])
  return text

def parse_legend_lines(lines):
  out = []
  macro_dict = {}
  for line in lines:
    if line[0] == "=":
      line_list = line.strip().split("=")
      k,v = line_list[1] , line_list[2]
      macro_dict[k] = v
      continue
    line = multipleReplace(line,macro_dict)
    out.append(line)
  return out

def get_legend_dict():
  legend_dict = {}
  legend_lines = file_to_lines(legend_file)
  for line in legend_lines:
    if line[0] == "=":
      continue
    line_list = line.strip().split(" ")
    color = line_list[-1].lstrip("(").rstrip(")")
    legend_dict[color.lower()] = line_list[0]
  return legend_dict

def write_sorted_legend():
  legend_lines = file_to_lines(legend_file)
  legend_lines = parse_legend_lines(legend_lines)
  legend_lines.sort(key = lambda x: x.strip().split(" ")[-1])
  write_list_to_file(legend_lines,out_dir+"sorted_legend.txt")

def hex_to_rgba(value):
  value = value.lstrip('#')
  lv = len(value)
  t = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
  t.append(255)
  return tuple(t)
