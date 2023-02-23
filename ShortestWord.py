def find_short(s):
    l = min(len(s) for s in s.split())
    return l # l: shortest word length