try:
    with open('Mars_Base_Inventory_List.csv','r',encoding='utf-8') as f:
        lines = f.readlines()
    for i in lines:
        print(i,end='')
    header = lines[0].strip().split(',')
    inven_list =[]
    for line in lines[1:]:
        inven_list.append(line.strip().split(','))
    #inven_list 인화성 지수 내림차순 정렬
    inven_list.sort(key = lambda x: float(x[4]),reverse=True)
    #danger_list에 인화성 지수가 0.7이상인 값 append
    danger_list = []
    for i in inven_list:
        if(float(i[4]) >= 0.7):
            danger_list.append(i)
    #인화성 지수 0.7 이상인 값들 출력력
    for i in danger_list:
        print(i)
    #인화성 지수 0.7이상인 값들 csv포멧(Mars_Base_Inventory_danger.csv)으로 저장
    with open('1_3/Mars_Base_Inventory_danger.csv','w',encoding='utf-8') as danger_file:
        danger_file.write('%s,%s,%s,%s,%s\n'%(header[0],header[1],header[2],header[3],header[4]))
        for i in danger_list:
            danger_file.write('%s,%s,%s,%s,%s\n'%(i[0],i[1],i[2],i[3],i[4]))
except Exception as e:
    print("에러발생\n",e)