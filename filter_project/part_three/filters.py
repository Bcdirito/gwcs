# Rename this file to be "filters.py"

from PIL import Image, ImageFilter

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
