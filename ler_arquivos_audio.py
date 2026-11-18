import sys
import speech_recognition as sr

# Arquivo a transcrever: o informado na linha de comando ou, por padrão,
# o audio.wav gravado pelo criar_audio.py.
# Exemplo: python ler_arquivos_audio.py minha_gravacao.wav
arquivo = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"

rec = sr.Recognizer()

try:
    with sr.AudioFile(arquivo) as arquivo_audio:
        audio = rec.record(arquivo_audio)
except FileNotFoundError:
    sys.exit(f"Arquivo não encontrado: {arquivo}. Grave um com criar_audio.py ou informe outro caminho.")

try:
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError as erro:
    print(f"Não foi possível acessar o serviço de reconhecimento (verifique a internet): {erro}")
