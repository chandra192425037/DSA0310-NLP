"""EXP2: Finite State Automaton - strings ending with ab
DSA03 - Natural Language Processing Lab
"""
def accepts(s):
    # DFA states: q0=start, q1=last char was a, q2=ends with ab
    state = "q0"
    for ch in s:
        if ch == "a":
            state = "q1"
        elif ch == "b":
            state = "q2" if state == "q1" else "q0"
        else:
            state = "q0"
    return state == "q2"

for sample in ["ab", "aab", "abab", "abb", "ba", "abc"]:
    print(f"{sample!r:8} -> {'ACCEPTED' if accepts(sample) else 'REJECTED'}")
