from PIL import Image

def is_not_color(color):
    return color in [(0, 0, 0, 0), (0, 0, 0)]

def get_total_colors(img):
    """
    Returns the total number of colors in an image.
    :param image_path: The path to the image file.
    :return: The total number of colors.
    """
    color_counts = img.getcolors(maxcolors=999999)
    
    # Return the length of the list
    return len(color_counts)


def reduce_image_quality(img, c_level=5):
    """
    Converts an image to an image with only 5 levels of color.
    :param image_path: The path to the image file.
    :return: The converted image.
    """
    # Open the image file
    # img = Image.open(image_path)
    img = img.convert('RGB')
    
    color_palette = img.convert('P', palette=Image.ADAPTIVE, colors=c_level-1)
    color_reduced_img = img.quantize(colors=c_level-1, palette=color_palette)
    
    return color_reduced_img


def convert_color(image_path, old_color, new_color):
    """
    Converts a specific color in an image to another color.
    :param image_path: The path to the image file.
    :param old_color: The RGB values of the color to be converted.
    :param new_color: The RGB values of the new color.
    """
    # Open the image file
    img = Image.open(image_path)
    
    # Get the pixel values
    pixels = img.load()
    
    # Loop through each pixel in the image
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # Check if the pixel matches the old color
            if pixels[x, y] == old_color:
                # Set the new color for the specified pixel
                pixels[x, y] = new_color
    return img

    
image_path = 'test.png'
img = Image.open(image_path)

color_reduced_img = reduce_image_quality(img, c_level=2)

# Save the converted image
color_reduced_img.save('test-reduced.png')