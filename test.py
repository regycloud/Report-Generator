from itertools import count
import re

def custome(startDate, endDate):
    result = []
    counterDate = startDate
    while(int(counterDate) < int(endDate)):
        if (counterDate < 10):
            counterDate = '0{}'.format(counterDate)
            result.append(counterDate)
            counterDate = int('{}'.format(counterDate))
        counterDate +=1 
    print(result)

custome(3, 11)