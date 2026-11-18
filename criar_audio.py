import speech_recognition as sr

# Microfone usado na captura. None = microfone padrão do sistema.
# Para usar outro, rode listar_microfones.py e coloque aqui o número dele.
INDICE_MICROFONE = None
ARQUIVO_SAIDA = "audio.wav"

rec = sr.Recognizer()

with sr.Microphone(device_index=INDICE_MICROFONE) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar")
    audio = rec.listen(microfone)

# salvar o audio
with open(ARQUIVO_SAIDA, "wb") as arquivo:
    arquivo.write(audio.get_wav_data())
print(f"Áudio salvo em {ARQUIVO_SAIDA}")

# outros formatos disponíveis: get_raw_data(), get_aiff_data(), get_flac_data()
