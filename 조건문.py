# 제어문 : 프로그램의 흐름을 제어하는 데 사용
# - 조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행 (if문, 3항연산자)
# - 반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행 (while문, for문)

# num = int(input("정수 입력: "))
#
# # 양수 / 음수 구분 하기
# if num >= 0:
#     print(f"{num}은 양수 입니다.")
# else:
#     print(f"{num}은 음수 입니다.")
#
# # 홀수 / 짝수 구분하기
# if num % 2 == 0:
#     print(f"{num}은 짝수 입니다.")
# else:
#     print(f"{num}은 홀수 입니다.")
#
# # M이면 남성, F면 여성, 그외는 잘 못 입력
# gender = input("성별 입력 (M/F): ").upper()
# if gender == 'M':
#     print("남성 입니다.")
# elif gender == 'F':
#     print("여성 입니다.")
# else:
#     print("성별을 잘 못 입력 하셨습니다.")

# 학생의 이름, 국어, 영어, 수학 성적을 입력 받음
# 각각의 성적이 0 ~ 100 사이가 아니면 성적이 잘 못 입력 되었습니다. 출력 후 종료
# 성적이 정상 입력 되었다면, 총점과 평균 구하기
# 평균이 90점 이상이면 이름과 등급 A
# 평균이 80점 이상이면 이름과 등급 B
# 평균이 70점 이상이면 이름과 등급 C
# 평균이 60점 이상이면 이름과 등급 D
# 나머지는 이름과 등급 F

while True:
    name = input("이름 입력: ")
    kor = int(input("국어 성적 입력: "))
    eng = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))
    if (0 <= kor <= 100) and (0 <= eng <= 100) and (0 <= math <= 100): break
    print("성적이 잘 못 입력 되었습니다.")

# 성적이 정상 입력 되었다면, 총점과 평균 구하기
total = kor + eng + math
avg = total / 3

# 평균에 따른 등급 판정
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"총점: {total}, 평균: {avg:.2f}")
print(f"{name}님의 등급은 {grade} 입니다.")

# 계절을 영문으로 입력 받아 계절에 맞는 문구 출력하기
# spring, summer, fall, autumn, winter 입력 받아서 계절에 맞는 문구 출력
# 단, 비교의 편의 위해 입력 받은 문자열은 대문자로 변환해서 비교하기
# season = input("계절 입력: ").upper()
# if season == "SPRING":
#     print("꽆피는 봄이 왔어요~~")
# elif season == "SUMMER":
#     print("휴가가 있는 여름 입니다.")
# elif season == "FALL" or season == "AUTUMN":
#     print("화창한 가을 입니다^^")
# elif season == "WINTER":
#     print("추운 겨울 입니다.")
# else:
#     print("계절을 잘 못 입력하셨습니다.")
