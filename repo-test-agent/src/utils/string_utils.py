def to_uppercase(text: str) -> str:
    return text.upper()

def to_lowercase(text: str) -> str:
    return text.lower()

def capitalize_words(text: str) -> str:
    return " ".join([word.capitalize() for word in text.split()])

def remove_special_chars(text: str) -> str:
    import re
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)
