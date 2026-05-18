text = input("Text: ")

alphabets = set("abcdefghijklmnopqrstuvwxyz")

if alphabets <= set(text.lower()):
    print("True")
else:
    print("False")