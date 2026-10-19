# read.py - extracts a hidden message from an image

from utils import binary_to_text, load_image, STOP_SIGNAL


def read_message(image_path):
    """reads and returns the hidden message from the image,
    or None if theres nothing hidden"""

    img = load_image(image_path)

    # getdata() gives all pixels as a flat list of (R,G,B) tuples
    # way faster than doing nested for loops with pixels[x,y]
    all_pixels = img.getdata()

    # grab last bit from every color value
    bits = []
    for r, g, b in all_pixels:
        bits.append(str(r & 1))
        bits.append(str(g & 1))
        bits.append(str(b & 1))

    # convert all bits to text at once and look for stop signal
    text = binary_to_text("".join(bits))

    if STOP_SIGNAL in text:
        # found it, grab everything before the stop signal
        secret = text.split(STOP_SIGNAL)[0]
        print(f"Message found! ({len(secret)} characters)")
        return secret

    # no stop signal means no message was hidden
    # (or it was hidden by some other tool)
    print("No hidden message found in this image.")
    return None
