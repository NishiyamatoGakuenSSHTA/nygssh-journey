import numpy as np


GameSize = (250, 720)


class SceneManeger():
    def __init__(self):
        self.scenekind = 0 # 0: idle, 1: battle
        self.backgrond = {
                            0: np.zeros(GameSize, dtype=np.uint8),
                            1: np.full(GameSize, 50, dtype=np.uint8)
                         }


