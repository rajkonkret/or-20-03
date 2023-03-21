fh = open('test.log', 'a')  # a append - dodaje do konca pliku
fh.write("Test")
fh.close()

with open('test.log', 'r', encoding='utf-8') as fh:  # fh = filehandler
    lines = fh.read()
    print(lines)
    print(type(lines))
