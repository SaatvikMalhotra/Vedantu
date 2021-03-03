import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
  print("Start Speaking!")
  audio=r.listen(source)
  try:
    text=r.recognize_google(audio)
  except:
    text="Sorry couldent catch that, please try again"
  print(text)
