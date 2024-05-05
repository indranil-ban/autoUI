import os

def get_filepaths(directory):
    file_paths = []  # Initialize an empty list to store file paths

    # Walk through the directory and its subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Construct the full file path by joining the root and filename
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths