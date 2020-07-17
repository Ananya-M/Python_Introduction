import os    
files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)]
print(files_no_ext)
