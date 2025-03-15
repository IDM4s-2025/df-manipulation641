import whisper

model = whisper.load_model("small")
result = model.transcribe("ruta/al/archivo/Entrevista.opus")

print(result["text"])
