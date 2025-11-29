import openai
import requests
from PIL import Image
from io import BytesIO

def generate_tarot_image(card_name, api_key):
    """
    Generate Tarot card image using OpenAI DALL·E API
    """
    openai.api_key = api_key

    prompt = f"Digital painting of Tarot card: {card_name}, mystical, detailed, fantasy style"

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']
    img_data = requests.get(image_url).content
    img = Image.open(BytesIO(img_data))
    return img
