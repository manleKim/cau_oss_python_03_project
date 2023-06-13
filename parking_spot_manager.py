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
        
def filter_by_name(spots, name):
    """
    클래스 parking_spot의 객체 리스트 [spots]와 문자열 [name]을 매개변수로 받아
    자원명(name)가 일치하는 객체들로 이루어진 새로운 리스트를 반환하는 함수입니다.
    Args:
        spots (list): 필터링할 parking_spot 클래스 객체 리스트
        name (string): 필터링할 자원명
    Returns:
        spots_filtered (list): 자원명이 일치하는 parking_spot 클래스 객체로 이루어진 새로운 리스트
    """
    spots_filtered = [spot for spot in spots if spot.get('name').find(name) != -1]
    
    return spots_filtered
    

def filter_by_city(spots, city):
    """
    클래스 parking_spot의 객체 리스트 [spots]와 문자열 [city]을 매개변수로 받아
    시도(city)가 일치하는 객체들로 이루어진 새로운 리스트를 반환하는 함수입니다.
    Args:
        spots (list): 필터링할 parking_spot 클래스 객체 리스트
        city (string): 필터링할 시도
    Returns:
        spots_filtered (list): 시도가 일치하는 parking_spot 클래스 객체로 이루어진 새로운 리스트
    """
    spots_filtered = [spot for spot in spots if spot.get('city').find(city) != -1]
    
    return spots_filtered

def filter_by_district(spots, district):
    """
    클래스 parking_spot의 객체 리스트 [spots]와 문자열 [district]을 매개변수로 받아
    시군구(district)가 일치하는 객체들로 이루어진 새로운 리스트를 반환하는 함수입니다.
    Args:
        spots (list): 필터링할 parking_spot 클래스 객체 리스트
        district (string): 필터링할 시군구
    Returns:
        spots_filtered (list): 시군구가 일치하는 parking_spot 클래스 객체로 이루어진 새로운 리스트
    """
    spots_filtered = [spot for spot in spots if spot.get('district').find(district) != -1]
    
    return spots_filtered

def filter_by_ptype(spots, ptype):
    """
    클래스 parking_spot의 객체 리스트 [spots]와 문자열 [ptype]을 매개변수로 받아
    주차장유형(ptype)가 일치하는 객체들로 이루어진 새로운 리스트를 반환하는 함수입니다.
    Args:
        spots (list): 필터링할 parking_spot 클래스 객체 리스트
        ptype (string): 필터링할 주차장유형
    Returns:
        spots_filtered (list): 주차장유형이 일치하는 parking_spot 클래스 객체로 이루어진 새로운 리스트
    """
    spots_filtered = [spot for spot in spots if spot.get('ptype').find(ptype) != -1]
    
    return spots_filtered

def filter_by_location(spots, locations):
    """
    클래스 parking_spot의 객체 리스트 [spots]와 위치 정보를 담은 튜플 [locations]를 매개변수로 받아
    최소위도(min_lat)보다 크고, 최대위도(max_lat)보다 작으며, 최소경도(min_lon)보다 크고, 최대경도(max_lon)보다 작은 범위 내에 있는
    객체들로 이루어진 새로운 리스트를 반환하는 함수입니다.
    
    Args:
        spots (list): 필터링할 parking_spot 클래스 객체 리스트
        locations (tuple): 최소 위도, 최대 위도, 최소 경도, 최대 경도를 담은 튜플
    Returns:
        spots_filtered (list): 위 설명과 같은 범위 내에 있는 parking_spot 클래스 객체로 이루어진 새로운 리스트
    """
    min_lat, max_lat, min_lon, max_lon = locations
    spots_filtered = [spot for spot in spots if min_lat <= spot.get('latitude') and max_lat >= spot.get('latitude') and min_lon <= spot.get('longitude') and max_lon >= spot.get('longitude')]
    
    return spots_filtered

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