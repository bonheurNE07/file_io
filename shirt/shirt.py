import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    arguments = sys.argv
    arguments_status = check_arguments(arguments)

    if arguments_status:
        # Open the shirt image
        with Image.open("shirt.png") as shirt_img:
            # Open the input image
            with Image.open(arguments[1]) as infile:
                # Get the size of the shirt image
                shirt_size = shirt_img.size
                # Resize the input image to match the shirt image size
                inimg_resized = ImageOps.fit(infile, shirt_size)
                # Paste the shirt image onto the resized input image
                inimg_resized.paste(shirt_img, shirt_img)
                # Save the result as the output image
                inimg_resized.save(arguments[2])

def get_extensions(path) -> str:
    _, extension = splitext(path)
    return extension

def check_arguments(arguments):
    valid_extensions = [".jpg", ".jpeg", ".png"]

    # Check for the correct number of arguments
    if len(arguments) != 3:
        if len(arguments) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    # Check that both input and output files have valid extensions
    extension1 = get_extensions(arguments[1])
    extension2 = get_extensions(arguments[2])
    if not extension1 in valid_extensions or not extension2 in valid_extensions:
        sys.exit("Invalid input")
    if extension1 != extension2:
        sys.exit("Input and output have different extensions")

    return True

if __name__ == "__main__":
    main()
