import requests
res = requests.get("http://naver.com")
res.raise_for_status()

# if res2.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 발생했습니다. [ErrorCode :", res2.status_code, "]")

# res.raise_for_status()
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
# print(res.text)

with open("mynaver.html", "w", encoding="utf=8") as f:
    f.write(res.text)