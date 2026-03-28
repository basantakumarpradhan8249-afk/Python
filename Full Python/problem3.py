import os

# Specify the directory you want to list
# (or leave blank to use current directory)
directory = "/"

try:
    # Get the list of entries in the directory
    entries = os.listdir(directory)

    # Print each entry
    print(f"Contents of directory '{directory}':")
    for entry in entries:
        print(entry)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: Permission denied.")
