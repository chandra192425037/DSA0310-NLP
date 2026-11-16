"""EXP6: Bigram N-gram Text Generation
DSA03 - Natural Language Processing Lab
"""
from collections import defaultdict, Counter
import random

text = "the cat sat on the mat the cat ate fish"
tokens = text.split()
bigrams = defaultdict(Counter)
for a, b in zip(tokens, tokens[1:]):
    bigrams[a][b] += 1

print("Training text:", text)
print("Bigram counts:")
for word, following in bigrams.items():
    print(f"  {word} -> {dict(following)}")

random.seed(3)
current = "the"
generated = [current]
for _ in range(9):
    choices = bigrams.get(current)
    if not choices:
        break
    current = choices.most_common(1)[0][0]
    generated.append(current)
print("Generated text:", " ".join(generated))
