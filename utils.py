# utils.py - helper stuff that both hide and read need

from PIL import Image

# this is how we know the message ended
# kinda like how you put "bye" at the end of a text
STOP_SIGNAL = "##END##"


def text_to_binary(text):
    # turns text into binary using utf-8
    # we use utf-8 so hindi, french etc also works not just english
    binary = ""
    for byte in text.encode('utf-8'):
        binary += format(byte, '08b')  # each byte = 8 bits always
    return binary


def binary_to_text(bits):
    # opposite of above, binary back to text
    result = bytearray()
    for i in range(0, len(bits) - 7, 8):
        chunk = bits[i:i+8]
        result.append(int(chunk, 2))
    # errors='replace' so it doesnt crash on weird bytes
    return result.decode('utf-8', errors='replace')


def load_image(path):
    # open image and force RGB mode because grayscale
    # and palette PNGs give weird pixel values and break everything
    img = Image.open(path)
    img = img.convert("RGB")
    return img
