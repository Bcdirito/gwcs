import filters

def main():
    file = input("What file are you trying to edit: ")

    img = filters.load_img(file)

    filters.save_img(img, "recolored.jpg")

if __name__ == "__main__":
    main()
