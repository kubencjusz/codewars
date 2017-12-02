def to_freud(sentence):
    return ' '.join('sex' for _ in sentence.split())

KandZ = to_freud("Kuba & Zbyszek")
print("Hello " + Kan    dZ + " BFMF")