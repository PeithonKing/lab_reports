import os
import time

files = []

for file in os.listdir():
    if file.endswith(".tex"):
        files.append(file)

for file in os.listdir("sections"):
    if file.endswith(".tex"):
        files.append("sections/"+file)

def get_file(file):
	with open(file) as f:
		return f.read()

data = {file:get_file(file) for file in files}
# data = {file:"" for file in files}

while True:
    for file in files:
        with open(file) as f:
            text = f.read()
            if data[file] != text:
                print(f"Change in {file} detected at {time.ctime()}. Compiling project... ", end="")
                # print(list(difflib.ndiff(data[file], text)))
                data[file] = text
                t0 = time.time()
                os.system("pdflatex main.tex --quiet")
                print(f"Done in {(time.time() - t0):.2f}s!")
                os.system("python clean.py")
                break
    
    time.sleep(2)