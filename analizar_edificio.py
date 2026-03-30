"""Analiza una foto de edificio usando Claude Vision para extraer datos estructurales."""
import base64
import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROMPT = """Eres un experto en construcción y normativa chilena (OGUC). Analiza esta fotografía de un edificio y entrega la siguiente información en formato JSON.

Debes responder SOLO con el JSON, sin texto adicional.

{
  "clase_estructura": "(CLASE A, B, C, D o E según Art. 5.3.1 OGUC: A=Acero, B=Hormigón armado, C=Albañilería reforzada, D=Albañilería confinada, E=Madera)",
  "descripcion_estructura": "(Describe los elementos estructurales que se observan o infieren: fundaciones, pilares, muros, vigas, losas. Ejemplo: 'Estructura de hormigón armado. Los elementos estructurales corresponden a fundaciones, pilares, muros, vigas y losas. Se observa edificio de X pisos con muros y losas de hormigón armado')",
  "tabiques_interiores": "(Infiere el tipo de tabiquería interior más probable según el tipo de construcción. Ejemplo: 'Tabiquería en perfiles metálicos de acero galvanizado (tipo volcomental) y placas de yeso-cartón (volcanita) y aislación de colchonetas de lana mineral.')",
  "fachadas_exteriores": "(Describe detalladamente lo que observas en la fachada: materiales, ventanas, balcones, revestimientos, barandas, equipos visibles, acceso principal. Ejemplo: 'Fachada con ventanas y ventanales, estos últimos para dar acceso a balcones. Materiales predominantes: Fachadas exteriores de hormigón armado con revestimiento de estuco pintado (se observa terminación lisa color beige/crema). Balcones con barandas metálicas de acero. Vanos con marcos de aluminio con cristales simples.')"
}

Sé detallado y técnico. Describe exactamente lo que observas en la imagen. Si no puedes determinar algo con certeza, indica lo más probable según el tipo de edificio."""


def analizar_foto(image_bytes, media_type="image/jpeg"):
    """Analiza una foto de edificio y retorna los datos estructurales."""
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": PROMPT,
                    },
                ],
            }
        ],
    )

    response_text = message.content[0].text.strip()
    # Limpiar posible markdown
    if response_text.startswith("```"):
        response_text = response_text.split("\n", 1)[1]
        response_text = response_text.rsplit("```", 1)[0]

    return json.loads(response_text)
