# pylint: disable-all
import sys
import os

def initiate_search():
    
    ## Ask the user for the word they want to search for
    word = input("Enter a word to search: ")
    path = input("Enter the directory: ")
    search_file(word, path)

## A function that reads through a file for the user's given word
def search_file(search_word, dir_path):
    file_ext = ".txt"
    wordcount = 0
    list_of_matching_files = {}

    ## Validation of path to check it is in the right format
    if not os.path.exists(dir_path):
        print("Path does not exist we will search your current directory")
        dir_path ="."

    if not (dir_path.endswith("/") or dir_path.endswith("\\") or dir_path.startswith("/")): 
        dir_path = dir_path + "/"

    listdir = os.listdir(dir_path)
    # import pdb; pdb.set_trace()
    # List all .txt files in the directory
    for file_name in listdir:
        # for each file file_name read the file and increment 
        if file_name.endswith(file_ext):
            internal_wordcount = 0
            searchfile = open(dir_path + file_name, 'r')
            # Read all lines in the file one by one
            line = searchfile.readline()
            # For each line, check if line contains the string
            while line != '' :
                if search_word in line:
                    internal_wordcount += 1
                line = searchfile.readline()
                list_of_matching_files[file_name] = internal_wordcount
            searchfile.close()
    sort_dict_by_vale(list_of_matching_files)
    iterate_through_dict(list_of_matching_files)

## Loop through the values and output an ordered string
def iterate_through_dict(files):
    print(f"Top matching results for word")
    for key, value in files.items():
        print(f"Found {value} times in {key}")

## Arrange the dictionary from highest to lowest
def sort_dict_by_value(given_dict):
    sorted_values = sorted(given_dict.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in given_dict.keys():
            if given_dict[k] == i:
                sorted_dict[k] = given_dict[k]
                break

## This will run the search_file() method as main
if __name__ == '__main__':
    initiate_search()