#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if a_list == search else a_list for a_list in my_list]
    return new_list
