# [3차 과제] 다중 설계 관리 시스템
design_history = []  # 여러 데이터를 담을 주머니

while True:
    print("\n1. 설계 등록  2. 목록 보기  0. 종료")
    menu = input("메뉴 선택: ")

    if menu == '1':
        name = input("명칭: ")
        vin = float(input("Vin: "))
        vout = float(input("Vout: "))
        # ... (계산 로직 동일) ...
        duty = vout / vin
        ripple = ((vin - vout) * duty) / (100 * 1e-6 * 50000) # 예시값 계산
        
        # 리스트에 추가 (누적)
        design_history.append([name, vin, vout, duty, ripple])
        print("저장되었습니다.")

    elif menu == '2':
        print("\n--- 전체 설계 목록 ---")
        for data in design_history:
            print(f"이름: {data[0]}, 듀티: {data[3]}, 리플: {data[4]}")

    elif menu == '0':
        print("프로그램을 종료합니다.")
        input("엔터를 누르면 창이 닫힙니다...")
        break
