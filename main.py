import os
from google import genai

# Initialisation du client IA
client = genai.Client()

def analyser_projet(description_projet: str):
    prompt = f"""
    Tu es une IA spécialisée en architecture et génie civil.
    Analyse le projet suivant et donne des conseils de conception, 
    d'aménagement et de structures :
    
    Projet : {description_projet}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    test_projet = "Immeuble R+4 à usage résidentiel et commercial sur un terrain de 32x17 mètres"
    print("Analyse du projet en cours...\n")
    # print(analyser_projet(test_projet))
