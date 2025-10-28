import speech_recognition as sr

class Mystt():

  # 스태틱 변수 만들어서 등록하기 위함
  cobject = []

  def __init__(self):
    self.recognizer = sr.Recognizer()
    
    # 스태틱 변수 등록
    self.cobject.append(self)

  def transcribe_audio(self, file):
    with sr.AudioFile(file) as source:
      audio = self.recognizer.record(source)

    try:
      text = self.recognizer.recognize_google(audio, language='ko-KR')

    except:
      print("오류가 발생했습니다.")
      return ""

    print(text)
    return text