materialEscolar = ['lapis', 'estojo',
                   'mochila', 'bolsinha',
                   'borracha', 'garrafa']

materialEscolar.pop(4)
materialEscolar.remove('bolsinha')
materialEscolar.__delitem__(0)

print(materialEscolar)