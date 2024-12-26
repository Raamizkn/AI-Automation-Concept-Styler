# src/config.py

import os

# Hugging Face model details
MODEL_NAME = "runwayml/stable-diffusion-v1-5"

# Where to save generated images
OUTPUT_DIR = os.path.join(os.getcwd(), "generated_images")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Streamlit configuration
APP_TITLE = "AI-Driven Automotive Concept Styler"
