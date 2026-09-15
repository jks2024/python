# 기본 메뉴 추가
# {} 중괄호를 사용해 선언, 각 요소는 ,(쉼표)로 구분
# 키와 값은 :(콜론)으로 구분
# 딕셔너리 내부에 리스트를 가짐.
menu = {
    "americano": ["coffee", 2000, "기본 커피 입니다."],
    "espresso": ["coffee", 2500, "진한 커피 입니다."],
    "latte": ["coffee", 4000, "우유가 들어 있는 커피"],
    "green tea": ["tea", 4500, "녹차 입니다"],
    "black tea": ["tea", 4500, "홍차 입니다."]
}

# 전제 메뉴 조회
def print_menu():
    for e in menu:
        print(f"{e} - {menu[e]}")

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(menu[name])
    else:
        print("찾는 메뉴가 없습니다.")

# 메뉴 추가
def add_menu(name, category, price, desc): # 메뉴의 정보를 매개변수로 전달 받음
    if name not in menu: # 딕셔너리에 해당 메뉴가 없으면 추가
        menu[name] = [category, price, desc] # 키를 생성하고, 값을 추가(값이 리스트 임)
        print(f"{name} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재 합니다.")

# 메뉴 삭제
def del_menu(name):  # 함수의 매개변수로 키값을 전달 받아 해당 메뉴를 삭제
    if name in menu: # 삭제할 메뉴가 메뉴 딕셔너리에 존재하는지 확인
        del menu[name]  # del 키워드를 사용해 키에 해당하는 메뉴 삭제
        print(f"{name} 메뉴가 삭제 되었습니다.")
    else:
        print("삭제할 메뉴가 없습니다.")


# 메뉴 수정
def modify_menu(name, category, price, desc):
    if name in menu:
        menu[name] = [category, price, desc]
        print("메뉴 정보가 수정 되었습니다.")
    else:
        print("수정할 메뉴가 없습니다.")


# 전체 메뉴 만들기
# [1]전체 메뉴 보기 [2]개별 메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]메뉴 수정 [6]종료 하기
while True:
    print("메뉴를 선택 하세요: ")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]종료 : "))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input("조회할 메뉴 이름 입력: ")
        get_menu(name)
    elif choice == 3:
        name = input("추가할 메뉴 입력 : ")
        category = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        add_menu(name, category, price, desc)
    elif choice == 4:
        name = input("삭제할 메뉴 입력 : ")
        del_menu(name)
    elif choice == 5:
        name = input("수정할 메뉴 입력 : ")
        category = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        modify_menu(name, category, price, desc)
    elif choice == 6:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못된 메뉴 선택 입니다.")