# Import the OpenAI library to access its API functions
import openai  # OpenAI Python SDK

# Set your OpenAI API key to authenticate requests
openai.api_key = "your-api-key"  # Replace with your actual API key

# Create an image based on the prompt using OpenAI's DALL·E model
response = openai.Image.create(  # Call to DALL·E API
    prompt="a cyberpunk cat playing guitar",  # Description of the image to generate
    n=1,  # Number of images to generate
    size="512x512"  # Size of the image
)

# Extract the URL of the generated image from the response
image_url = response['data'][0]['url']  # Access the image URL from the API response

# Print the image URL to the console
print("Image URL:", image_url)  # Output the image URL
