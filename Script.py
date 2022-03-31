import os

count = 0
collection_xml = []
collection_png = []
collection= []
source = (
    r"C:/Users/alric/Downloads/New folder (2)/License-20220325T124014Z-001/License/"
)
destination = (
    r"C:/Users/alric/Downloads/New folder (2)/License-20220325T124014Z-001/extra/"
)

#Takes the filename and splites the filename at "." and returns them in form of list.
def splite_filename(file):
    filename = file.split(".")
    return filename

"""Takes the splited filename and classifies them into png and xml, 
hence appending the filename and the image in their respective
collections."""
def xml_files(filename):
    for x in filename:
        splite=splite_filename(x)
        if splite[2]=="png":
            collection_png.append(x)
        elif splite[2]=="xml":
            collection_xml.append(x)
    print('Done')

#Appending the common png and xml into a collection by checking for common filename.
def binding():
    for x in collection_png:
        splite_png=splite_filename(x)
        for y in collection_xml:
            splite_xml=splite_filename(y)
            if (splite_png[0:2]==splite_xml[0:2]):
                collection.append(x)
                collection.append(y)

#Moving files from source to destination.
def move():
    global count
    for f in collection:
        os.rename(source + f, destination + f)

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:

            file_paths.append(filename)  # Add it to the list.

    return file_paths  # Self-explanatory.


# Run the above function and store its results in a variable.
full_file_paths = get_filepaths(
    r"C:\Users\alric\Downloads\New folder (2)\License-20220325T124014Z-001\License"
)
xml_files(full_file_paths)
binding()
move()
for x in collection:
    print(x)
print(len(collection_xml))
print(len(collection_png))
print(len(collection))
