# 3개의 햄버거와 2개의 음료의 가격을 입력 받아 제일 싼 세트 메뉴의 가격 구하기(50원 할인)
# - 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료둘 중 싼 음료의 가격을 합산하고 여기서 50원 할인
# 한개의 리스트로 구현
# prices = list(map(int, input("햄버거 3개, 음료 2개 연속 입력: ").split()))
# burgers = prices[:3]
# drinks = prices[3:]
#
# choice_burger = min(burgers)
# choice_drink = min(drinks)
#
# print(f"세트 메뉴 가격: {choice_burger + choice_drink - 50}")

# 리스트 순회 하기 : 5대의 자동차 이름을 입력 받음
# - 범위기반 for문으로 순회해서 출력: for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# - 오름차순, 내림차순 출력

cars = list(input("자동차 이름: ").split())
for i in range(len(cars)):
    print(f"{cars[i]}", end=" ")
print()

for e in cars:
    print(f"{e}", end=" ")
print()

print(f"{sorted(cars)}")
print(f"{sorted(cars, reverse=True)}")