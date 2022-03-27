import os, shutil

j = 0
counter = 0
collectionx = []
source = (
    r"C:/Users/alric/Downloads/New folder (2)/License-20220325T124014Z-001/License/"
)
destination = (
    r"C:/Users/alric/Downloads/New folder (2)/License-20220325T124014Z-001/extra/"
)


def splite_filename(file):
    filename = file.split(".")
    return filename


def identify(i, filename):
    global counter
    file = len(filename[1:])
    for j in range(1, file):
        spliteFile1 = splite_filename(filename[i])
        spliteFile2 = splite_filename(filename[j])
        if spliteFile1[0] == spliteFile2[0] and (
            spliteFile1[2] == "png" or spliteFile2[2] == "xml"
        ):
            counter = counter + 1
            # print (filename[i], "\n", filename[j])
            return
    collectionx.append(filename[i])


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
while j < len(full_file_paths):
    identify(j, full_file_paths)
    j = j + 1
for f in collectionx:
    print(f)
print(counter)
