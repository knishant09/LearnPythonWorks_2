import os


def name_reverse(first_name, last_name):
    print first_name
    print last_name
    rev = last_name + " " + first_name
    return rev



if __name__ == "__main__":
    fname = str(raw_input("Enter your first name:"))
    lname = str(raw_input("Enter your last name:"))
    rev = name_reverse(fname, lname)
    print "Name in the reverse manner:%s" % rev