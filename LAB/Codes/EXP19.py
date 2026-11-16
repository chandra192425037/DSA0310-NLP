"""EXP19: Word Sense Disambiguation - Lesk Algorithm
DSA03 - Natural Language Processing Lab
"""
from collections import Counter
senses = {
    "bank_finance": set("money loan deposit account cash finance".split()),
    "bank_river": set("river water shore stream flood".split())
}
sentence = set("I deposited cash at the bank".lower().split())
context = sentence - {"i", "at", "the"}
scores = {sense: len(context & signature) for sense, signature in senses.items()}
best = max(scores, key=scores.get)
print("Context words:", sorted(context))
for sense, score in scores.items():
    print(f"{sense:15} overlap = {score}")
print("Selected sense:", best)
