"""EXP5: Porter Stemming
DSA03 - Natural Language Processing Lab
"""
words = ["playing", "played", "player", "studies", "studying", "connected"]
try:
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    print("Porter Stemmer (NLTK):")
    for word in words:
        print(f"{word:12} -> {stemmer.stem(word)}")
except ImportError:
    print("NLTK is not installed. Simple suffix demonstration:")
    for word in words:
        stem = word
        for suffix in ("ing", "ies", "ed", "er", "s"):
            if stem.endswith(suffix) and len(stem) > len(suffix) + 2:
                stem = stem[:-len(suffix)]
                break
        print(f"{word:12} -> {stem}")
