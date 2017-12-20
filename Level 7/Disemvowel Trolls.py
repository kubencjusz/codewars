def disemvowel(string):
    samogloski=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return ' '.join([''.join([k for k in wyraz if k not in samogloski]) for wyraz in string.split()])