def filter_string(text, simbol):
    new_text = ''
    for i in text:
        if i.lower() == simbol.lower():
            i = ''
        new_text += i
    return new_text

text = 'If I look forward I win'
print(filter_string(text, 'i')) 
print(filter_string(text, 'O'))  