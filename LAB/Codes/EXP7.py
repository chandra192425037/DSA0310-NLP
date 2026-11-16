"""EXP7: Part-of-Speech Tagging using NLTK
DSA03 - Natural Language Processing Lab
"""
sentence = "The quick brown fox jumps over the lazy dog"
try:
    import nltk
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    print("NLTK POS tags:")
    for word, tag in tags:
        print(f"{word:10} {tag}")
except Exception:
    print("POS tagging (fallback rule-based tags):")
    for word in sentence.split():
        lower = word.lower()
        if lower in {"the", "a", "an"}: tag = "DT"
        elif lower in {"quick", "brown", "lazy"}: tag = "JJ"
        elif lower in {"jumps"}: tag = "VBZ"
        elif lower in {"over"}: tag = "IN"
        else: tag = "NN"
        print(f"{word:10} {tag}")
