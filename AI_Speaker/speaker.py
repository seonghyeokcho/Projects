import time
import os
import sys

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from utils.daily_info_scraping import scrape_weather, scrape_it_news,\
    scrape_headline_news, scrape_daily_english_conversation

# 음성 인식(STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio_data=audio, language="ko")
        print("[USER] : " + text)  # 사용자가 말한 내용 출력
        answer(text)  # 사용자가 말한 내용 분석
    except sr.UnknownValueError:
        print("인식 실패")  # 음성 인식을 실패한 경우
    except sr.RequestError as e:
        print(f"요청 실패 : {e}")  # API Key 오류 혹은 네트워크 단절 등

# 대답
def answer(input_text):
    answer_text = ""
    if "안녕" in input_text:
        answer_text = "안녕하세요? 반갑습니다!"
    elif "날씨" in input_text:
        # answer_text = scrape_weather()
        answer_text = "오늘의 서울 기온은 20도입니다. 맑은 하늘이 예상됩니다."
    elif "환율" in input_text:
        answer_text = "원 달러 환율은 1380원 입니다."
    elif "고마워" in input_text:
        answer_text = "별 말씀을요."
    elif "종료" in input_text:
        answer_text = "다음에 또 만나요"
        stop_listening(wait_for_stop=False)  # 이 함수를 호출하면 컴퓨터가 더 이상 듣지 않음
    else:
        answer_text = "메뉴얼에 없는 명령이에요. 다시 한번 말씀해주시겠어요?"

    speak(answer_text)

# 말하기(TTS)
def speak(text):
    print("[JARVIS] : " + text)  # AI가 말한 내용 출력
    file_name = "voice.mp3"
    tts = gTTS(text=text, lang="ko")
    tts.save(file_name)  # mp3 파일로 저장
    playsound(file_name)  # mp3 파일 재생
    if os.path.exists(file_name):  # voice.mp3 파일 삭제
        os.remove(file_name)

# 인식기, 마이크 객체 생성
r = sr.Recognizer()
m = sr.Microphone()

speak("무엇을 도와드릴까요?")
stop_listening = r.listen_in_background(source=m, callback=listen)

while True:
    time.sleep(0.1)