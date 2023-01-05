# import required module
import glob
 
# get the path/directory
folder_dir = 'New folder'
 
image_list = []
# iterate over files in
# that directory
for images in glob.iglob(f'{folder_dir}/*'): #f'{folder_dir}/*'
    #image_list.append(images)
    # check if the image ends with png
    if (images.endswith(".png")):
        image_list.append(images)
        #print(images)
print(image_list)
print(image_list[-1])
print(image_list[0])
print(image_list[-5])
