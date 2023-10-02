import numpy as np
from PIL import Image


def image_path_to_array(image_path: str, input_format: str) -> np.ndarray:
    image = Image.open(image_path).convert(input_format.upper())
    return np.array(image)
