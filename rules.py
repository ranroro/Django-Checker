import re

def get_rules():
<<<<<<< Updated upstream
    #전에 정한대로 리스트로 관리
    return[]
    """
    [취약점 항목명, 정규표현식(Pattern), 조치 권고]
    """
    return [
        # 1. SQL Injection
        [
            "SQL Injection", 
            r"cursor\.execute\(f[\"'].*\{.*\}[\"']\)", 
            "f-string 대신 'cursor.execute(sql, [param])' 형태의 매개변수화 쿼리를 사용하세요."
        ],
        
        # 2. XSS 
        [
            "XSS", 
            r"\.replace\(.*<script>.*\)|\|safe", 
            "|safe 필터 사용을 중단하고, 블랙리스트 방식의 replace 대신 장고 기본 이스케이프를 사용하세요."
        ],
        
        # 3. File Upload 
        [
            "File upload", 
            r"\{\{.*\.read\.decode\s*\}\}|request\.FILES\.get", 
            "파일 확장자 화이트리스트 검증을 추가하고, 파일 내용을 직접 브라우저에 렌더링하지 마세요."
        ],
        
        # 4. CSRF
        [
            "CSRF", 
            r"@csrf_exempt|['\"]#.*CsrfViewMiddleware['\"]", 
            "보안 미들웨어를 활성화하고, 특정 뷰에서 CSRF 면제 데코레이터를 제거하세요."
        ]
    ]
>>>>>>> Stashed changes
