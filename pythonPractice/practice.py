str = 'X-DSPAM-Confidence : 0.8475 '
a = str.find(':',)
# print(a)
b = str[a+2:]
# print(b)
c = float(b)
print(c)




