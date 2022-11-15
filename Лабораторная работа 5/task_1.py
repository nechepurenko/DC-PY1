from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
pprint([({"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)}) for num in range(16)])
