from PIL import Image, ImageDraw, ImageFont, ImageShow


def decode_image(path_to_png):
    """
    Decode an image file by taking the LSD from the binary value of RED from the rgb color value of each pixel
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    x_size, y_size = encoded_image.size

    for x in range(0, x_size):
        for y in range(0, y_size):
            binValStr = str(bin(red_channel.getpixel((x, y))))
            leastSigDig = binValStr[len(binValStr)-1]
            color = int(leastSigDig) * 255
            decoded_image.putpixel((x, y), (color, color, color))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png, text_to_encode, autoBreakLines):
    """
    Encode an image's Red channel's binary LSD with given text
    """

    image = Image.open(path_to_png)
    x_size, y_size = image.size

    # Get a black and white image with text
    image_with_text = write_text(
        text_to_encode, image.size, 30, autoBreakLines)
    text_pixels = image_with_text.getdata()

    # Store the text image's data into the Red value of the encode image
    for x in range(0, x_size):
        for y in range(0, y_size):
            # get the pixel from the text image

            # if pixel is white set val to 1, else 0
            text_pixel_is_white = 1
            if text_pixels.getpixel((x, y))[0] > 0:
                text_pixel_is_white = 0

            encoded_image_pixel = image.getpixel((x, y))
            red = encoded_image_pixel[0]
            green = encoded_image_pixel[1]
            blue = encoded_image_pixel[2]

            if(red % 2 == text_pixel_is_white):
                if(red < 255):
                    red += 1
                else:
                    red -= 1

            image.putpixel((x, y), (red, green, blue))

    image.save("encoded_image.png")


def write_text(text_to_write, image_size, font_size, autoBreakLines):
    """
    Create a black image of specified size with the desired text written on it
    """
    image = Image.new("RGB", image_size)
    wrappedText = text_to_write

    if autoBreakLines:
        # Add line breaks to prevent string going off screen
        textWidth = 0
        for i in range(0, len(text_to_write)):
            if(textWidth > (image_size[0] + (image_size[0] * 5/9))):
                textWidth = 0
                wrappedText = wrappedText[:i] + '\n' + wrappedText[i:]

            textWidth += font_size

    drawing = ImageDraw.Draw(image)
    myFont = ImageFont.truetype('./RobotoMono-Bold.ttf', font_size)
    drawing.text((0, 0), wrappedText, font=myFont, fill=(255, 255, 255))

    # Show the decoded version of the image to the user to ensure quality
    image.show()

    return image


# Run this to decode an encoded image
# decode_image('./encoded_sample.png')


# Run this to encode an image with text
# encode_image('image-path', 'text-to-encode', 'bool: auto add line breaks')
encode_image('./image_to_encode.jpg',
             "Here is some text to encode in an image", False)
