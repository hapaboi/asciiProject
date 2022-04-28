from PIL import Image

# ASCII char used
ASCII = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

# Specific ASCII Aspect Ratio to fix stretching
ASCII_ASPECT = 1.65


# Resizes image with same aspect ratio
def resize(image, new_width=100):
    tempwidth, tempheight = image.size
    ratio = tempheight / tempwidth / ASCII_ASPECT
    new_height = int(new_width * ratio)
    resized_im = image.resize((new_width, new_height))
    return resized_im


# Make image grayscale
def make_grayscale(image):
    grayscale = image.convert("L")
    return grayscale


# Convert image to ASCII
def make_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel//3.9] for pixel in pixels])
    return characters


def main(new_width=100):
    # Open and Resize image
    im = Image.open("hollow.jpg")

    image_data = make_ascii(make_grayscale(resize(im)))

    pixel_count = len(image_data)
    ascii_image = "\n".join(image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    f = open('asciiversion.txt', 'w')
    f.write(ascii_image)
    f.close()


if __name__ == '__main__':
    main()



