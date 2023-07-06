input_string = "Hello, World!"

def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
    return result


remove_duplicates(input_string)