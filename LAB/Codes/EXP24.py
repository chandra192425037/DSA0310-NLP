"""EXP24: Dialog Act Recognition
DSA03 - Natural Language Processing Lab
"""
def dialog_act(utterance):
    text = utterance.lower().strip()
    if text.endswith("?") or text.startswith(("who", "what", "where", "when", "why", "how")):
        return "QUESTION"
    if text.startswith(("please", "could you", "can you")):
        return "REQUEST"
    if text.startswith(("hello", "hi", "good morning")):
        return "GREETING"
    if text.startswith(("thanks", "thank you")):
        return "THANKING"
    return "STATEMENT"

dialog = ["Hello!", "Can you open the door?", "Where is the library?",
          "The class starts at ten.", "Thank you."]
for line in dialog:
    print(f"{line:35} -> {dialog_act(line)}")
