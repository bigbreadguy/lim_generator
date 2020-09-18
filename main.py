import os
import glob
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from generator import LimGenerator

cwd = os.getcwd()
png_list = list(glob.glob(os.path.join(cwd, "layers","*.png")))
sortKeyFunc = lambda x : int(os.path.splitext(os.path.basename(x))[0].split("_")[0])
png_list.sort(key=sortKeyFunc)

img_list = []
for png in png_list:
  img = Image.open(png)
  img_list.append(img)

gen = LimGenerator(img_list)
gen.display()