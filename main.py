#!usr/bin/python3
# Code to add name in the certificate from the excel file.

# Importing the required libraries.
from PIL import Image as PILImage
from PIL import ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
import os
import cv2
import xlrd
import numpy as np
from tqdm import tqdm

# To store the coordinate of the rectangle in the image.
global left_x, left_y, right_x, right_y


# Function for getting the coordinate of the rectangle from the image.
def drawRectangle(event, x, y, flags, params):
    global left_x, left_y, right_x, right_y, drawRect, mini_image

    if event == cv2.EVENT_LBUTTONDOWN:  # Check left mouse button click.
        drawRect = True
        left_x, left_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # Check left mouse button movement.
        if drawRect == True:
            mini_image = cv2.imread(sample_image_file_name)
            cv2.rectangle(mini_image, (left_x, left_y), (x, y), (0, 0, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:  # Check left mouse button release.
        drawRect = False
        right_x, right_y = x, y

        # For selecting rectangle from top->bottom and bottom->top
        left_x, right_x = sorted([left_x, right_x])
        left_y, right_y = sorted([left_y, right_y])


root = Tk()
root.withdraw()  # To cancel poping out of the tkinter window.

# Variables used
# For scaling large image into smaller one for displaying.
large_to_small_ratio = 5


drawRect = False  # For drawing rectangle in image.

# Getting the file path of excel sheet, certificate image and font file.
excel_file_path = filedialog.askopenfilename(
    initialdir=os.getcwd(), title="Select excel file")
certificate_file_path = filedialog.askopenfilename(
    initialdir=os.getcwd(), title="Select certificate image")
font_file_path = filedialog.askopenfilename(
    initialdir=os.getcwd(), title="Select font file")

# Image file extension of the certificate image.
image_file_extension = certificate_file_path.split(".")[-1]

# For naming sample image created.
sample_image_file_name = "test.{}".format(image_file_extension)

# Getting the column details in the excel file.
name_column = int(input("Enter the column number of Name in the excel: "))-1
name_row_start = int(input("Enter the starting row of name in the excel: "))-1
name_row_end = int(input("Enter the ending row of name in the excel: "))

# To style the names in the excel file for printing in certificate.
print("\n\nChoose the style for name in the certificate")
print("\t[1] michael faraday")
print("\t[2] MICHAEL FARADAY")
print("\t[3] Michael Faraday")
print("\t[4] Michael faraday")
print("\t[5] Same as in excel file")
name_style = int(input("Enter your style (1-5): "))

# Getting color for names.
name_font_color = tuple(
    map(int, input("Enter the color in RGB with spaces: ").split()))

# Default font size.
name_font_size = 100

# Reading the excel file
wbr = xlrd.open_workbook(excel_file_path)
sheet = wbr.sheet_by_index(0)

name_list = []  # List for storing the names.

# Traversing through the excel file and adding names into the list.
for i in range(name_row_start, name_row_end):
    # Reading the cell value in the excel sheet.
    name = str(sheet.cell_value(i, name_column))
    if name_style == 1:
        name = name.lower()
    elif name_style == 2:
        name = name.upper()
    elif name_style == 3:
        name = name.title()
    elif name_style == 4:
        name = name.capitalize()
    name_list.append(name)  # Adding names to list.

# Getting the longest name in the list
max_length_name = max(name_list, key=len)

# Reading the certificate image.
image = cv2.imread(certificate_file_path)

# Getting the height width of the original image
height, width, channels = image.shape

# Create the smaller version of the larger image for speed.
mini_image = cv2.resize(
    image, (width//large_to_small_ratio, height//large_to_small_ratio))
cv2.imwrite("test.{}".format(image_file_extension), mini_image)

# Getting the coordinate of rectangle to fix the name.
cv2.namedWindow("NTC", cv2.WINDOW_NORMAL)
cv2.resizeWindow("NTC", 600, 600)
cv2.setMouseCallback("NTC", drawRectangle)
while True:
    cv2.imshow("NTC", mini_image)
    key = cv2.waitKey(1)    # Checking key pressed in the keyboard.
    if key == 13:   # Enter key is pressed.
        break
cv2.destroyWindow("NTC")

# Reading the mini image using pillow.
mini_image = PILImage.open(sample_image_file_name)

# To note down, which key is pressed.
key_press = 0
while(key_press != 13):  # Press the ENTER key to stop.

    # Adding the font again.
    name_font = (ImageFont.truetype(font_file_path,
                                    name_font_size//large_to_small_ratio))

    clone_img = mini_image.copy()   # Store the copy of the mini_image

    # For drawing text on the image.
    d = ImageDraw.Draw(clone_img)

    # Getting the width and height of the text in the image.
    text_w, text_h = d.textsize(max_length_name, font=name_font)

    # Putting text on selected x and y coordinate and on the center of the selected area.
    text_x = left_x + ((right_x - left_x) // 2) - (text_w // 2)
    text_y = right_y - text_h
    d.text((text_x, text_y),
           max_length_name, fill=name_font_color, font=name_font)

    # Showing image on the screen
    cv_image = cv2.cvtColor(np.array(clone_img), cv2.COLOR_RGB2BGR)
    cv2.namedWindow("NTC", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("NTC", 600, 600)
    cv2.imshow("NTC", cv_image)
    key_press = cv2.waitKey(0)
    if key_press == 43:  # Plus button is pressed on keyboard.
        # Increasing the font size.
        name_font_size += 2
    elif key_press == 45:   # Minus button is pressed on keyboard.
        # Decreasing the font size.
        name_font_size -= 2
    cv2.destroyWindow("NTC")


# Selecting the  output folder for certificate.
certificate_folder_path = filedialog.askdirectory(
    initialdir=os.getcwd(), title='Select the output folder to save certificate')

# Remove the sample file created.
os.remove("test.{}".format(image_file_extension))

# Original certificate image
cert_img = PILImage.open(certificate_file_path)

# Adding the font again.
name_font = (ImageFont.truetype(font_file_path,
                                name_font_size))

# Printing certificate using names in the list.
for names in tqdm(name_list):

    # Copying the original image.
    clone_img = cert_img.copy()

    d = ImageDraw.Draw(clone_img)
    text_w, text_h = d.textsize(names, font=name_font)

    text_x = (left_x + ((right_x - left_x) // 2)) * large_to_small_ratio - (text_w // 2)
    text_y = right_y * large_to_small_ratio - text_h
    d.text((text_x, text_y), names,
           fill=name_font_color, font=name_font)

    # Convert pillow image to opencv-image
    np_image = np.array(clone_img)
    opencv_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    # Saving the images to output folder.
    cv2.imwrite(os.path.join(certificate_folder_path, "{}.{}".format(
        names, image_file_extension)), opencv_image)

print("Certificate naming completed.")
