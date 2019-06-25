import filters

def main():
    file = input("What file are you trying to edit: ")

    img = filters.load_img(file)

    new_img = filters.obamicon(img)
    gray_img = filters.grayscale(new_img)

    blue = (30, 85, 115)
    emph_img = filters.emphasize(img, blue, 50)

    blue_img = filters.add_color(img, blue)

    invert_img = filters.invert(blue_img)

    filters.save_img(gray_img, "recolored.jpg")
    filters.save_img(emph_img, "emph.jpg")
    filters.save_img(blue_img, "blue.jpg")
    filters.save_img(invert_img, "invert.jpg")

if __name__ == "__main__":
    main()
