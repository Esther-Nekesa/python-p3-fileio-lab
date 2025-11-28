# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a .txt file, overwriting existing content.
    The file_name is converted to string to correctly append the extension.
    """
    
    full_file_name = str(file_name) + ".txt"
    
    # Open the file in 'w' (write) mode.
    with open(full_file_name, 'w') as f:
        f.write(file_content)
pass

def append_file(file_name, append_content):
    """
    Appends content to the end of a .txt file.
    """
    # Fix: Convert the Path object to a string before concatenating.
    full_file_name = str(file_name) + ".txt"
    
    # Open the file in 'a' (append) mode.
    with open(full_file_name, 'a') as f:
        f.write(append_content)
pass

def read_file(file_name):
    """
    Reads and returns the entire content of a .txt file.
    """
    # Fix: Convert the Path object to a string before concatenating.
    full_file_name = str(file_name) + ".txt"
    
    # Open the file in 'r' (read) mode.
    with open(full_file_name, 'r') as f:
        # Use read() to return the entire content as a single string
        return f.read()
pass