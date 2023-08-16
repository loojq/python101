# Move and rename all .png files on your Desktop (done this on a test folder instead)

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib
#working directory?
current_path = pathlib.Path.home()

test_folder = pathlib.Path("C:/Users/looji/OneDrive/Documents/Testing_files")
test_folder.mkdir(exist_ok=True)
new_folder = pathlib.Path("C:/Users/looji/OneDrive/Documents/Testing_files/another_test")
new_folder.mkdir(exist_ok=True)
#
counter = 0
for filepath in test_folder.iterdir():
    counter += 1
    if filepath.suffix == ".docx":
        #creating a new path for each file
        #filepath.rename("success" + str(counter))
        new_name = f"my document-{counter}{filepath.suffix}"
        print(new_name)
        new_filepath = filepath.joinpath(new_name)
        #moving the files into another folderw
        #new_filepath = filepath.replace(new_filepath)
        filepath.replace(filepath.joinpath(new_filepath))


