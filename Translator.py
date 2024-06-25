import requests,dotenv,os

dotenv.load_dotenv()

def translate_text(text, target_language):
    api_key = os.getenv("DAPI") 
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}"
    }
    data = {
        "text": text,
        "target_lang": target_language
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    
    if 'translations' in result:
        return result['translations'][0]['text']
    else:
        return "Translation failed."
