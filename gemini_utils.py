import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_content(content_request, subject, topic, form, user_type, language):
    prompt = f"""
    As an educational content creator, {content_request}
    The subject is {subject} for {form}.
    {"Focus specifically on the topic: " + topic + "." if topic else ""}
    This is for a {'teacher creating a lesson plan' if user_type == 'Teacher' else 'student creating a revision plan'}.
    Provide a structured {'lesson' if user_type == 'Teacher' else 'revision'} plan with clear explanations and examples.
    Format the plan as follows:
    1. Objective(s)
    2. Introduction
    3. Main Content (broken into subtopics if applicable)
    4. Activities or Practice Exercises
    5. Assessment or Review
    6. Conclusion
    
    Use numbering for each section and provide detailed content within each.
    The entire response should be in {language}.
    """
    
    response = model.generate_content(prompt)
    return response.text