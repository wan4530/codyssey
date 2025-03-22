print('Hello Mars')
try:
    f = open('mission_computer_main.log','r',encoding='utf-8')
except FileNotFoundError:
    print("FileNotFound")
else:
    fw = open('1_1/log_analysis.md','w',encoding='utf-8')
    line1 = f.readline()
    fw.writelines(line1)
    print(line1)
    line = f.readlines()
    for i in reversed(line):
        print(i, end ='')
        fw.write(i)
    f.close()
    fw.close()