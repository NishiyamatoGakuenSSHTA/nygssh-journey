import numpy as np
import cv2


movements = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

class CharaBase():
    def __init__(self, name, pos, skills, level, img_path):
        self.scale = 32
        self.name = name
        self.pos = pos
        self.acts = skills
        img = cv2.imread(img_path)
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.lavel = level
        self.hp = level * 5
        self.attck = level * 3
        self.block = level
        self.mental = level * 4
        self.intelgence = level * 2

    def move(self, key):
        self.pos['x'] += movements[key][0] * self.scale
        self.pos['y'] += movements[key][1] * self.scale


class CharaManeger():
    def __init__(self):
        pass
