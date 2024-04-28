import os

_TEXT_CACHE = {}


def load_text_file(relative_path):
    """
    Load the content of a text file.

    Args:
        relative_path (str): The relative path to the text file.

    Returns:
        str: The content of the text file as a string.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        IsADirectoryError: If the specified path is a directory.
    """
    file_path = os.path.join(os.path.dirname(__file__), relative_path)
    # Check if the file path is valid
    if not os.path.isfile(file_path):
        if os.path.isdir(file_path):
            raise IsADirectoryError(f"{file_path} is a directory, not a file.")
        raise FileNotFoundError(f"{file_path} does not exist.")

    # Check if the file content is cached
    if file_path in _TEXT_CACHE:
        return _TEXT_CACHE[file_path]

    # Load the text content
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    _TEXT_CACHE[file_path] = text_content

    return text_content
