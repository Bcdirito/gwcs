import filters

def main():
    file = input("What file are you trying to edit: ")

    img = filters.load_img(file)

    new_img = filters.obamicon(img)

    filters.save_img(img, "recolored.jpg")

if __name__ == "__main__":
    main()
