import openai

openai.api_key = "your-api-key"

response = openai.Image.create(
    prompt="a cyberpunk cat playing guitar",
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']
print("Image URL:", image_url)
