import socket
import urllib.request, urllib.parse, urllib.error

# Socket
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Stream 형태의 소켓
# mysocket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysocket.send(cmd)
#
# while True:
#     data = mysocket.recv(512)
#     if(len(data) < 1):
#         break
#     print(data.decode(), end='')
# mysocket.close()
# print('')

# Urllib
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# Urllib + Dictionary
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# Google
fhand = urllib.request.urlopen('http://www.google.com')
for line in fhand:
    print(line.decode().strip())


# ASCII

# print(ord('H'))
# print(ord('e'))
# print(ord('\n'))