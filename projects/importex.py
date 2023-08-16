#import pathlib
import pathlib

#find the path to my desktop
path = pathlib.Path.home() #returns the path of the working directory
#print(str(path))

#list all the files in there 
desktop = path / "OneDrive"/ "Desktop"
#for filepath in desktop.iterdir():
    #print(filepath.name)

#create a new folder
new_path = pathlib.Path("C:/Users/looji/OneDrive/Desktop/png")
new_path.mkdir(exist_ok=True) #if file already exists that's fine. override

#filter for screenshots only
for filepath in desktop.iterdir():
    if filepath.suffix == ".png":
        #print(filepath.suffix)

#create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)

#move the screenshots in there
        filepath.replace(new_filepath)








