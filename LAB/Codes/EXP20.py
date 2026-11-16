"""EXP20: Information Retrieval using TF-IDF
DSA03 - Natural Language Processing Lab
"""
import math, re
documents = {
    "D1": "python is a popular programming language",
    "D2": "natural language processing uses python",
    "D3": "database systems store information"
}
query = "python language"
tokenize = lambda s: re.findall(r"\w+", s.lower())
N = len(documents)
vocab = set(w for doc in documents.values() for w in tokenize(doc))
idf = {w: math.log((N + 1) / (sum(w in tokenize(d) for d in documents.values()) + 1)) + 1
       for w in vocab}
qterms = tokenize(query)
scores = {}
for name, doc in documents.items():
    terms = tokenize(doc)
    scores[name] = sum(terms.count(w) * idf.get(w, 0) for w in qterms)
print("Query:", query)
print("Document ranking:")
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score:.3f} | {documents[name]}")
