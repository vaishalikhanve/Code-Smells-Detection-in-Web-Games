import os, zipfile

dir_name = r'C:\Users\minni\Downloads'
extension = ".zip"

for item in os.listdir(dir_name): 
    if item.endswith(extension): 
        file_name = dir_name + "/" + item 
        zip_ref = zipfile.ZipFile(file_name) 
        zip_ref.extractall(dir_name) 
        zip_ref.close() 
