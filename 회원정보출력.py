# 회원정보를 입력 받아서 출력 하는 예제 진행
#
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다. (남성과 여성으로 출력)
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

name = input("이름을 입력 하세요 : ")
while True:
    age = input("나이를 입력하세요 : ")
    if age.isdigit():  # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
        age = int(age)
        if 0 < age < 200:
            break
    print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")

while True:
    gender = input("성별을 입력 하세요 : ").lower()
    if gender == "m" or gender == "f": break
    print("성별을 잘 못 입력 하셨습니다.")

while True:
    jobs = input("직업을 입력 하세요 : ")
    if jobs.isdigit():
        jobs = int(jobs)
        if 0 < jobs < 5: break
    print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

if gender == 'm':
    gen_name = "남성"
else:
    gen_name = "여성"

jobs_name = ("", "학생", "회사원", "주부", "무직")  # 튜플 사용

print("=" * 3, "회원정보", "=" * 3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[jobs]}")


# 짝수/홀수 개수 세기
# 정수를 하나씩 계속 입력받다가, -1이 입력되면 반복을 종료합니다. 그동안 입력받은 숫자 중 짝수의 개수와 홀수의 개수를 각각 출력하세요.
# while과 break 사용
even_cnt = 0
odd_cnt = 0
while True:
    n = int(input("정수 입력 (-1 종료): "))
    if n == -1:
        break
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print(f"짝수 개수: {even_cnt}")
print(f"홀수 개수: {odd_cnt}")


# 구구단 중 특정 단만 출력하기
# 2~9 사이의 정수를 입력하세요: 3
while True:
    dan = int(input("2 ~ 9 사이의 정수 입력: "))
    if 2 <= dan <= 9:
        break
    print("잘못된 입력 입니다.")

for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")





