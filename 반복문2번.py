# for 문 : 정해진 범위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값):


# ive = ["안유진", "장원영", "이서", "가을", "레이", "리즈"]
# for e in ive:  # 시퀀스형 데이터를 자동으로 반복 수행 하면서 요소의 값을 복사 하면서 수행
#     print(e, end=" ")
#
# print()
#
# for i in range(0, len(ive), 2):
#     print(ive[i], end= " ")
#
# print()
#
# for i in range(len(ive) - 1, 0 - 1, -1):
#     print(ive[i], end= " ")
#
# print()

# 1 ~ 1000사이의 3의 배수 출력하기
# cnt = 0
# for i in range(1, 100 + 1):
#     if i % 3 == 0:
#         print(f"{i:3}", end=" ")
#         cnt += 1
#         if cnt >= 10:
#             print()
#             cnt = 0


# 입력 받은 수의 범위 내의 7의 배수를 출력.
# 한줄에 10개씩 출력
# 정렬{n:5}을 적용해 줄 맞추가
# cnt = 0
# num = int(input("정수 입력: "))
# for i in range(1, num + 1):
#     if i % 7 == 0:
#         print(f"{i:3}", end=" ")
#         cnt += 1
#         if cnt >= 10:  # 출력 개수가 10개 이거나 이상인 경우 줄바꿈
#             print()
#             cnt = 0


# 입력 받은 문자열을 뒤집어 출력 하기
# 입력: abcdef => fedcba
# text = input("\n문자 입력: ")
# for i in range(len(text) - 1, -1, -1):
#     print(text[i], end=" ")
# print()

# 입력 받은 문자열에서 대문자는 소문자로, 소문자는 대문자로 변경해서 출력하기

# new_text = ""
# for e in text:
#     if e.isupper():
#         new_text += e.lower()
#     elif e.islower():
#         new_text += e.upper()
#     else:
#         new_text += e
#
# print(new_text)

# 정수값을 입력 받아 3의 배수, 5의 배수이면 값을 출력, 한줄에 5개
# cnt = 0
# num = int(input("정수 입력: "))
# for e in num:
#     if e % 3 == 0 or e % 5 == 0:
#         print(e, end=" ")
#         cnt += 1
#         if cnt == 5:
#             print()
#             cnt = 0

# 이중 for문
# 입력 받은 수가 10이라면 10 * 10의 행렬 출력
num = int(input("정수 입력: "))
for i in range(1, num + 1):  # 1 ~ num
    for j in range(1, num + 1):
        print("*", end=" ")
    print()



