import os

def strhex(string, start = '\0x'):
    return start+''.join(('{:x}'.format(ord(char))).zfill(2) for char in string)


def hexstr(txt):
	txt = txt.replace("\0x","")
	return ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])

hex = strhex("6041f")
print(hex)
cad = hexstr("\0x6041f")
print(cad)

# newFileBytes = [123, 3, 255, 0, 100]
# newFileByteArray = bytearray()
# newFileByteArray.extend(map(ord,hex))

# # file = open("file_bin.txt","wb")
# # file.write(newFileByteArray)
# # file.close()

# file = open("file_bin.txt", 'rb')
# print(file)
# for ca in file:
# 	print(ca.decode("utf-8"))
# 	print(hexstr(ca.decode("utf-8")))