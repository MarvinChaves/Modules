class Detectors:
    def __init__(self):
        pass

    def comparing(value1=0, comp='', value2=0):
        '''

        returns True or False

        ex:

            Itelligence.comparing(4, ==, 5)
                                  
            console:

                False

        '''


        compare = str(comp)

        if compare == '==':
            if value1 == value2:
                return True
            
            else:
                return False
        
        elif compare == '!=':
            if value1 != value2:
                return True
            
            else:
                return False
        
        elif compare == '>':
            if value1 > value2:
                return True
            
            else:
                return False
        
        elif compare == '<':
            if value1 < value2:
                return True
            
            else:
                return False
        
        elif compare == '>=':
            if value1 >= value2:
                return True
            
            else:
                return False
        
        elif compare == '<=':
            if value1 <= value2:
                return True
            
            else:
                return True


    def numType(num):
        '''
        
        returns the type of a number

        ex:

            Itelligence.numType(10)

            console:

                Type: <int>, Positive

        '''

        if type(num) == int:
            if num > 0:
                return 'Type: <int>, Positive'
            
            elif num < 0:
                return 'Type: <int>, Negative'
            
            elif num == 0:
                return 'Type: <void>, Void'
        
        elif type(num) == float:
            if num > 0:
                return 'Type: <float>, Positive'
            
            elif num < 0:
                return 'Type: <float>, Negative'
            
            elif num == 0:
                return 'Type: <void>, Void'


