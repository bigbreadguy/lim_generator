import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class LimGenerator():
    def __init__(self, layers):
        super(LimGenerator, self).__init__()
        self.layers = layers
        self.colors = [(163, 156, 255), (236, 177, 161), (22, 22, 22), (190, 0, 32), (0, 0, 0), (255, 255, 255), (36, 8, 0), (2, 0, 29)]

    def random_color(self, index, layer, change : bool = False):
        im = layer.convert("RGBA")
        color = self.colors[index]
        if change:
            color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        data = np.array(im)
        red_channel, green_channel, blue_channel, alpha_channel = data.T
        target_area = (red_channel == 255) & (blue_channel == 255) & (green_channel == 255)
        data[..., :-1][target_area.T] = color
        return Image.fromarray(data)

    def display(self, color_change : bool = False):
        canvas = []
        for index, layer in enumerate(self.layers):
            canvas.append(self.random_color(index, layer, color_change))
        for layer in canvas:
            _ = plt.imshow(layer)
        
        plt.axis("off")
        plt.show()
    
    def collage(self):
        fig, axs = plt.subplots(nrows=3, ncols=3)
        for ax in axs.ravel():
            canvas = []
            for index, layer in enumerate(self.layers):
                canvas.append(self.random_color(index, layer, True))
            for layer in canvas:
                ax.imshow(layer)
            ax.axis("off")
        
        plt.title("Hayoung Lim", 
          position=(0.5, 1.0+0.05), 
          fontsize=15)
        plt.axis("off")
        plt.show()