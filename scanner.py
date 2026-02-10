import os
import re

try:
    import main



    ##폴더 탐색해서 분석할 파일을 리스트로 만든 후 반환
    def find_files(root_path):

        #결과값으로 리턴할 리스트생성
        file_list = []

        #os.walk를 사용해서 폴더 내부 구조를 탐색
        #rules.py 적용 X -> 나중에 수정 해야 됨.
        for (path, dir, files) in os.walk(root_path):

            #파일 이름이 .py로 끝나는지 검사
            #맞으면 리스트에 저장.
            for file in files: 
                if file.endswith(".py") or file.endswith(".html"):

                    #dir은 read_file_data에서 안 써서 저장 X
                    file_list.append([path, file])

        return file_list
    

                    


    ##위의 함수에서 반환받은 리스트를 돌면서 파일을 하나씩 탐색
    def read_file_code(file_list, detection_rules):

        #리턴할 취약점을 담은 리스트
        #형식은 [취약점, 파일 이름, 자세한 위치, 이유]
        list_data = []

        
        for (path, file) in file_list:
            #경로와 파일 이름 합치기
            #나중에 괜찮다면 [path, file]를 저장하지 말고, full_path를 저장하는 것도 괜찮을 듯.
            full_path = os.path.join(path, file)

            #with open쓰면 마지막에 안 닫아도(close()) 된다고해서 이걸로 썼습니다.
            with open(full_path, 'r', encoding="utf-8") as f:
                
                #한 줄씩 보고 규칙에 맞는 게 있는지 확인.
                #규칙 적용 X 나중에 해야 함.
                for (line_number, line) in enumerate(f, 1):

                    #공백/줄바꿈 문자 제거
                    clean_line = line.rstrip()

                


                    #sql Injection
                    if re.search(detection_rules[0][1], clean_line):
                        list_data.append([detection_rules[0][0], detection_rules[0][2]])

                    #stored XSS
                    elif re.search(detection_rules[1][1], clean_line):
                        list_data.append([detection_rules[1][0], detection_rules[1][2]])

                    #파일 업로드 취약점
                    elif re.search(detection_rules[2][1], clean_line):
                        list_data.append([detection_rules[2][0], detection_rules[2][2]])
                    
                    #csrf
                    elif re.search(detection_rules[3][1], clean_line):
                        list_data.append([detection_rules[3][0], detection_rules[3][2]])


        
        return list_data





    #위에 두 함수를 돌리고, 값을 반환할 함수
    ## main에서 여기를 실행시킴
    def start_scan(path, detection_rules):

        #main에서 받은 path를 가지고 탐색할 파일 찾는 함수 실행
        file_list = find_files(path)

        #find_files에서 받은 file_list를 가지고 취약점 스캔
        weak_point = read_file_code(file_list, detection_rules)

        return weak_point



except Exception as e:
    print("[scanner error] :", e) 
