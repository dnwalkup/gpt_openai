import openai

openai.organization = "org-avmR5XV53t3FVcuTEKCQl15p"
openai.api_key = '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'

audio_file = open("test.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

print(transcript.text.strip())