import os


file_input = str(raw_input("Enter the filename with an extension:"))

ext = file_input.split('.')
print ext[1]
