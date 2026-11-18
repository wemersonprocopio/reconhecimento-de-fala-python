import speech_recognition as sr
import time

# Microfone usado na captura. None = microfone padrão do sistema.
# Para usar outro, rode listar_microfones.py e coloque aqui o número dele.
INDICE_MICROFONE = None
COMANDO_PARAR = "encerrar gravação"

acabou = False


def tratar_audio(rec, audio):
    global acabou
    # tratar o meu audio
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
        if COMANDO_PARAR in texto.lower():
            acabou = True
    except sr.UnknownValueError:
        print("Não escutei")
    except sr.RequestError as erro:
        print(f"Não foi possível acessar o serviço de reconhecimento (verifique a internet): {erro}")


rec = sr.Recognizer()
microfone = sr.Microphone(device_index=INDICE_MICROFONE)

with microfone:
    rec.adjust_for_ambient_noise(microfone)
rec.pause_threshold = 0.8
# rec.dynamic_energy_adjustment_ratio = 4
print(f'Pode começar a falar (diga "{COMANDO_PARAR}" para parar):')

# thread 1: ouve em segundo plano e chama tratar_audio a cada trecho
parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

# thread 2: espera o comando de parar
while not acabou:
    time.sleep(0.1)

parar_ouvir(wait_for_stop=False)
print("Gravação encerrada.")
