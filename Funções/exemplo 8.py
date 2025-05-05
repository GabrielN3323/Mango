def formatar_texto(texto, maisculo=False, prefixo="", sufixo=""):
    if maisculo:
        texto = texto.upper()
    return f"{prefixo}{texto}{sufixo}"
print(formatar_texto("python"))
print(formatar_texto("python", True))
print(formatar_texto("python", prefixo="linguagem: "))
print(formatar_texto("python", sufixo=" é incrivel", maisculo=True))