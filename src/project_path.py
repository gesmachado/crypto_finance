import os


def get_root_path():
    root_dir = os.path.abspath(os.pardir)
    return root_dir


def get_path_file():
    root_dir = get_root_path()
    path_file = root_dir + '/files/response.json'

    return path_file
