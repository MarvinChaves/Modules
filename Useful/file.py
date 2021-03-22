import os
import sys

class File:
    def __init__(self):
        pass

    def create(name, openIt=False):
        '''
        
        creates a file
        
        ex:

            File.create(fileName.txt, False/True)

            the 2ª parameter is to open it
        '''
        open(name, 'w+')

        if openIt == False:
            pass

        elif openIt == True:
            os.system(f'start {name}')

    
    def openFile(name):
        'open a file'
        os.system(f'start {name}')
        

    def deleteFile(name):
        '''

        write the path of the file to delete it

        ex:

            File.deleteFile('C:\Users\marvin\Desktop\FileName.txt')
        
        '''
        os.system(f'del /f /a {name}')
        