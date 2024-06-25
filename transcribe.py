import assemblyai as aai
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("AAPI")

aai.settings.api_key =  api_key

def Transcribe(file):


    transcriber = aai.Transcriber()
    
    transcriber.config.language_detection=True
    transcript = transcriber.transcribe(file)
    

    return(transcript)
