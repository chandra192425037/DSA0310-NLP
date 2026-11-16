"""EXP23: Text Coherence Evaluation
DSA03 - Natural Language Processing Lab
"""
sentences = [
    "The student opened a book.",
    "The book contained a chapter about language.",
    "Language is used by people to communicate."
]
def keywords(sentence):
    return {w.strip(".,").lower() for w in sentence.split()
            if len(w.strip(".,").lower()) > 4}
scores = []
for a, b in zip(sentences, sentences[1:]):
    overlap = len(keywords(a) & keywords(b))
    scores.append(overlap)
    print(f"Sentence pair overlap: {overlap}")
average = sum(scores) / len(scores)
print(f"Coherence overlap score: {average:.2f}")
print("Interpretation:", "RELATED" if average > 0 else "WEAKLY RELATED")
