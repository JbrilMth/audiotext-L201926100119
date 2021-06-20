import  speech_recognition as sr
rec = sr.Recognizer()
audioF = 'sound3.wav'
with sr.AudioFile(audioF) as sourceF:
    audio = rec.record(sourceF)
    print('File Reading . . .')

print('File Text is: ')
try:
    text = rec.recognize_google(audio)
    print(text)

except Exception as e:
    print(e)