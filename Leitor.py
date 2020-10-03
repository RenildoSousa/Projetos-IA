import speech_recognition as sr


def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio, language='pt-BR')

        print("Você disse: " + frase)

    except sr.UnkownValueError:
        print("Não entendi")

    return frase


def ler_arquivo_audio():
    audio = sr.Recognizer()
    PATH = 'record.wav'

    with sr.AudioFile(PATH) as source:
        arquivo = audio.record(source)

        print(audio.recognize_google(arquivo, language='pt-BR'))
