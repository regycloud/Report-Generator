from percentileFinder import findValue

newNameFile = '{} - SSPL.MIX1.011.png'.format(29)
result = findValue('./imgs/table/{}'.format(newNameFile))
print(result)