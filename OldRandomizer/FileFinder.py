import os

def file_is_filetype(filename, filetypes):
    return any(f in filename for f in filetypes)

def get_files_from_folder(folder_path, filetypes):
    selected_files = []
    for root, dirs, files in os.walk(folder_path):
        selected_files.extend([os.path.join(root, f) for f in files if file_is_filetype(f, filetypes)])
    return selected_files

def get_files_of_type_from_folders(folders, filetypes):
    return sum([get_files_from_folder(folder, filetypes) for folder in folders], [])