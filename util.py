class Util:


    @staticmethod
    def getStringFromFile(file_location):
        fhand = open(file_location)
        return fhand.read()

    @staticmethod
    def getListFromFile(file_location):
        fhand = open(file_location)
        list = []
        for line in fhand:
            list.append( line.rstrip() )
        return list

    
    @staticmethod
    def createZeroMatrix(x, y):
        """ creates 2D array of zeros (used in day 3) """
        a = [[0] * x for i in range(y)]
        return a

    @staticmethod
    def maxInt():
        return 9223372036854775807