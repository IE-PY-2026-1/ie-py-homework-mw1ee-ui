print("===컨버터 설계 시스템===")

labels = ['명칭', 'vin', 'vout', 'L[uH]', 'fs[Hz]']
data = []
for L in labels:
    v = input(L + '입력: ')
    if L == '명칭':
        data.append(v)
    else:
        data.append(float(v))

nm, vi, vo, Lu, fs = data[0], data[1], data[2], data[3], data[4]
duty = vo / vi
ripple = ((vi - v0) * duty) / (Lu * 1e-6 * fs)

if ripple < 0.1:
    grade = "S(최적)"
    if duty > 0.5 and ripple < 0.05:
        grade = "S+(전설)"
elif ripple < 0.5:
    grade = "A(안정)"
else:
    grade = "F(재설계)"

res = [nm, round(duty, 2), round(ripple, 4), grade]
res.insert(1, "Buck")

for i in range(1):
    if vi <= vo:
        break
    continue

print(f"\n[결과] {res[0]} 등급: {res[-1]} (데이터:{len(res)}개)")
print(f"상세결과 -> 모델: {res[1]}, Duty: {res[2]}, Ripple: {res[3]}")
input("\n엔터를 누르면 종료됩니다...")
