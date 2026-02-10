import datetime
import os

def generate(results):
    # 파일명 생성 (예시: result_2026-02-10_1142.md)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    os.makedirs("reports", exist_ok=True)
    report_filename = os.path.join("reports", f"result_{now}.md")
    
    # 보고서 작성
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            # 제목
            f.write("========== 취약점 분석 결과 ==========\n")
            f.write(f"탐지된 취약점 개수(총): {len(results)}건\n\n")
            f.write("=" * 40 + "\n\n")

            # 취약점 없을 경우
            if not results:
                f.write("취약점이 발견되지 않았습니다.\n")
                return report_filename
            
            # 취약점 목록
            for idx, result in enumerate(results, 1):
                rule_name, recommendation = result

                f.write(f"[{idx}] 취약점 종류: {rule_name}\n")
                f.write(f"- 조치 권고: {recommendation}\n")
                f.write("\n" + "-" * 40 + "\n\n")

                #f.write(f"[{idx}] 취약점 종류: {rule_name}\n")
                #f.write(f"- 파일명: {result['file']}\n")
                #f.write(f"- 라인 번호: {result['line']}\n")
                #f.write("- 코드:\n")
                #f.write("```python\n")
                #f.write(result["code"])
                #f.write("\n```\n")
                #f.write(f"- 조치 권고: {recommendation}\n")
                #f.write("\n" + "-" * 40 + "\n\n")

        print(f"[+] 보고서 생성 완료: {report_filename}")

    except Exception as e:
        print("[reporter error]", e)
        return None