import os
import glob
import random
import argparse
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from generator import *

cwd = os.getcwd()
png_list = list(glob.glob(os.path.join(cwd, "layers","*.png")))
sortKeyFunc = lambda x : int(os.path.splitext(os.path.basename(x))[0].split("_")[0])
png_list.sort(key=sortKeyFunc)

img_list = []
for png in png_list:
  img = Image.open(png)
  img_list.append(img)

class opts():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="lim_generator",
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.parser.add_argument("-t", "--type", default="display",
                                 choices=["display", "collage"], type=str, dest="type")
        self.parser.add_argument("-c", "--change", default=False,
                                 choices=[True, False], type=bool, dest="change")
    
    def parse(self, args : str = None):
        if args == None:
            opt = self.parser.parse_args()
        else:
            opt = self.parser.parse_args(args)

        return opt

args = opts().parse()
gen = LimGenerator(img_list)
if args.type == "display":
    gen.display(args.change)
else:
    gen.collage()