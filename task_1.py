import shutil
import os
from pathlib import Path


def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [entry.path for entry in os.scandir(path)]


def read_directory_recursive(directory, files_dictionary):
    for element in absolute_file_paths(directory):
        if os.path.isfile(element):
            extension = os.path.splitext(element)[1][1::]

            if not extension in files_dictionary:
                files_dictionary[extension] = []

            files_dictionary[extension].append(element)
        else:
            read_directory_recursive(element, files_dictionary)


def copy_files(destination_directory, files_dictionary):
    for extension in files_dictionary:
        dir_path = os.path.abspath(os.path.join(os.sep, destination_directory, extension))

        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        
        for file in files_dictionary[extension]:
            shutil.copy(file, dir_path)
            

def main():
    source_directory = input('Type source directory:\n')
    destination_directory = input('Type destination directory:\n')

    try:
        if not os.path.isdir(source_directory):
            print('Source directory is not directory!')
            return -1

        if destination_directory == '':
            destination_directory = os.path.abspath(os.path.join(os.sep, source_directory, 'dist'))
        else:
            destination_directory = os.path.abspath(os.path.join(os.sep, source_directory, destination_directory))

        files_dict = {}
        read_directory_recursive(source_directory, files_dict)
        copy_files(destination_directory, files_dict)
    except Exception as inst:
        print('We have an exception:', type(inst))    # the exception type   # arguments stored in .args
        print(inst)          

    print('\nFiles copied. Goodbye!')


if __name__ == '__main__':
    main()
