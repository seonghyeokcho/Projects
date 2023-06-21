# TTS(Text To Speech)
# STT(Speech To Text)
from gtts import gTTS
from playsound import playsound

# English sentence
# text = "Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."
# file_name = "sample.mp3"
# tts_en = gTTS(text=text, lang="en")
# tts_en.save(file_name)
# playsound(file_name)  # mp3 파일 재생

# 한글 문장
# text = "내가 까르보 불닭볶음면 한 개 먹었다."
# file_name = "sample_ko.mp3"
# tts_ko = gTTS(text=text, lang="ko")
# tts_ko.save(file_name)
# playsound(file_name)  # mp3 파일 재생

# 긴 문장(파일에서 불러온 후 처리)
with open("sample.txt", "r", encoding="utf8") as f:
    text = f.read()

file_name = "sample_ko.mp3"
tts_ko = gTTS(text=text, lang="ko")
tts_ko.save(file_name)
playsound(file_name)  # mp3 파일 재생