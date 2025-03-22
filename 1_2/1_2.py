try:
    file = open('mission_computer_main.log','r',encoding='utf-8')
#예외처리
except Exception as e:
    print("에러발생\n",e)

else:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    log_list = []
    for line in lines[1:]:
        log_list.append(line.strip().split(',',2))
    file.close()
    for i in log_list:
        print(i)
    log_list.sort(reverse=True)
    log_dict = {}
    for index, log in enumerate(log_list):
        log_dict[index] = {header[0]: log[0], header[1]: log[1], header[2]: log[2]}

    #json 파일로 저장
    json_file = open('1_2/mission_computer_main.json', 'w',encoding='utf-8')
    json_file.write('{')
    for k,v in log_dict.items():
        json_file.write('\n\t"%d":{"%s": "%s", "%s": "%s", "%s": "%s"},'%(k,header[0],v[header[0]],header[1],v[header[1]],header[2],v[header[2]]))
    json_file.seek(json_file.tell()-1)
    json_file.write('\n}')
    json_file.close()   

    #특정 문자열 찾기
    search = input('찾을 문자를 입력하세요 : ')
    for k,v in log_dict.items():
        if search in v[header[2]]:
            print(v[header[0]],':',v[header[1]],':',v[header[2]])
