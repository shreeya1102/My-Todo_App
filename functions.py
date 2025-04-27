def get_todo(filepath="todos.txt"):
    """
    Read the text file and return list of to-do items

    """

    with open(filepath, 'r') as file_local:
        todos_1 = file_local.readlines()
    return todos_1


def write_todos(todos_arg, filepath="todos.txt"):
    """
    Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todo())
