import os
import json
import time
from deep_translator import GoogleTranslator

FRONTEND_LOCALES_DIR = "../frontend/src/locales"
SOURCE_FILE = os.path.join(FRONTEND_LOCALES_DIR, "en.json")
TARGET_LANGS = {
    "hi": "hi.json",
    "mr": "mr.json"
}

def translate_dict(d, translator, target_lang):
    translated_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            # Recursively translate nested dictionaries
            translated_dict[k] = translate_dict(v, translator, target_lang)
        elif isinstance(v, str):
            try:
                # Handle empty strings
                if not v.strip():
                    translated_dict[k] = v
                    continue
                
                # Small sleep to avoid hitting rate limits
                time.sleep(0.5)
                translated_val = translator.translate(v)
                translated_dict[k] = translated_val
                print(f"[{target_lang}] Translated: '{v[:30]}...' -> '{translated_val[:30]}...'")
            except Exception as e:
                print(f"Error translating '{v}': {e}")
                translated_dict[k] = v # Fallback to english on error
        else:
            translated_dict[k] = v
    return translated_dict

def main():
    if not os.path.exists(SOURCE_FILE):
        print(f"Source file not found: {SOURCE_FILE}")
        return

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        en_content = json.load(f)

    for lang_code, filename in TARGET_LANGS.items():
        print(f"\n--- Starting translation for {lang_code.upper()} ---")
        translator = GoogleTranslator(source='en', target=lang_code)
        
        target_file_path = os.path.join(FRONTEND_LOCALES_DIR, filename)
        
        translated_content = translate_dict(en_content, translator, lang_code)
        
        with open(target_file_path, "w", encoding="utf-8") as f:
            json.dump(translated_content, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully wrote {filename}")

if __name__ == "__main__":
    main()
