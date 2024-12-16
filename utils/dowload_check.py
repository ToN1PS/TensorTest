import os


def check_size_matching(text: str, file_path: str, file_name: str) -> bool:
    """Checks if the file size listed on the website matches the actual size of the downloaded file.

    Args:
        text (str): A string containing the file size information obtained from the website.
        file_path (str): The path to the folder where the file was downloaded, without the file name.
        file_name (str): The name of the downloaded file.

    Returns:
        bool: True if the string representation of the file size (in MB) is contained in the text,
              False otherwise.
    """
    file_path = file_path + file_name

    size_bytes = os.path.getsize(file_path)
    size_MB = round(size_bytes / (1024**2), 2)

    return str(size_MB) in text
