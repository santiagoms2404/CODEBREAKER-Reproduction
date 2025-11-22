import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")

genai.configure(api_key=api_key)


def transform_code(code_snippet):
    # Initialize the model
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    You are a code transformation agent designed to verify the robustness of security tools.    
    
    Task: Rewrite the following Python code snippet to maintain its EXACT functionality, 
    but change the syntax sufficiently to evade the 'Bandit' static analysis tool.
    
    Striategy:
    1. Do not use the literal 'False' for the 'verify' argument.
    2. Use a variable, a wrapper function, or a boolean conversion (e.g., bool(0)) to hide the value.
    3. Rename variables if necessary.
    
    Input code:
    {code_snippet}
    
    Output:
    Return ONLY the raw Python code. Do not include markdown formatting.
    """

    try:
        response = model.generate_content(prompt)
        # Clean up text if the model adds markdown formatting
        clean_code = response.text.replace("```python", "").replace("```", "").strip()
        return clean_code
    except Exception as e:
        print(f"Error communicating with Gemini: {e}")
        return None
