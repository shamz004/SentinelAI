from PIL import Image
import numpy as np


def detect_currency(image_path):
    img = Image.open(image_path).convert("L")
    img = img.resize((100, 100))

    arr = np.array(img)
    brightness = np.mean(arr)

    if brightness > 130:
        return "LIKELY GENUINE NOTE"
    return "POSSIBLY FAKE NOTE"
