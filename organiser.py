import os
import shutil 

# CHECKING THE FOLDER AND READING EVERY FILE
folder = r"C:\Users\Aadi Jain\OneDrive\Desktop\jee"

files = os.listdir(folder)
print(f"number of files: {len(files)}")

#dictionary

categories = {

  
    ".pdf": "Documents",
    ".docx": "Documents",
    ".png": "Images",
    ".jpg": "Images",
    ".mp3": "Music"


}

for file in files:
    name, extension = os.path.splitext(file)
    if extension in categories:
        category = categories[extension]
    else:
        category = "Others"
    print(f"{file}->{categories}")
    # DESTINATION OF THE FILE AFTER SORTING 

    destination_folder = os.path.join(folder, category)
    os.makedirs(destination_folder, exist_ok=True)
    print(destination_folder)

     #SHIFTING THE FILES 

    source_path = os.path.join(folder,file)
    destination_path = os.path.join(destination_folder,file)
    shutil.move(source_path,destination_path)

print(f"Moved {file} to {category}")