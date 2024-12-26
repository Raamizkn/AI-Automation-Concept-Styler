# src/constraints.py

def apply_basic_constraints(prompt: str) -> str:
    """
    In a real system, you'd filter or transform the prompt according
    to brand identity or engineering constraints. Here we just do a placeholder
    transformation.
    """
    # Example: Ensure mention of "4 wheels" and "aerodynamic shape" for a minimal car concept
    if "car" not in prompt.lower():
        prompt += " car"
    if "wheels" not in prompt.lower():
        prompt += " with 4 wheels"
    if "aerodynamic" not in prompt.lower():
        prompt += " featuring an aerodynamic body"
    
    return prompt
