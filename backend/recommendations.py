def get_recommendations(disease_label: str) -> dict:
    """
    Returns specific recommendations based on the disease category.
    Categorizes the 39 PlantVillage classes into Fungal, Bacterial, Viral, Pests, or Healthy.
    """
    disease_lower = disease_label.lower()
    
    # 1. Healthy Plants
    if "healthy" in disease_lower:
        return {
            "immediate": ["No immediate treatment required – plant is healthy."],
            "organic": ["Continue using organic compost to maintain soil health."],
            "chemical": ["No chemical treatment needed."],
            "preventive": ["Maintain crop rotation.", "Provide adequate spacing for air circulation."]
        }
    
    # 2. Viral Diseases (Leaf Curl, Mosaic Virus)
    # These have no cure; focus is on vector control and removal.
    if any(v in disease_lower for v in ["virus", "curl", "mosaic"]):
        return {
            "immediate": [
                "Remove and burn/bury infected plants immediately to prevent spread.",
                "Rogue (destroy) symptomatic plants as there is no cure for viral infections."
            ],
            "organic": ["Use reflective mulches to deter aphids/whiteflies.", "Apply neem oil to manage insect vectors."],
            "chemical": ["Use systemic insecticides to control whiteflies or aphids that spread the virus."],
            "preventive": ["Use virus-free seeds.", "Control weeds that may harbor the virus.", "Plant resistant varieties."]
        }
    
    # 3. Bacterial Diseases (Bacterial Spot, Citrus Greening/Haunglongbing)
    if "bacterial" in disease_lower or "haunglongbing" in disease_lower:
        return {
            "immediate": [
                "Prune infected branches and destroy them.",
                "Avoid overhead watering which spreads bacteria via splashing."
            ],
            "organic": ["Apply copper-based sprays (approved for organic use) early in the season.", "Improve soil drainage."],
            "chemical": ["Use streptomycin or other specialized bactericides if permitted locally.", "Apply fixed copper fungicides."],
            "preventive": ["Sanitize tools after every use.", "Source certified disease-free seedlings.", "Avoid working in the field when plants are wet."]
        }
    
    # 4. Pests (Spider Mites)
    if "spider_mites" in disease_lower:
        return {
            "immediate": [
                "Blast the undersides of leaves with a strong stream of water to dislodge mites.",
                "Increase humidity in the area if possible."
            ],
            "organic": ["Apply insecticidal soap or horticultural oil.", "Release predatory mites (biological control)."],
            "chemical": ["Apply specialized miticides (Abamectin or Bifenthrin).", "Ensure thorough coverage of leaf undersides."],
            "preventive": ["Monitor plants regularly during dry, hot weather.", "Keep plants well-watered to reduce stress."]
        }
    
    # 5. Fungal Diseases (Everything else: Scab, Rust, Blight, Mildew, Spot, Rot, Mold, Esca)
    # Most PlantVillage diseases are fungal.
    return {
        "immediate": [
            "Remove visibly infected leaves/fruit immediately.",
            "Improve air circulation by pruning dense foliage."
        ],
        "organic": ["Apply sulfur or potassium bicarbonate sprays.", "Use compost tea to boost plant immunity."],
        "chemical": ["Apply appropriate fungicides (Chlorothalonil or Mancozeb) every 7-14 days.", "Use systemic fungicides for deep-seated infections."],
        "preventive": ["Avoid watering foliage; use drip irrigation.", "Rotate crops to non-host plants for 3 years.", "Clean up all crop debris at the end of the season."]
    }
