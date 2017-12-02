def replace_exclamation(s):
    samog = 'aeiouAEIOU'
    nowy = ''
    for literka in s:
        if literka in list(samog):
            nowy+='!'
        else:
            nowy+=literka
    return nowy