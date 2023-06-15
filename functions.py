FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Reads the list from the text file and returns the list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """Writes the list into the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
