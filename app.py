import speech_recognition as sr

rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names())