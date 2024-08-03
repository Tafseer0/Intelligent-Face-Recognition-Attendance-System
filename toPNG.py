from PIL import Image
import os

def toPNG():
    # Specify the input folder containing the images
    input_folder = "rawImages"

    # Specify the output folder for converted PNG images
    output_folder = "Images"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Convert images to PNG and delete original files
    for filename in image_files:
        file_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

        try:
            img = Image.open(file_path)
            img.save(output_path, "PNG")
            img.close()

            # Delete the original image
            os.remove(file_path)
            
            print(f"Converted and deleted: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
