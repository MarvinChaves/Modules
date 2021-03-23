import os

class System:
    def __init__(self):
        pass

    def startApplication(name):
        'star a application'
        os.system(f'start {name}')
    

    def createPyExecutable(name):
        'creates a pythonFile.exe'
        os.system(f'pyinstaller {name}')
    
