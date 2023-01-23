import re

p = re.compile("ca.e")
# . : 하나의 문자를 의미 > (ca.e) care, cafe, case..
# ^ : 문자열의 시작 > (^de) desk, destination...
# $ : 문자열의 끝 > (se$) case, base...

def print_match(m):
    if m:
        print("m.group():", m.group()) # group: 일치하는 문자열 부분 반환
        print("m.string:", m.string) # string: 입력받은 문자열 모두 반환
        print("m.start():", m.start()) # start: 일치하는 문자열의 시작 index
        print("m.end()", m.end()) # end: 일치하는 문자열의 끝 index
        print("m.span()", m.span()) # span: 일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

m = p.search("careless") # search: 주어진 문자열 중 정규식에 부합하는 부분이 있는지 확인
print_match(m)

lst = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)