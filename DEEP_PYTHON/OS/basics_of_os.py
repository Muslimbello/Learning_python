""" i  created a program that created folder then deleted it using the os module in python
"""
import os


current_directory = os.getcwd()
print(f"imitates the PWD function: {current_directory}")
new_dir = "os"
os.mkdir(new_dir)  # imitates the mkdir shell command
files = os.listdir(current_directory)
print({f" imitates the ls function{files}"})
os.rmdir(new_dir)
print(f"imitates the rmdir or rm -r command: {new_dir}")
