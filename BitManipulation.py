class BitHelper():

    @staticmethod
    def getBit(num: int, i: int):
        return ((num & (1 << i)) != 0)
    
    def setBit(num: int, i: int, target: bool):
        
        return 

    @staticmethod
    def booleanToInt(bit: bool):
        return (1 if bit else 0)

    @staticmethod
    def formatIntToBinary(num: int):
        return "{0:b}".format(num)
    
    

if __name__ == "__main__":
    num = 31
    i = 3
    print(BitHelper.formatIntToBinary(num), 
          "Get Bit : " + str(i), 
          BitHelper.booleanToInt(BitHelper.getBit(num, i)));    