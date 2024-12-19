# Read from File we use 'r'
f = open("My File", 'r')
# print(f.read())

# write to a file 'w'

r = open("CopyofMyFile", 'w')
for i in f:
    r.write(i)

sno= open("CopyofMyFile", 'a')
sno.write("I am a music composer")

img= open("Demo.JPG", 'rb')


cimg= open("copyDemo.JPG",'wb')
for i in img:
    cimg.write(i)