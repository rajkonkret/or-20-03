# 'r'       open for reading (default)
#     'w'       open for writing, truncating the file first - tworzy lun usuwa plik
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)

with open('test.log', 'w', encoding='utf-8') as f:  # f = filehandler
    f.write("Radek\n")
    f.write("Ola\n")
    f.write("Michał\n")

with open('test.log', 'a', encoding='utf-8') as fh:  # f = filehandler
    fh.write("Dopisane\n")

with open('test.log', 'r', encoding='utf-8') as fh:  # fh = filehandler
    lines = fh.read()
    print(lines)
    print(type(lines))

with open('C:\\Users\\CSComarch\\PycharmProjects\\or-20-03\\test2.log', 'r', encoding='utf-8') as fh:
    for x in fh:
        print(x, end="")
