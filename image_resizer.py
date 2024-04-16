import cv2
import os

# Define the folder containing images
folder_path = r'C:\Users\alexd\OneDrive\Desktop\pokemon\pokemon_images_original\pokemon_images\zorua_images'

# Define the output folder for resized images and create it if it doesn't exist
output_folder = r'C:\Users\alexd\OneDrive\Desktop\pokemon\pokemon_images_original_resized\pokemon_images\zorua_images_resized'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Read the image
        img = cv2.imread(os.path.join(folder_path, filename))
        
        # Check if the image was read successfully
        if img is None:
            print(f"Failed to read image {filename}")
            continue
        
        # Crop image to square size based on smallest dim
        h, w = img.shape[:2]
        if h < w:
            start = (w - h) // 2
            end = start + h
            cropped_img = img[:, start:end]
        else:
            start = (h - w) // 2
            end = start + w
            cropped_img = img[start:end, :]

        img = cropped_img

        # Resize the image to 256x256 pixels
        resized_img = cv2.resize(img, (256, 256))
        
        # Generate the new filename with .jpg extension
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        
        # Write the resized image to the output folder as JPG
        cv2.imwrite(os.path.join(output_folder, new_filename), resized_img)