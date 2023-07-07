import re

input = "hello. how are you? i'm fine, thank you."

def capitalize_sentences(text):
    sentences = re.split('([.!?] )', text)
    sentences = [sentence.capitalize() for sentence in sentences]
    text = ''.join(sentences)
    return text


print(capitalize_sentences(input))