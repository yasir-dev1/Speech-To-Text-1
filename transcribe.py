import assemblyai as aai


def Transcribe(file):

    aai.settings.api_key = "bf3cfaf02c3c47d2a1632aca76505bed"

    transcriber = aai.Transcriber()
    transcriber.config.language_detection=True
    transcript = transcriber.transcribe(file)



    return(transcript.text)
langnages ={

    "Global English": "en",
    "Australian English":"en_au", 
    "British English":"en_uk",
    "US English":"en_us",
    "Spanish":"es",
    "French":"fr",
    "German":"de",
    "Italian":"it",
    "Portuguese":"pt",
    "Dutch":"nl",
    "Hindi":"hi",
    "Japanese":"ja",
}
