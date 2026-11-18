# Reconhecimento de Fala em Python

Projeto desenvolvido em Python para praticar reconhecimento de fala, captura de áudio pelo microfone e transcrição de arquivos de áudio.

O objetivo do projeto é compreender como aplicações Python podem capturar voz, processar áudio e transformar fala em texto.

## Funcionalidades

O projeto possui diferentes exemplos de uso:

- Captura de áudio pelo microfone
- Reconhecimento de fala em português do Brasil
- Gravação de áudio em arquivo `.wav`
- Leitura e transcrição de arquivos de áudio
- Reconhecimento contínuo de fala
- Encerramento da gravação por comando de voz

## Requisitos

- Python 3.9 ou superior
- Um microfone
- Conexão com a internet (a transcrição usa o serviço gratuito de reconhecimento de fala do Google, pela biblioteca SpeechRecognition)

## Instalação

```bash
pip install -r requirements.txt
```

O `requirements.txt` instala o **SpeechRecognition** e o **PyAudio** (usado para acessar o microfone).

## Como usar

```bash
python main.py                     # fala no microfone e mostra o texto
python criar_audio.py              # grava a fala no arquivo audio.wav
python ler_arquivos_audio.py       # transcreve o audio.wav
python ler_arquivos_audio.py x.wav # transcreve outro arquivo
python reconhecer_audio_longo.py   # transcreve sem parar até ouvir "encerrar gravação"
```

Os scripts usam o **microfone padrão** do sistema. Para escolher outro, rode `python listar_microfones.py`, veja o número do microfone e coloque esse número em `INDICE_MICROFONE`, no início do script.

## Arquivos do projeto

### `main.py`

Realiza o reconhecimento de fala utilizando o microfone e converte o áudio capturado em texto.

### `criar_audio.py`

Captura áudio pelo microfone e salva a gravação no arquivo `audio.wav`.

### `ler_arquivos_audio.py`

Lê um arquivo de áudio existente (por padrão, o `audio.wav`) e realiza sua transcrição.

### `reconhecer_audio_longo.py`

Executa reconhecimento contínuo de fala e permite interromper o processo através do comando:

```text
encerrar gravação
```

### `listar_microfones.py`

Lista os microfones disponíveis com o número de cada um.
