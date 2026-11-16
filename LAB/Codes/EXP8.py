"""EXP8: Stochastic POS Tagging
DSA03 - Natural Language Processing Lab
"""
# A tiny probabilistic tagger using emission probabilities.
emission = {
    "time": {"NN": 0.8, "VB": 0.2},
    "flies": {"NN": 0.3, "VB": 0.7},
    "like": {"IN": 0.6, "VB": 0.4},
    "an": {"DT": 1.0},
    "arrow": {"NN": 1.0}
}
sentence = "time flies like an arrow".split()
print("Sentence:", " ".join(sentence))
for word in sentence:
    scores = emission.get(word, {"NN": 1.0})
    tag = max(scores, key=scores.get)
    print(f"{word:10} -> {tag} (P={scores[tag]:.1f})")
