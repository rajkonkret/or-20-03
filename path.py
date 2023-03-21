import os

user_folder = os.path.expanduser("~")
print(user_folder)

file_name = 'test2.log'
file_path = os.path.abspath(file_name)
print(file_path)
