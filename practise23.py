'''
import zipfile
import os

with zipfile.ZipFile("new.zip", "w") as python:
    python.write("new1/s.text")
    python.write("new1/r.text")


import zipfile
import os

with zipfile.ZipFile("new.zip","r") as python:
    python.extractall()
    extracted_files=python.namelist()
    print(extracted_files)

'''

import shutil

shutil.make_archive("new_new","zip","new1")