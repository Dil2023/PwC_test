input = "Hello, World! OpenAI is amazing."

def revertWords(input):
    string_splitted = input.split(" ")
    reversed_words = string_splitted[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

revertWords(input)