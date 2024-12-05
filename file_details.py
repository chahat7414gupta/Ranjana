# import os
# import stat
# import time
# import sys
#
# from Demos.FileSecurityTest import permissions
# from anaconda_navigator.utils.url_utils import file_name
#
#
# def print_file_details(file_name):
#     try:
#         if not os.path.exists(file_name):
#             print(f"Error: The file '{file_name}' does not exist.")
#             return
#         file_stat = os.stat(file_name)
#         permissions = stat.filemode(file_stat.st_mode)
#         access_time = time.ctime(file_stat.st_atime)
#
#         print(f"File 1: {file_name}")
#         print(f"Permissions 2: {permissions}")
#         print(f"Owner UID 3: {file_stat.st_uid}")
#         print(f"Group GID: {file_stat.st_gid}")
#         print(f"Last Access Time: {access_time}")
#         print(f"Size: {file_stat.st_size} bytes")
#
#     except Exception as e:
#         print(f"An error occured: {e}")
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python file_details.py <file_name>")
#     else:
#         file_name = sys.argv[1]
#         print_file_details(file_name)
import os

# f = open("demofile.txt", "r")
# print(f.read())

# Open the file and read its contents
file_name = "demofile.txt"
# Open the file in read mode
with open(file_name, "r") as f:
    content = f.read()
    print("File Contents:")
    print(content)

# Get file size
file_size = os.path.getsize(file_name)

# Get file extension
file_extension = os.path.splitext(file_name)

# Print file details
print("\nFile Details:")
print(f"File Name: {file_name}")
print(f"File Size: {file_size} bytes")
print(f"File Extension: {file_extension}")
