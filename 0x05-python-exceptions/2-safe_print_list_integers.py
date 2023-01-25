#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:    
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
    except TypeError:
        pass
    except ValueError:
        pass
    else:
        count += 1
    print()
    return count
