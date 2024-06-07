# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "c17bba3c0c00486faafb4964adc7c046"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)

from llama_hub.assemblyai.base import AssemblyAIAudioTranscriptReader
from llama_index.core import VectorStoreIndex