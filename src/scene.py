import numpy as np
import os


GameSize = (250, 720)


class MapScene():
    def __init__(self, SceneCreateInfoFile) -> None:
        pass

class SceneManeger():
    def __init__(self, SceneDataDir="./data"):
        datafiles = os.listdir(SceneDataDir)
        self.jsonfiles = [f for f in datafiles if ".json" in f]

        self.scenekind = 0 # 0: map, 1: battle
        self.backgrond = {
                            0: np.zeros(GameSize, dtype=np.uint8),
                            1: np.full(GameSize, 50, dtype=np.uint8)
                         }

    def initialize():
        pass


