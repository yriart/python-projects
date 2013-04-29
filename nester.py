"""This is the "nester.py" module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists."""

def print_lol(the_list,tabs=0):
    """this function takes a positional argument called "the list",
    which is any Python list (of, possibly, nested lists), and a
    second positional argument called "tabs", which is the number of
    tabs to place before nested items. Each data item in the provided
    list is (recursively) printed to the screen on its own line."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, tabs+1)
        else:
            for each_tab in range(tabs):
                print("\t",end="")
            print(each_item)
