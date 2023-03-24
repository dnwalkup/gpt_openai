import openai
import keys

openai.organization = keys.oai_organization
openai.api_key = keys.oai_api_key

audio_file = open("test.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

print(transcript.text.strip())