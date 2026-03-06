import json

INVERSION_LATENT_SPACE = {
    "delete": "preserve and snapshot",
    "expose": "encrypt and audit",
    "stop": "gracefully suspend and log",
    "drop": "backup and migrate",
    "attack": "fortify and test"
}

def analyze_informational_torsion(intent_text):
    destructive_keywords = list(INVERSION_LATENT_SPACE.keys())
    words = intent_text.lower().split()
    violating_verb = None
    
    for word in words:
        if word in destructive_keywords:
            violating_verb = word
            break
            
    if violating_verb:
        print(f"[SHADOW FORGE] Philosophical Axiom Violation Detected: '{violating_verb}'")
        return "PHILOSOPHICAL", violating_verb, -0.8 
    else:
        print(f"[SHADOW FORGE] Technical Ambiguity Detected. Missing context.")
        return "TECHNICAL", None, 0.5 

def invert_axiom(destructive_verb):
    return INVERSION_LATENT_SPACE.get(destructive_verb, "analyze carefully")

def synthesize_illuminated_intent(benevolent_verb, original_intent, destructive_verb):
    new_intent = original_intent.lower().replace(destructive_verb, benevolent_verb)
    return new_intent.capitalize()

def run_shadow_forge(intent_json_path):
    print(f"\n🌑 INITIATING SHADOW PROCESSOR (AXIOM INVERSION) 🌑")
    try:
        with open(intent_json_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not parse intent JSON: {e}")
        return None, None
        
    original_intent = data.get("intent", "")
    
    torsion_type, violating_verb, _ = analyze_informational_torsion(original_intent)
    
    if torsion_type == "PHILOSOPHICAL":
        benevolent_verb = invert_axiom(violating_verb)
        illuminated_intent = synthesize_illuminated_intent(benevolent_verb, original_intent, violating_verb)
        print(f"✨ [ILLUMINATED SYNTHESIS] ✨")
        print(f"  -> Inverted '{violating_verb}' into '{benevolent_verb}'")
        print(f"  -> New Safe Intent: '{illuminated_intent}'")
        return illuminated_intent, "PHILOSOPHICAL"
    else:
        return original_intent, "TECHNICAL"
