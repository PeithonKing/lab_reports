import os

white_files = [
    'main.tex',
    'apssamp.bib',
    'fig_1.eps',
    'fig_2.eps',
    'vid_1a.eps',
    'vid_1b.eps',
    'main.pdf',
]

white_ext = [
    ".py",
    ".ipynb",
    ".xlsx",
    ".csv",
]

l = os.listdir()


def keep(file):
    if os.path.isdir(file):
        return True
    if sum(map(lambda x: file.endswith(x), white_ext)):
        return True
    if file in white_files:
        return True
    return False

n = 0
for file in l:
    if keep(file):
        print('Removing: ' + file)
        os.remove(file)
        n += 1

if n == 0:
    print('No files removed.')
else:
    print(f'{n} files removed.')