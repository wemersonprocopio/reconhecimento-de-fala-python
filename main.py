import speech_recognition as sr

# Microfone usado na captura. None = microfone padrão do sistema.
# Para usar outro, rode listar_microfones.py e coloque aqui o número dele.
INDICE_MICROFONE = None

# - criar um "reconhecedor"
rec = sr.Recognizer()

# - ouvir o audio do microfone
with sr.Microphone(device_index=INDICE_MICROFONE) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar:")

    # rec.pause_threshold = 1 # coloque isso se quiser que ele demore mais para entender que uma pausa é o fim do audio

    audio = rec.listen(microfone)

try:
    # reconhece esse audio e traduz ele pra texto
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError as erro:
    print(f"Não foi possível acessar o serviço de reconhecimento (verifique a internet): {erro}")
