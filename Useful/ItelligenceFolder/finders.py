class Finders:
    def __init__(self):
        pass

    
    def valueFinder(lists, value):
        '''
        in list param, put a list to find a value
        in value param, put a value to find in list
        '''
        o = 0
        for values in lists:
            if value == values:
                return o
            
            o += 1
    

    def fileTypeFinder(fileName):
        '''
        
        This function returns the file type

        '''

        try:
            fileOpen = open(fileName)
            fileOpen.close()

        except FileNotFoundError:
            print(f"The file {fileName} does not exist")
        
        else:
            if '.' in fileName:
                lastDot = '.'.find(fileName)
            
            else:
                print(f'The file {fileName} have not a type')

            fileType = fileName[lastDot - 1:]

            return fileType



        