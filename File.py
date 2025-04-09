with open("../files/wyx.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

with open("../files/xf.txt", 'a', encoding='utf-8') as f:
    f.write("hello world\n")
