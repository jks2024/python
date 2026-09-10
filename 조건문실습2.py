# [실습문제] 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 10320원
# 야간 근무 : 주간 시급 * 1.5
#
# - 주간근무 [1], 야간근무[2]를 입력 하세요 :
# - 근무 시간을 입력해 주세요 :
# - 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.

work_type = int(input("[1]주간근무 [2]야간근무 를 입력 : "))
work_time = int(input("근무 시간 입력 : "))
HOUR_PAY = 10030  # 코드내에서 변경 불가의 의미로 대문자 사용

if work_type == 1:
    pay = work_time * HOUR_PAY   # 주간 근무에 대한 급여
else:
    pay = work_time * HOUR_PAY * 1.5  # 야간 근무에 대한 급여

print(f"{work_time}시간 동안 근무한 {work_type == 1 and '주간' or '야간'} 급여는 {pay:,.0f}원 입니다.")
