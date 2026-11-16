"""EXP16: Named Entity Recognition using spaCy
DSA03 - Natural Language Processing Lab
"""
text = "Apple was founded by Steve Jobs in California in 1976."
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    print("Named entities (spaCy):")
    for ent in doc.ents:
        print(f"{ent.text:20} {ent.label_}")
except Exception:
    print("Named entities (offline demonstration):")
    for entity, label in [("Apple", "ORG"), ("Steve Jobs", "PERSON"),
                          ("California", "GPE"), ("1976", "DATE")]:
        print(f"{entity:20} {label}")
