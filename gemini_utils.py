import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get the API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_content(content_request, subject, topic, form, user_type, language):
    prompt = f"As an educational content creator, {content_request} "
    prompt += f"The subject is {subject} for {form}. "
    if topic:
        prompt += f"Focus specifically on the topic: {topic}. "
    prompt += f"This is for a {'teacher creating a lesson plan' if user_type == 'Teacher' else 'student creating a revision plan'}. "
    prompt += f"Provide a structured {'lesson' if user_type == 'Teacher' else 'revision'} plan with clear explanations and examples. "
    prompt += f"The entire response should be in {language}."
    
    response = model.generate_content(prompt)
    return response.text