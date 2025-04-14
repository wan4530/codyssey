try:
    import numpy

    main_parts_1 = numpy.genfromtxt('1_5/mars_base_main_parts-001.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
    main_parts_2 = numpy.genfromtxt('1_5/mars_base_main_parts-002.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
    main_parts_3 = numpy.genfromtxt('1_5/mars_base_main_parts-003.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
    #3개의 ndarray들을 merge하기
    parts = numpy.concatenate((main_parts_1,main_parts_2,main_parts_3))
    #평균 구해서 parts_avr에 append하기
    parts_avr = []
    for i in main_parts_1:
        name = i[0]
        values = [j[1] for j in parts if j[0] == name]
        avr = round(sum(values)/len(values),2)
        parts_avr.append([str(name), float(avr)])
    #각 항목의 평균값 출력
    print('-'*15,'parts average','-'*15)
    for i in parts_avr:
        print(i)
    print()
    #평균값이 50보다 작은 값들을 뽑아 parts_to_work_on.csv 파일에 저장
    with open('1_5/parts_to_work_on.csv','w',encoding='utf-8') as work_file:
        for i in parts_avr:
            if i[1]<50:
                work_file.write('%s,%0.2f\n' %(i[0], i[1]))
    #parts_to_work_on.csv 를 읽어 parts2에 저장하고 출력하기
    with open('1_5/parts_to_work_on.csv','r',encoding='utf-8') as f:
        lines = f.readlines()
    parts2 = []
    for i in lines:
        parts2.append(i.strip().split(','))
    print('-'*15,'parts2','-'*15)
    for i in parts2:
        print(i)
    print()
    #parts2의 전치행렬을 parts3에 저장하고 출력하기
    parts3 = numpy.transpose(parts2)
    print('-'*15,'parts3','-'*15)
    for i in parts3:
        print(i)
except Exception as e:
    print("에러발생\n",e)
