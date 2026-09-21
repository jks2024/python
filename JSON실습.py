# JSON(JavaScript Object Notation)은 데이터를 저장하고 교환하는 데 널리 사용되는 경량 텍스트 형식입니다.
# - 파이썬에서는 json 기본 라이브러리를 통해 사용 가능
# - 경량 텍스트 포맷
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 API 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용
import json

# 파이썬 객체를 json으로 직렬화
# 도서 정보 (제목, 저자, 출판사, 출간연도, 가격, 장르 2개) => 딕셔너리
# 도서 정보가 여러 개인 리스트 => 리스트

books = [
    {
        "title": "파이썬 코딩 도장",
        "author": "남재윤",
        "publisher": "길벗",
        "year": 2019,
        "price": 30000,
        "genre": ["프로그래밍", "입문서"]
    },
    {
        "title": "클린 코드",
        "author": "로버트 마틴",
        "publisher": "인사이트",
        "year": 2013,
        "price": 33000,
        "genre": ["소프트웨어공학", "베스트프랙티스"]
    },
    {
        "title": "이펙티브 자바",
        "author": "조슈아 블로크",
        "publisher": "인사이트",
        "year": 2018,
        "price": 36000,
        "genre": ["자바", "베스트프랙티스"]
    },
    {
        "title": "모던 자바스크립트 튜토리얼",
        "author": "일리야 카투코프",
        "publisher": "얼추",
        "year": 2020,
        "price": 28000,
        "genre": ["자바스크립트", "입문서"]
    },
    {
        "title": "혼자 공부하는 자바스크립트",
        "author": "윤인성",
        "publisher": "한빛미디어",
        "year": 2021,
        "price": 22000,
        "genre": ["자바스크립트", "입문서"]
    }
]

# Python 객체를 JSON으로 직렬화
json_str = json.dumps(books, ensure_ascii=False, indent=4)
print(json_str)

# JSON을 -> Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print("----------------------------------")
for e in obj:
    print(e)
print("----------------------------------")

# 특정 필드만 뽑아서 출력해보기 (실습 포인트 추가)
for book in obj:
    print(f"{book['title']} ({book['year']}) - {book['price']:,}원")
print("----------------------------------")

# 파일로 저장 하기
# with는 파일을 자동으로 닫아 줌
with open('books.json', 'w', encoding='utf-8') as json_file:
    json.dump(books, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('books.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)