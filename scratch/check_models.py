import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyApmIuLaf6EHbZZIl208hbyNFlwb9Qi0Rs')

try:
    print("Listing available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error: {e}")
