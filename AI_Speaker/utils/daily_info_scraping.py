########## 20년도 8월 ##########
# import requests
# from bs4 import BeautifulSoup as bs4
# import re

# def create_soup(url):
#     headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = bs4(res.text, "lxml")
#     return soup

# def print_news(index, title, link):
#     print("{}. {}".format(index + 1, title))
#     print("  (링크 : {})".format(link))

# def scrape_weather():
#     print("[오늘의 날씨]", "\n")
#     url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&tqi=U1ZSKdp0J1sssTXyQZwssssssxC-127613"
#     soup = create_soup(url)
#     # 오늘 날씨 요약 정보
#     cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
#     # 현재 기온(최저, 최고 기온)
#     curr_temp = soup.find("p", attrs={'class':"info_temperature"}).get_text().replace("도씨", "")
#     min_temp = soup.find("span", attrs={"class":"min"}).get_text()  # 최저 기온
#     max_temp = soup.find("span", attrs={"class":"max"}).get_text()  # 최고 기온
#     # 오전 / 오후 강수확률
#     morning_rain_rate = soup.find("span", attrs={"class",'point_time morning'}).get_text().strip()  # 오전 강수확률
#     afternoon_rain_rate = soup.find("span", attrs={"class",'point_time afternoon'}).get_text().strip()  # 오후 강수확률
#     # 미세먼지 정보
#     dust = soup.find("dl", attrs={"class":"indicator"})
#     pm10 = dust.find_all("dd")[0].get_text()
#     pm25 = dust.find_all("dd")[1].get_text()

#     # 출력
#     print(cast)
#     print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
#     print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate), "\n")
#     print("미세먼지 {}".format(pm10))
#     print("초미세먼지 {}".format(pm25), "\n")

# def scrape_headline_news():
#     print("[헤드라인 뉴스]", "\n")
#     url = "https://news.naver.com"
#     soup = create_soup(url)
#     news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)  # limit = n : 찾은 모든 것들 중 n개만 가져와라
#     for idx, news in enumerate(news_list):
#         title = news.find("a").get_text().strip()
#         link = url + news.find("a")['href']
#         # 출력
#         print_news(idx, title, link)
#     print()

# def scrape_it_news():
#     print("[IT 뉴스]", "\n")
#     url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
#     soup = create_soup(url)
#     news_list = soup.find("ul", attrs={"class":"cluster_list"}).find_all("li", limit=3)  # 3개 까지만
#     for idx, news in enumerate(news_list):
#         a_idx = 0
#         img = news.find("img")
#         if img:
#             a_idx = 1  # img 태그가 있으면 1번쨰 img 태그의 정보를 사용

#         a_tag = news.find_all("a")[a_idx]
#         title = a_tag.get_text().strip()
#         link = a_tag['href']
#         # 출력
#         print_news(idx, title, link)
#     print()

# def scrape_english():
#     print("[오늘의 영어 회화]", "\n")
#     url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
#     soup = create_soup(url)
#     sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
#     print("(영어 지문)")
#     for sentence in sentences[len(sentences)//2:]:  # 8문장이 있다고 가정할 때, 4~7 까지 잘라서 가져옴
#         print(sentence.get_text().strip())
    
#     print()

#     print("(한글 지문)")
#     for sentence in sentences[:len(sentences)//2]:  # 8문장이 있다고 가정할 때, 0~3 까지 잘라서 가져옴
#         print(sentence.get_text().strip())

#     print()


# if __name__ == "__main__":
#     scrape_weather()  # 오늘의 날씨 정보 가져오기
#     scrape_headline_news()  # 헤드라인 뉴스 정보 가져오기
#     scrape_it_news()  # IT 뉴스 정보 가져오기
#     scrape_english()  # 오늘의 영어 회화 가져오기

########## 21년도 10월 ##########
import re
import requests

from bs4 import BeautifulSoup as bs4

def create_bs4(url):  # BeautifulSoup 객체 생성 함수
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = bs4(res.text, "lxml")
    return soup

def print_news(idx, title, link):  # 뉴스 출력 함수
    print(f"{idx}. {title}")
    print(f"링크 : {link}")

def scrape_weather():
    print("[오늘의 날씨]", "\n")
    url = "https://weather.naver.com/today/09140104"
    soup = create_bs4(url)
    # 오늘의 날씨 요약 정보
    cast = soup.find("p", attrs={"class":"summary"}).get_text().strip()[:-2]
    state = soup.find("span", attrs={"class":"weather before_slash"}).get_text()
    sensible = soup.find_all("dd", attrs={"class":"desc"})[2].get_text()
    # 현재 기온(최저, 최고 기온)
    curr_temp = soup.find("strong", attrs={"class":"current"}).get_text()[5:]  # 현재 온도xx or x
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()[4:]  # 최저기온xx or x
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()[4:]  # 최고기온xx or x
    # 오전 / 오후 강수확률
    morning_rain_rate = soup.find_all("span", attrs={"class":"rainfall"})[0].get_text()
    afternoon_rain_rate = soup.find_all("span", attrs={"class":"rainfall"})[1].get_text()
    # 미세먼지 정보
    url = "https://weather.naver.com/air/09140104"
    soup = create_bs4(url)
    dust = soup.find_all("span", attrs={"class":re.compile("^_cnPm")})
    pm10 = dust[0].get_text()
    pm10_state = dust[1].get_text()
    pm25 = dust[2].get_text()
    pm25_state = dust[3].get_text()
    # 날씨 출력
    print(cast, "/", state)
    print(f"현재 {curr_temp} / 체감 {sensible} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 {morning_rain_rate} / 오후 {afternoon_rain_rate}")
    print(f"미세먼지 {pm10}({pm10_state}) / 초미세먼지 {pm25}({pm25_state})", "\n")

def scrape_headline_news():
    print("[헤드라인 뉴스]", "\n")
    url = "https://news.naver.com/"
    soup = create_bs4(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)  # 맨 위부터 3개까지만
    # find_all("element", limit=n) -> 해당 element 를 모두 찾는데 n개까지 찾아라
    for idx, news in enumerate(news_list):  # 가져온 뉴스들을 각각 번호,제목,링크를 함께 출력
        title = news.a.get_text().strip()
        link = "https://news.naver.com" + news.a['href']
        # 뉴스 출력
        print_news(idx+1, title, link)
    print()  # 컨텐츠 사이의 줄바꿈

def scrape_it_news():
    print("[IT 뉴스]", "\n")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_bs4(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)  # 맨 위부터 3개까지만
    for idx, news in enumerate(news_list):  # 가져온 뉴스들을 각각 번호,제목,링크를 함께 출력
        a_idx = 0
        img = news.find("img")
        if img:  # 만약 img 태그가 있으면 2번째 a 태그의 정보를 사용
            a_idx = 1
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        # 뉴스 출력
        print_news(idx+1, title, link)
    print()  # 컨텐츠 사이의 줄바꿈

def scrape_daily_english_conversation():
    print("[오늘의 영어 회화]", "\n")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_bs4(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    # 영어 회화 지문 출력
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()  # 영어 지문과 한글 지문 사이의 줄바꿈
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

# if __name__ == "__main__":
#     scrape_weather()  # 오늘의 날씨 가져오기
#     scrape_headline_news()  # 헤드라인 뉴스 3개 가져오기
#     scrape_it_news()  # IT 뉴스 3개 가져오기
#     scrape_daily_english_conversation()  # 오늘의 영어 회화 지문 가져오기