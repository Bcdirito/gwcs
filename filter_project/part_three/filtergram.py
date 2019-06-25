import filters

def main():
    file = input("What file are you trying to edit: ")

    img = filters.load_img(file)

    new_img = filters.obamicon(img)
    gray_img = filters.grayscale(new_img)

    filters.save_img(gray_img, "recolored.jpg")

if __name__ == "__main__":
    main()
