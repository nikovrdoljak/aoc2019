class Util:

    @staticmethod
    def getListFromFile(file_location):
        fhand = open(file_location)
        list = []
        for line in fhand:
            list.append( line.rstrip() )
        return list
