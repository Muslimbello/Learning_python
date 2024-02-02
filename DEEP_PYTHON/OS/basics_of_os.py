""" i  created a program that created folder then deleted it using the os module in python
"""
import os


current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")
new_dir = "os"
os.mkdir(new_dir)
files = os.listdir(current_directory)
print({f" imitates the ls function{files}"})
os.rmdir(new_dir)
print(f"Removed directory: {new_dir}")
