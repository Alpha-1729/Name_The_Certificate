#!usr/bin/python3
# Code to add names automatically in the certificates using python.

# Importing the libraries.

from PIL import Image
import os,cv2,shutil
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import copy # for copying image.

# variable to store coordinates of the rectangular selector in the certicate.
global x1,y1,x2,y2
global image_path

# Path variables
img_folder="images"
certificate_folder="certificate"
certificate_name="certificate.jpg"
name_file="names.txt"

# getting the path of the image.
image_path=os.path.join(img_folder,certificate_name)


# reading the names from the file and added it to the list.
with open(name_file,"r") as file:
	names_list=[i.upper() for i in file.read().split("\n")]


def toggle_selector(event):
 toggle_selector.RS.set_active(True)

def onkeypress(event):
 global x1,y1,x2,y2

 if event.key == 'q':
 	 # Getting the coordinate of the rectangular selector.
     # print(x1,y1,x2,y2) 
     for names in names_list:
         clone_img = copy.copy(certificate_image) # copying the image.
         fontface = cv2.FONT_HERSHEY_COMPLEX # adding the font.
         fontsize = 0.8 # font-size
         fontcolor = (0, 0, 0) # color of the font->black
         font_thickness=2
         cv2.putText(clone_img,names, (x1,y2), fontface, fontsize, fontcolor,font_thickness) 
         cv2.imwrite(os.path.join(certificate_folder,"{}.jpg".format(names)),clone_img)     

def line_select_callback(clk, rls):
 global x1,y1,x2,y2
 x1=int(clk.xdata);y1=int(clk.ydata);x2=int(rls.xdata);y2=int(rls.ydata)



# setting the window manager to show the image
fig, ax = plt.subplots(1, figsize=(10.5, 8))
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry=(250, 40, 1000, 800)

# reading the image
image=cv2.imread(image_path)
certificate_image=copy.copy(image) # for certificate

# Converting to RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

ax.imshow(image)
toggle_selector.RS = RectangleSelector(
 ax, line_select_callback,
 drawtype='box', useblit=True,
 button=[1], minspanx=5, minspany=5,
 spancoords='pixels', interactive=True,
)
bbox = plt.connect('key_press_event', toggle_selector)
key = plt.connect('key_press_event', onkeypress)
plt.tight_layout()
plt.show()
plt.close(fig)
print("Process is completed. Thank You")
















