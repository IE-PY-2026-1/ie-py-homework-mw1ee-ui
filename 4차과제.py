import csv

# 1. 함수 정의 (모듈화)
def get_ripple(vin, vout, l, f):
    d = vout / vin
    r = ((vin - vout) * d) / (l * 1e-6 * f)
    return round(r, 4)

def save_to_file(data_list):
    with open('converter_db.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['이름', 'Vin', 'Vout', '리플'])
        writer.writerows(data_list)

# 2. 메인 로직
history = []
while True:
    cmd = input("\n[1]등록 [2]파일저장 [0]종료: ")
    if cmd == '1':
        n = input("이름: ")
        vi, vo = float(input("Vin: ")), float(input("Vout: "))
        rip = get_ripple(vi, vo, 100, 50000) # 함수 호출
        history.append([n, vi, vo, rip])
        print(f"분석 완료: 리플 {rip}A")
    
    elif cmd == '2':
        save_to_file(history) # 파일 저장 함수 호출
        print("converter_db.csv로 저장되었습니다.")
        
    elif cmd == '0':
        print("작업을 마칩니다.")
        input("엔터를 누르면 창이 닫힙니다...")
        break
