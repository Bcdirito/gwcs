# Rename this file to be "filters.py"

from PIL import Image, ImageFilter
import math
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename mode="r" )


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    # img = Image.open("luigyeet.png")
    image.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(destination, img):
    destination = "new_luigyeet.png"
    Image.save(destination, img)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    pixels = img.getdata()
    new_pixels = []

    dark_blue = (0, 51, 76)
    red = (217, 26, 33)
    light_blue = (112, 150, 158)
    yellow = (252, 227, 166)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(dark_blue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(light_blue)
        else:
            new_pixels.append(yellow)

    new_image = Image.new("RGB", img.size)
    new_image.putdata(new_pixels)
    return new_image

def grayscale(img):
    pixels = img.getdata()
    new_pixels = []

    for p in pixels:
        gray_p = get_average(p)
        new_pixels.append(gray_p)

    new_image = Image.new("RGB", img.size)
    new_image.putdata(new_pixels)

    return new_image

def get_average(pixels):
    avg = (pixels[0] + pixels[1] + pixels[2]) // 3
    return (avg, avg, avg)

def emphasize(img, color_tup, threshold):
    pixels = img.getdata()
    new_pixels = []

    red = color_tup[0]
    green = color_tup[1]
    blue = color_tup[2]

    for p in pixels:
        pix_red = p[0]
        pix_green = p[1]
        pix_blue = p[2]

        color_dist = math.sqrt((rtarget-r)**2 + (gtarget-g)**2 + (btarget-b)**2)

        if color_dist > threshold:
            new_p = avg_pixels(p)
            new_pixels.append(new_p)
        else:
            new_pixels.append(p)

    new_image = Image.new("RGB", img.size)
    new_image.putdata(new_pizels)

    return new_image

def invert(img):
    pixels = img.getdata()
    new_pixels = []

    for p in pixels:
        new_red = 255-p[0]
        new_green = 255-p[1]
        new_blue = 255-p[2]
        new_pixels.append((new_red, new_green, new_blue))

    new_image = Image.new("RGB", img.size)
    new_image.putdata(new_pizels)

    return new_image
