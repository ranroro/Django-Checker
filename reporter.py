import datetime
import os

def generate(results):
    # 파일명 생성 (예시: result_2026-02-10_1142.md)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    report_filename = f"result_{now}.md"

    # 보고서 작성
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            # 제목
            f.write("\n'''\n")
            f.write("========== 취약점 분석 결과 ==========")
            f.write("'''\n\n")
            f.write(f"- 생성 시각: {now}\n")
            f.write(f"- 총 발견 취약점 수: {len(results)}건\n\n")
            f.wirte("---\n\n")

            # 취약점 없을 경우
            if not results:
                f.write("취약점이 발견되지 않았습니다.\n")
                return report_filename
            
            # 취약점 목록
            for idx, item in enumerate(results, 1):
                vuln, file, line, reason = item

                f.write(f"## {idx}.  {vuln}\n")
                f.write(f"- 파일 경로: `{file}`\n")
                f.write(f"- 라인 번호: {line}\n")


        return report_filename

    except Exception as e:
        print("[reporter error]", e)
        return None