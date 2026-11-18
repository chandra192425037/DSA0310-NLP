"""EXP25: GPT-3 Text Generation
DSA03 - Natural Language Processing Lab
"""
# Requires an API key and the legacy OpenAI completion endpoint for live generation.
prompt = "Write one sentence about natural language processing."
print("Prompt:", prompt)
try:
    import os, openai
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    openai.api_key = key
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=40, temperature=0.7
    )
    print("Generated:", response.choices[0].text.strip())
except Exception as error:
    print("Live GPT-3 call unavailable:", error)
    print("Sample output: Natural language processing helps computers understand human language.")
