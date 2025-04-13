import csv
import random

# with open("../files/CSVTest.csv",'w',newline='',encoding='gb2312') as file:
#     writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名','语文','数学','英语'])
#     names= ['张三','李四','王五','赵六']
#     for name in names:
#         scores=[random.randrange(90,150) for i in range(3)]
#         scores.insert(0,name)
#         writer.writerow(scores)
with open("../files/CSVTest.csv",'r') as file:
    reader = csv.reader(file)
    for data_list in reader:
        print(reader.line_num,end="\t")
        for elem in data_list:
            print(elem,end="\t")
        print()