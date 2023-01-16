FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text  file and return the list of to-do items.
    :param filepath:this is default argument needed to store todos in text file.
    :return:it returns the contents in text file as list.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if "__name__" == "__main__":
    print("Checking the execution")
