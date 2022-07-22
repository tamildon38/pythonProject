file = open('test')
print(file.readline())
print(file.read(5))
file.close()


with open('test','r') as reader:
    content = reader.readline()
    reversed(content)
    with open('test','w') as writer:
        for line in reversed(content):

            writer.write(line)
            
