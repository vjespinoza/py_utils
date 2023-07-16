import os
from pathlib import Path

from PIL import Image
from rembg import remove


def remove_background() -> None:
    input_dir = 'resources/img'
    output_dir = 'out/img'
    extensions = ('jpg', 'png')

    for file in os.listdir(input_dir):
        if file.endswith(extensions):
            input_path = Path(f'{input_dir}/{file}')
            output_path = Path(f'{output_dir}/{file}')
            input_img = Image.open(input_path, mode='r')
            output_img = remove(input_img)
            output_img.save(fp=output_path, format='png')
