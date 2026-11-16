"""EXP14: Subject-Verb Agreement
DSA03 - Natural Language Processing Lab
"""
# Simple CFG-inspired agreement checker.
singular_subjects = {"he", "she", "it", "boy", "girl", "cat"}
plural_subjects = {"they", "we", "you", "boys", "girls", "cats"}
singular_verbs = {"runs", "eats", "plays", "is"}
plural_verbs = {"run", "eat", "play", "are"}

def check(sentence):
    words = sentence.lower().split()
    subject = words[0]
    verb = words[1]
    if subject in singular_subjects:
        return verb in singular_verbs
    if subject in plural_subjects:
        return verb in plural_verbs
    return False

for s in ["He runs", "They run", "She eat", "Boys plays"]:
    print(f"{s:15} -> {'AGREEMENT' if check(s) else 'ERROR'}")
