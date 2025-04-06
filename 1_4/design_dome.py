#전역변수 초기화
material = ''
diameter = 0
thickness = 0.0
area = 0.0
weight = 0.0

def sphere_area(input_diameter, input_material = '유리', input_thickness = 1.0):
    global diameter, material, thickness, area, weight

    diameter = input_diameter
    material = input_material
    thickness = input_thickness
    materials_dict = {
        '유리': 2.4,
        '알루미늄': 2.7,
        '탄소강': 7.85
    }
    #면적
    r = diameter / 2
    area = (r**2) * 3.1415 *2
    area *= 10000       #m^2 ->cm^2
    #무게
    weight = (area * thickness) * materials_dict[material]
    weight /= 1000      #g->kg
    weight *= 0.378     #지구 중력의 0.378배  = 화성 중력
    
    area = round(area, 3)
    weight = round(weight, 3)
    return area,weight

while True:
    #재질 입력
    while True:
        input_material = input('material: ')
        if input_material in ['유리','알루미늄','탄소강']:
            break
        else:
            print('재질은 [유리, 알루미늄, 탄소강] 중 하나여야 합니다.')

    #지름 입력
    while True:
        try:
            input_diameter = float(input('diameter(m): '))
            if input_diameter > 0:
                break
            else:
                print("지름은 0보다 커야 합니다.")
        except ValueError:
            print("숫자를 입력해야 합니다.")

    #두께 입력
    while True:
        try:
            input_thickness = float(input('thickness(cm): '))
            break
        except ValueError:
            print("숫자를 입력해야 합니다.")

    sphere_area(input_diameter, input_material, input_thickness)
    print(
        f'재질 =⇒ {material}, 지름 =⇒ {diameter}m, 두께 =⇒ {thickness}cm, 면적 =⇒ {area}cm^2, 무게 =⇒ {weight}kg'
    )
    #종료료
    end = input('계산을 종료하시겠습니까?(yes/no)')
    if end == 'yes' or end == 'YES':
        break