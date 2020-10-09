import speech_recognition as sr
from fuzzywuzzy import fuzz, process


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


def ver_texto_similar_fuzzy():
    print("Resultado para apenas uma palavra parcialmente")
    print("==============================================")
    print("Similaridade de:", fuzz.ratio('Renildo', 'Renild'), '\n')

    lista = ['João carlos', 'joão batista', 'Renildo Sousa Vale']
    print('Resultado para apenas uma lista parcialmente')
    print("==============================================")
    print("Similaridade de:", process.extract('Renildo', lista, scorer=fuzz.ratio))
