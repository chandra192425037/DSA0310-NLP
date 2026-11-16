"""EXP3: Morphological Analysis using NLTK
DSA03 - Natural Language Processing Lab
"""
# NLTK is optional; the fallback keeps this experiment runnable offline.
words = ["cats", "playing", "unhappiness", "replayed"]
try:
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    print("Morphological analysis (NLTK WordNet lemmatizer):")
    for word in words:
        print(f"{word:15} -> {lemmatizer.lemmatize(word)}")
except Exception:
    print("Morphological analysis (rule-based fallback):")
    for word in words:
        root = word
        affixes = []
        for suffix in ("ness", "ing", "ed", "s"):
            if root.endswith(suffix) and len(root) > len(suffix) + 2:
                root = root[:-len(suffix)]
                affixes.append("-" + suffix)
                break
        for prefix in ("un", "re"):
            if root.startswith(prefix) and len(root) > len(prefix) + 2:
                root = root[len(prefix):]
                affixes.insert(0, prefix + "-")
                break
        print(f"{word:15} -> root: {root}, affixes: {''.join(affixes) or 'none'}")
