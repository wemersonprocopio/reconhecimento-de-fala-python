import speech_recognition as sr

# Mostra os microfones disponíveis com o número de cada um.
# Use o número em INDICE_MICROFONE nos outros scripts para escolher um microfone específico.
for indice, nome in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{indice}: {nome}")
