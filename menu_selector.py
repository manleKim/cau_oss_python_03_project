"""
사용자와 상호작용하기 위한 UI(User Interface)를 제공하는 모듈
"""

import file_manager
import parking_spot_manager

def start_process(path):
    """
    파일의 경로[path]를 매개변수로 받아, 
    file_manager 모듈의 read_file 함수를 호출하여 문자열 리스트를 반환받고, 
    다시 이 문자열 리스트를 이용, parking_spot_manager 모듈의 str_list_to_class_list 함수로 parking_spot 객체의 리스트를 반환받은 후,
    select 값에 따라 다양한 process를 시행하는 함수
    
    select == 1: print_spot 함수를 호출한다.
    select == 2: filter 기능. 본인이 필터하고 싶은 항목에 따라 번호를 입력.
                fitering하고 싶은 단어를 입력하면 filter된 데이터들을 출력한다.
    select == 3: 필터를 할 기준의 키[keyword]를 문자열로 입력.
                keyword가 지원하는 목록에 없다면 "invalid input"을 출력하며, 지원하는 경우 parking_spot_manager 모듈의
                sort_by_keyword 함수를 호출하여 정렬된 데이터들을 출력한다.
    select == 4: "Exit"을 출력하고 menu 선택 반복을 종료한다.
    
    Args:
    path (string): input 파일의 경로
    """
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)
            
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1: # fiter_by_name
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)

            elif select == 2: # fiter_by_city
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)

            elif select == 3: # fiter_by_district
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)

            elif select == 4: # fiter_by_ptype
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)

            elif select == 5: # fiter_by_locations
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)

            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots =  parking_spot_manager.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")
            