
from PIL import Image

matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

# print(matrix.size) -> (1015, 559)
# print(mask.size) -> (505, 251)

matrix_w, matrix_h = matrix.size

# Rezise mask to cover word matrix
mask = mask.resize((matrix_w, matrix_h))

# create a new image by interpolating between the two images, using a constant alpha value
revealed = Image.blend(matrix, mask, 0.5)
revealed.show()