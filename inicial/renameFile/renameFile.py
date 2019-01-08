'''
renameFile use import: os
	rename the files of a particular folder in order to decrypt a message
'''

import os

dictionary = str.maketrans("^", "~", "0123456789")

# you can enter the path manually by changing the parameter
path = ( os.getcwd())

fileNames = os.listdir(path)
os.chdir(path)

for index in fileNames:
    
    print(index + ' \n|\n-------------------> ' + index.translate(dictionary)+'\n')
    os.rename(index, index.translate(dictionary))
    
os.chdir(path)

print('\nCompleted')
