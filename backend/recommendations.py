from deep_translator import GoogleTranslator
import time

def translate_recommendations(recs: dict, target_lang: str) -> dict:
    if target_lang == 'en':
        return recs
        
    translator = GoogleTranslator(source='en', target=target_lang)
    translated_recs = {}
    
    for key, items_list in recs.items():
        translated_list = []
        for item in items_list:
            try:
                time.sleep(0.1) # Small sleep to avoid rate limiting
                translated_item = translator.translate(item)
                translated_list.append(translated_item)
            except Exception as e:
                print(f"Error translating recommendation: {e}")
                translated_list.append(item) # fallback to english
        translated_recs[key] = translated_list
        
    return translated_recs

def get_recommendations(disease_label: str, lang: str = 'en') -> dict:
    """
    Returns specific recommendations based on the disease category,
    translated into the requested language.
    Categorizes the 39 PlantVillage classes into Fungal, Bacterial, Viral, Pests, or Healthy.
    """
    disease_lower = disease_label.lower()
    recs = {}
    
    # 1. Healthy Plants
    if "healthy" in disease_lower:
        recs = {
            "immediate": ["No immediate treatment required – plant is healthy."],
            "organic": ["Continue using organic compost (e.g., Vermicompost) to maintain soil health."],
            "chemical": ["No chemical pesticide needed.", "Apply balanced NPK fertilizer (19:19:19) for generic growth."],
            "preventive": ["Maintain crop rotation.", "Provide adequate spacing for air circulation.", "Visit your nearest Agro-Center to restock on organic seeds and fertilizers."]
        }
    
    # 2. Viral Diseases (Leaf Curl, Mosaic Virus)
    elif any(v in disease_lower for v in ["virus", "curl", "mosaic"]):
        recs = {
            "immediate": [
                "Remove and burn/bury infected plants immediately to prevent spread.",
                "Rogue (destroy) symptomatic plants as there is no cure for viral infections."
            ],
            "organic": ["Use reflective mulches to deter aphids/whiteflies.", "Apply Neem Oil (1500 PPM) to manage insect vectors."],
            "chemical": ["Apply systemic insecticides like Bayer Confidor (Imidacloprid) or Syngenta Actara (Thiamethoxam) to control vectors.", "Use exactly as per label instructions."],
            "preventive": ["Use virus-free seeds.", "Control weeds that may harbor the virus.", "Ask your local fertilizer shop for virus-resistant seed varieties for the next season."]
        }
    
    # 3. Bacterial Diseases (Bacterial Spot, Citrus Greening/Haunglongbing)
    elif "bacterial" in disease_lower or "haunglongbing" in disease_lower:
        recs = {
            "immediate": [
                "Prune infected branches and destroy them.",
                "Avoid overhead watering which spreads bacteria via splashing."
            ],
            "organic": ["Apply Copper Oxychloride (Blitox 50) sprays approved for organic use early in the season.", "Improve soil drainage."],
            "chemical": ["Use Streptomycin sulfate (Plantomycin) or specialized bactericides if permitted locally.", "Apply fixed copper fungicides (Syngenta Blue Copper)."],
            "preventive": ["Sanitize tools after every use.", "Source certified disease-free seedlings.", "Consult your nearby Krishi Seva Kendra for localized soil testing kits."]
        }
    
    # 4. Pests (Spider Mites)
    elif "spider_mites" in disease_lower:
        recs = {
            "immediate": [
                "Blast the undersides of leaves with a strong stream of water to dislodge mites.",
                "Increase humidity in the area if possible."
            ],
            "organic": ["Apply Insecticidal soap or Horticultural Oil.", "Release predatory mites (biological control)."],
            "chemical": ["Apply specialized miticides like UPL Phoskill (Monocrotophos) or Bayer Oberon (Spiromesifen).", "Ensure thorough coverage of leaf undersides."],
            "preventive": ["Monitor plants regularly during dry, hot weather.", "Keep plants well-watered to reduce stress.", "Purchase preventive miticides from your fast-delivery local agro shop before summer hits."]
        }
    
    # 5. Fungal Diseases (Everything else: Scab, Rust, Blight, Mildew, Spot, Rot, Mold, Esca)
    else:
        recs = {
            "immediate": [
                "Remove visibly infected leaves/fruit immediately.",
                "Improve air circulation by pruning dense foliage."
            ],
            "organic": ["Apply Sulfur-based fungicides (UPL Sulflox) or Potassium Bicarbonate sprays.", "Use compost tea to boost plant immunity."],
            "chemical": ["Apply broad-spectrum fungicides like Syngenta Amistar (Azoxystrobin) or Bayer Luna Sensation.", "Use systemic fungicides like Ridomil Gold for deep-seated infections."],
            "preventive": ["Avoid watering foliage; use drip irrigation.", "Rotate crops to non-host plants for 3 years.", "Contact your nearby fertilizer retailer to purchase high-quality drip irrigation supplies."]
        }
        
    return translate_recommendations(recs, lang)
