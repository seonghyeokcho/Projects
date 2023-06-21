import speech_recognition as sr


# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("듣고 있어요.")
    audio = r.listen(source)

# 파일로부터 음성 불러오기 - 확장자 wav, aiff/aiff-c, flac 만 가능 / mp3 불가능
# file_name = None  # 여기에 음성파일 경로 작성
# r = sr.Recognizer()
# with sr.AudioFile(file_name) as source:
#     audio = r.record(source)

try:
    # Google API로 인식(하루 50회 까지 가능)
    text = r.recognize_google(audio_data=audio, language="ko")  # 영어: language="en-US"
    print(text)
except sr.UnknownValueError:
    print("인식 실패")  # 음성 인식을 실패한 경우
except sr.RequestError as e:
    print(f"요청 실패 : {e}")  # API Key 오류 혹은 네트워크 단절 등
