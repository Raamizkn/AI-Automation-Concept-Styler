# app.py

import streamlit as st
import torch
from src.config import APP_TITLE
from src.interface import show_sidebar, main_interface
from src.generate import ConceptStyler
from src.constraints import apply_basic_constraints

def run_app():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    device, steps, guidance = show_sidebar()
    prompt, generate_btn = main_interface()

    if generate_btn:
        # 1. Apply constraints or brand logic
        final_prompt = apply_basic_constraints(prompt)
        st.write(f"**Final Prompt after Constraints:** {final_prompt}")

        # 2. Load or initialize model pipeline
        st.write("Initializing model (this may take a moment)...")
        styler = ConceptStyler(device=device)

        # 3. Generate image
        with st.spinner("Generating image..."):
            filepath, used_prompt = styler.generate_image(final_prompt, steps, guidance)
        
        # 4. Display result
        st.success(f"Image generated! Saved at: {filepath}")
        st.image(filepath, caption=f"Prompt: {used_prompt}", use_column_width=True)

if __name__ == "__main__":
    run_app()
