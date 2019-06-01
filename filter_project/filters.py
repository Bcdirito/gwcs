# Rename this file to be "filters.py"

from PIL import Image, ImageFilter

# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img():
    return Image.open("luigyeet.png", mode="r" )


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img():
    img = Image.open("luigyeet.png")
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img):
    destination = "new_luigyeet.png"
    Image.save(destination)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon():
    img = Image.open("luigyeet.png")
    filt_img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    return Image.new("RGB", (200, 200))

load_img()
obamicon()
show_img()
save_img(obamicon)
