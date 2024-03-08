def write_file(file_name, file_content):
    """Write content to a .txt file."""
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append content to a .txt file."""
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Read content from a .txt file."""
    with open(f'{file_name}.txt', 'r') as f:
        file_content = f.read()
    return file_content

write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

log_content = read_file(file_name="logfile")
print(log_content)