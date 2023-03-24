import whisper, os

model = whisper.load_model(name="large-v1", download_root="c:/download")

result = model.transcribe("test.mp3")
print(result["text"])