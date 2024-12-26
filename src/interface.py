# src/interface.py

import streamlit as st
from src.generate import ConceptStyler
from src.constraints import apply_basic_constraints

def show_sidebar():
    """
    Create a sidebar for model settings, device selection, etc.
    """
    st.sidebar.header("Settings")
    device = st.sidebar.selectbox("Device", ["cpu", "mps", "cuda"], index=0)
    steps = st.sidebar.slider("Inference Steps", min_value=5, max_value=100, value=30)
    guidance = st.sidebar.slider("Guidance Scale", min_value=1.0, max_value=15.0, value=7.5)
    return device, steps, guidance

def main_interface():
    """
    Main Streamlit interface for generating car concepts.
    """
    st.title("AI-Driven Automotive Concept Styler")
    st.write("""
    Enter a prompt describing your dream vehicle concept, and let AI generate
    an automotive design idea. This is a simplified demo using Stable Diffusion.
    """)

    prompt = st.text_input("Design Prompt", "A sleek futuristic sports coupe")
    generate_btn = st.button("Generate Concept")

    return prompt, generate_btn
