# Python program to explain shutil.copyfile() method

# importing os module
import os

# importing shutil module
import shutil


# Source path
source = "/home/User/Documents/file.txt"

# Destination path
destination = "/home/User/Documents/file(copy).txt"

# Copy the content of
# source to destination
dest = shutil.copyfile(source, destination)



# Print path of newly
# created file
print("Destination path:", dest)
