# 11654번
a = input()
dType = type(a)

if dType == str:
	print(ord(a))
else: print(chr(a))

