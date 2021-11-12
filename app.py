"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image


# def decode_image(path_to_png):
#     """
#     TODO: Add docstring and complete implementation.
#     """
#     encoded_image = Image.open(path_to_png)

#     # convert the image to use rgb format
#     image = encoded_image.convert("RGB")

#     # get list of raw pixels
#     raw_pixels = list(image.getdata())
#     width, height = image.size

#     # process pixel list into a matrix
#     encoded_pixels = [
#         raw_pixels[i * width: (i + 1) * width] for i in range(height)]

#     # Create a new PIL image with the same size as the encoded image:
#     decoded_image = Image.new("RGB", encoded_image.size)
#     pixels = decoded_image.load()
#     x_size, y_size = encoded_image.size

#     # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
#     # Start coding here!

#     for row in range(0, len(encoded_pixels)):
#         for col in range(0, len(encoded_pixels[0])):
#             print(pixels)

#             # DO NOT MODIFY. Save the decoded image to disk:
#     decoded_image.save("decoded_image.png")


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    # Start coding here!
    print(red_channel)
    print(red_channel.getpixel((0, 0)))

    for x in range(0, x_size):
        for y in range(0, y_size):
            binValStr = str(bin(red_channel.getpixel((x, y))))
            leastSigDig = binValStr[len(binValStr)-1]
            color = int(leastSigDig) * 255
            decoded_image.putpixel((x, y), (color, color, color))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


decode_image('./encoded_sample.png')
