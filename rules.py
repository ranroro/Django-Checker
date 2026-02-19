import re

def get_rules():
    py_cmt = chr(35) 
    html_cmt = "<" + "!--"
    # 줄 시작부분에 주석이 없는지 확인하는 필터 (f-string 사용)
    prefix = rf"^(?!\s*(?:{py_cmt}|{html_cmt}))"

    """
    [취약점 항목명, 정규표현식(Pattern), 조치 권고]
    """
    return [
        # 1. SQL Injection
        [
            "SQL Injection",
            prefix + r".*?(?:\b\w+\.execute\(\s*f['\"][\s\S]*?\{[\s\S]*?\}[\s\S]*?['\"][\s\S]*?\))",
            "f-string 대신 'cursor.execute(sql, [param])' 형태의 매개변수화 쿼리를 사용하세요."
        ],
        
        # 2. XSS 
        [
            "XSS", 
            prefix + r".*?(?:(\|\s*safe\b)|(<\s*script(?![^>]*\bsrc\s*=)\b)|(\.replace\(.*<script>.*\)))",
            "|safe 필터 사용을 중단하고, <script> 태그 직접 삽입이나 단순 치환(replace) 대신 장고의 기본 이스케이프 기능을 사용하세요."
        ],
        
        # 3. File Upload
        [
            "File upload", 
            prefix + r".*?(?:request\.FILES\.(get|getlist)\b|read(?:\(\))?\s*\.\s*decode(?:\(\))?)",
            "파일 확장자 검증을 도입하고, 파일 내용을 템플릿에 직접 노출하지 마세요."
        ],

        # 4. CSRF & Security Settings
        [
            "CSRF", 
            prefix + rf".*?(?:@csrf_exempt\b|{py_cmt}.*CsrfViewMiddleware|DEBUG\s*=\s*True|ALLOWED_HOSTS\s*=\s*\[['\"]\*['\"]\])",
            "보안 미들웨어를 활성화하고, 배포 시 DEBUG와 ALLOWED_HOSTS 설정을 점검하세요."
        ]
    ]

