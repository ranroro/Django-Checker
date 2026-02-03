import os
import sys

try:
    import scanner
    import rules
    import reporter

def print_banner():
    banner = """
    ============================
           Django-Checker
      ★swuforce web-project★
    ============================
    """
    print(banner)

def main():
    print_banner()

    # 대상 폴더 입력받기
    path = input("장고 루트 폴더의 로컬 주소를 입력하세요 : ").strip() #혹시 공백 넣어서 입력하면 공백 없애려고 strip씀

    # 유효성 검사
    if not os.path.isdir(path):
        print(f"[오류]'{path}'은(는) 유효한 디렉터리 경로가 아닙니다. 다시 입력해주세요.")
        return
    
    try:
        # 규칙 불러오기 
        detection_rules = rules.get_rules()
        # 스캐너 실행
        print(f"\n[*]'{path} 분석을 시작합니다...")
        scan_results = scanner.start_scan(path, detection_rules)
        
        # 리포터 실행
        if scan_results:
            print(f"분석 완료. {len(scan_results)}개의 취약점 흔적을 발견했습니다.")
            reporter.generate(scan_results) # 결과 리스트를 리포터에 전달
            print("보고서 생성이 완료되었습니다.")
        else:
            print("탐지된 취약점이 없습니다.")

    # 오류 발생시 출력
    except Exception as e:
        print(f"\n[실행 오류] : {e}")


# 파일 실행될 때만 main() 호출
## 파이썬은 import를 한 번씩 다 실행해서 테스트용 파일을 호출해올수도 있다네요
if __name__ == "__main__":
    main()