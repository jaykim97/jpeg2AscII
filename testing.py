hold ="""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\|()1{}[]?-_+~<>i!lI;:,"^`'. """
hold =" .:-=+*#%@"
# hold = hold[::-1]
current=255
for i in range(70):
    print("elif i > ", current,":")
    print('c="{}"'.format(hold[i]))
    current -= 15
