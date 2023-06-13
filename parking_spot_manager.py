"""
무료주차장의 데이터를 분석하고 관리하기 위한 모듈
"""

class parking_spot:
    """
    parking_spot class는 [순번]을 제외한 [자원명], [시도], [시군구], [주차장유형], [경도], [위도] 6개 데이터를 
    저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가능한 __item이 있으며,
    해당 변수를 접근하기 위해 get 메소드를 제공합니다.
    """
    __item={'name': '', 
            'city': '', 
            'district': '', 
            'ptype': '', 
            'longitude': 0, 
            'latitude': 0}
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item ={'name': name, 
                      'city': city, 
                      'district': district, 
                      'ptype': ptype, 
                      'longitude': longitude, 
                      'latitude': latitude}
        
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        '''
        __item[keyword]를 반환하는 함수
        Args:
        keyword (string): 얻고자하는 __item의 인덱스값
        인자를 쓰지 않으면 자동으로 __item[name]값을 반환
        '''
        return self.__item[keyword]
    
def str_list_to_class_list(str_list):
    '''
    문자열 리스트[str_list]를 매개변수로 받아,
    parking_spot 클래스 객체의 리스트로 변환한 후 그 리스트를 반환하는 함수
    Args:
    str_list (list): [순번], [자원명], [시도], [시군구], [주차장유형], [경도], [위도]로 표현되는 문장들을 원소로 하는 리스트
    '''
    class_list = []
    
    for item in str_list:
        num, name, city, district, ptype, longitude, latitude = item.split(',')
        spot = parking_spot(name, city, district, ptype, float(longitude), float(latitude))
        class_list.append(spot)

    return class_list

def print_spots(spots):
    """
    parking_spot 클래스 객체의 리스트[spots]를 매개변수로 받아
    "---print elements([리스트의 길이])---"를 출력 후 
    리스트에 저장된 모든 객체의 값을 출력하는 함수
    Args:
    spots  (list): 출력하고자 하는 parking_spot 클래스 객체의 리스트
    """
    print(f"---print elements({len(spots)})---")
    
    for spot in spots:
        print(spot)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)