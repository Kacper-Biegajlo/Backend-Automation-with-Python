with open('test.txt', 'r') as reader: #file opened in read mode
    content = reader.readlines()
    reversed(content) # reversing content in the list
    with open('test.txt', 'w') as writer: #file opened in write mode
        writer.writelines(reversed(content)) 
        # can also use for line in reversed(content): writer.write(line)

