import numpy as np
from PIL import Image

row_data = np.arange(256)  # 255列
hue_data = np.tile(row_data, (256, 1))  # 255行
sat_data = np.transpose(hue_data)  # 配列の順番入れ替え
val_data = np.full_like(hue_data, 255)  # すべての要素の値が同一の配列
mat_data = np.stack([hue_data, sat_data, val_data], 2)  # 新たな軸に沿って結合する

im = Image.fromarray(np.uint8(mat_data), "HSV")
im_rgb = im.convert("RGB")
im_rgb.show()
