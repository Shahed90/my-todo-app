filepath1 = "todos.txt"
def get_todos(filepath=filepath1):
    """Read a text file and return the todo list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=filepath1):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file1:
        file1.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
