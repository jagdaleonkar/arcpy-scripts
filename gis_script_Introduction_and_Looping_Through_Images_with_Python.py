import os 

img_folder = r'C:\GeoTaggedImages'
img_contents = os.listdir(img_folder)

for image in img_contents:
    print(image)
    full_path = os.path.join(img_folder, image)
    print(full_path)