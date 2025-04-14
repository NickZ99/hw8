def process_text(text):
    uppercase_count = 0
    for char in text:
        if 'A' <= char <= 'Z':
            uppercase_count += 1
    uppercase_text = text.upper()
    return uppercase_count, uppercase_text
user_input = input("Please enter text: ")
count, upper_text = process_text(user_input)
print (f"In Text {count} Uppercase letters")
print (f"Text in uppercase letters: {upper_text}")
