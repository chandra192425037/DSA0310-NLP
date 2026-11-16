"""EXP1: Regular Expressions
DSA03 - Natural Language Processing Lab
"""
import re

text = "Python is fun. Contact: student@example.com. Call 9876543210."
print("TEXT:", text)
print("Words:", re.findall(r"\b[A-Za-z]+\b", text))
print("Email addresses:", re.findall(r"[\w.-]+@[\w.-]+\.\w+", text))
print("Phone numbers:", re.findall(r"\b\d{10}\b", text))
print("Contains 'Python'?", bool(re.search(r"Python", text)))
