def file_handling(filename, content):
    with open (filename, "a") as f:
        f.write(content)

    with open (filename, "r") as f:
        content = f.read()