# src/generate.py

import torch
from diffusers import StableDiffusionPipeline
from typing import Tuple
import os
from src.config import MODEL_NAME, OUTPUT_DIR

class ConceptStyler:
    def __init__(self, model_name: str = MODEL_NAME, device: str = "cpu"):
        """
        Initialize the Stable Diffusion pipeline.
        For Apple Silicon with MPS, use device="mps".
        """
        self.device = device
        print(f"Loading model on device: {self.device}")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
        )
        self.pipe.to(self.device)

    def generate_image(self, prompt: str, steps: int = 30, guidance_scale: float = 7.5) -> Tuple[str, str]:
        """
        Generate an image from a text prompt and save it locally.
        Returns tuple of (filepath, prompt_used).
        """
        # Run inference
        with torch.autocast(self.device):
            image = self.pipe(prompt, num_inference_steps=steps, guidance_scale=guidance_scale).images[0]

        # Build filename
        filename = prompt.replace(" ", "_")[:50]  # Basic sanitation/truncation
        filepath = os.path.join(OUTPUT_DIR, f"{filename}.png")
        
        # Save
        image.save(filepath)
        return filepath, prompt
