import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a 엘리먼트를 반환
# print(soup.a.attrs) # a 엘리먼트의 어트리뷰트(속성) 정보를 반환
# print(soup.a["href"]) # a 엘리먼트의 href 속성의 value를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class = "Nbtn_upload"인 a의 엘리먼트를 탐색
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 엘리먼트를 탐색

# print(soup.find("li", attrs={"class":"rank01"}))
rank1=soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text()) # "태그명.자식태그명" 을 통해 해당 태그의 자식태그로 바로 이동할 수 있다.
# # print(rank1.next_sibling.get_text()) # next_sibling을 사용하면 동렬에 있는 다음 태그로 넘어갈 수 있다.
# print(rank1.next_sibling.next_sibling.get_text()) # 하지만 태그 사이에 줄바꿈이 있는 경우 next_sibling을 두번 적용해야 한다.
# print(rank1.find_next_sibling("li")) # find_next_sibling("태그명")은 동렬 태그 중 해당 조건을 만족하는 태그로 바로 이동한다.
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.previous_sibling.previous_sibling.get_text())
# print(rank1.parent)

# rank2=rank1.find_next_sibling("li")
# print(rank2.find_previous_sibling("li").get_text()) # previous_sibling에도 find 적용 가능!

print(rank1.find_next_siblings("li"))