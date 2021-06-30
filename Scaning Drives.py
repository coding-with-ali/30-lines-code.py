import os ,stat
global i
i=0
def scanfile(drive):
    try:
        with os.scandir(drive) as dr:
            for entry in dr:
                if entry.name.endswith('.mp4') and entry.is_file():
                    print(entry.name)
                    print(entry.path)
                    global i
                    i=i+1
                elif os.path.isdir(entry):
                    scanfile(entry)
    except PermissionError as e:
        # print(e)
        pass
    except WindowsError as y:
        # print(y)
        pass

import shutil
import logging
# import timeit
def copyfiles(file):
    with os.scandir(file) as d:
        for entry in d:
            logging.info('currnetly working on {} '.format(entry))
            shutil.copy(entry,'E://')



if __name__ == '__main__':
    import timeit
    print(timeit.Timer("copyfiles('D:\Academic Videos\Website Development course Udemy')", setup="from __main__ import copyfiles").repeat(1,1))
    # copyfiles('D:\Academic Videos\Python\Long Video Tutorial')

# scanfile('D:\\')
# print(i)