# hide.py - hides a secret message inside an image
# uses LSB (least significant bit) method

from utils import text_to_binary, load_image, STOP_SIGNAL


def hide_message(image_path, message, output_path):
    """hides the given message into the image at image_path
    and saves the result to output_path. returns True if it worked"""

    img = load_image(image_path)
    pixels = img.load()
    w, h = img.size

    # add stop signal at the end so we know where message stops
    # otherwise itd just keep reading random pixel garbage lol
    full_msg = message + STOP_SIGNAL
    binary = text_to_binary(full_msg)

    # check if image has enough space
    total_bits = w * h * 3   # each pixel has R G B = 3 values we can use
    if len(binary) > total_bits:
        print("ERROR: message too long for this image")
        print(f"  image can fit around {total_bits // 8} characters")
        print(f"  your message needs {len(binary)} bits")
        return False

    # now the fun part - hiding bits in pixels
    # basically we change the last bit of each color value
    # 142 and 143 look the same to human eyes so nobody notices
    # its like hiding veggies in a smoothie, sneaky but effective

    idx = 0       # which bit of the message we're on
    finished = False

    for y in range(h):
        if finished:
            break
        for x in range(w):
            px = list(pixels[x, y])

            for c in range(3):    # 0=red 1=green 2=blue
                if idx < len(binary):
                    # change last bit to our message bit
                    if binary[idx] == '0':
                        px[c] = px[c] & 0xFE     # last bit -> 0
                    else:
                        px[c] = px[c] | 0x01     # last bit -> 1
                    idx += 1

            pixels[x, y] = tuple(px)

            if idx >= len(binary):
                finished = True
                break

    img.save(output_path)
    print(f"Message hidden in '{output_path}' successfully!")
    print(f"  {len(message)} characters hidden using {len(binary)}/{total_bits} bits")
    # the image looks literally the same, thats the whole point
    return True
