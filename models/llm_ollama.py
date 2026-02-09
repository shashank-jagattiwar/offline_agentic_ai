import ollama  # pyright: ignore[reportMissingImports]


class OllamaLLM:
    def __init__(self, model_name="tinyllama"):
        # -------- CURRENT MODE (LOW RAM, FAST) --------
        self.model = model_name

        # -------- DRDO MODE (UNCOMMENT IF NEEDED) --------
        # self.model = "phi3:mini"
        # self.model = "mistral"

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                options={
                    "temperature": 0.2,   # more accurate answers
                    "num_predict": 120    # limit response size → faster
                }
            )

            return response["message"]["content"]

        except Exception as e:
            return f"LLM Error: {str(e)}"
