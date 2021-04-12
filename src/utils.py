from PIL import Image, ImageDraw, ImageFont
import numpy as np

def cv2_putText(img, text, org, fontFace, fontScale, color):
    x, y = org
    imgPIL = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPIL)
    fontPIL = ImageFont.truetype(font=fontFace, size=fontScale)
    # w, h = draw.textsize(text, font=fontPIL)
    draw.text(xy=(x,y), text=text, fill=color, font=fontPIL)
    return np.array(imgPIL, dtype=np.uint8)
