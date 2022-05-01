import os

# you give this function dir1 dir2 file which are in the assets folder
# it will return the abs path of the file where you are on the 
# system(inside this project)
def getPath(*args):
    return os.path.join(os.getcwd().split(f'{os.sep}assets{os.sep}')[0], "assets", os.path.join(*args))
