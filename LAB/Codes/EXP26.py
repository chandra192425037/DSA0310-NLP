"""EXP26: Machine Translation using Hugging Face
DSA03 - Natural Language Processing Lab
"""
# First run may download the model: pip install transformers torch sentencepiece
sentence = "Hello, how are you?"
print("English:", sentence)
try:
    from transformers import pipeline
    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    result = translator(sentence, max_length=60)[0]["translation_text"]
    print("French:", result)
except Exception as error:
    print("Live translation unavailable:", error)
    print("Sample French translation: Bonjour, comment allez-vous ?")
