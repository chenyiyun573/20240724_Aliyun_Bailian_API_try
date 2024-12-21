import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def query_gpt4v(prompt, image_path=None):
    # Set the API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key is missing in the environment variables")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Prepare the user message content with the prompt text
    user_content = [{"type": "text", "text": prompt}]

    # Encode the image to base64 and include in the payload if an image path is provided
    if image_path:
        if not os.path.exists(image_path):
            raise ValueError(f"Image path {image_path} does not exist")
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('ascii')
        user_content.insert(0, {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
        })

    # Make the API call
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are an AI assistant that helps people find information."}
                    ]
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ],
            temperature=0.7,
            top_p=0.95,
            max_tokens=800
        )
        # Return the generated response
        message1 = completion.choices[0].message
        response = message1.content if hasattr(message1, 'content') else str(message1)
        return response
    except Exception as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")


# Example usage
if __name__ == "__main__":
    prompt_text = "What's in this image?"
    image_path = "dog_and_girl.jpeg"  # Replace with your image path or set to None for text-only queries
    response = query_gpt4v(prompt_text, image_path)
    print(response)


