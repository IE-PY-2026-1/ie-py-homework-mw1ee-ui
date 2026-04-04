# [2차 과제] 컨버터 설계 및 등급 판정
print("========== ⚡ 컨버터 설계 시스템 V2.0 ⚡ ==========")

# 1. 입력 받기
name = input("컨버터 명칭: ")
vin = float(input("입력 전압(Vin): "))
vout = float(input("출력 전압(Vout): "))
l_uH = float(input("인덕턴스(L) [uH]: "))
fs = int(input("주파수(fs) [Hz]: "))

# 2. 계산 (산술 연산)
duty = vout / vin
ripple = ((vin - vout) * duty) / (l_uH * 1e-6 * fs)

# 3. 등급 판정 (조건문)
if ripple < 0.1:
    grade = "S (최적)"
elif ripple < 0.5:
    grade = "A (안정)"
else:
    grade = "F (재설계 필요)"

# 4. 리스트에 저장 및 출력
design_data = [name, vin, vout, round(duty, 2), round(ripple, 4), grade]
print(f"\n[결과] {design_data[0]}의 설계 등급은 {design_data[5]}입니다.")
# 기존 코드의 마지막 줄 (print...) 아래에 추가
input("\n엔터 키를 누르면 프로그램이 종료됩니다...")
