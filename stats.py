def get_num_words(text):
    return len(text.split())
def get_num_chars(text):
    chars = {}
    for ch in text:
        if ch.lower() in chars:
            chars[ch.lower()] += 1
        else:
            chars[ch.lower()] = 1
    return chars

def format_dict(map):
    return sorted([{"char": key, "num": v} for key,v in map.items()], key=lambda x: x["num"], reverse=True)