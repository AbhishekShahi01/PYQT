from PIL import Image
import glob
image_list = []
for filename in glob.glob('Home/desktopapp/project/pyqt5/*.New folder'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
    print(image_list[1])
