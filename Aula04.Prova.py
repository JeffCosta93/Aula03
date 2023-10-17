pessoas = {
    'João':23,
    'Maria':28,
    'Pedro':35,
     'Lucas':19,
    }

idade_joao = pessoas ['João']
print('Idade de João é: ', idade_joao)

pessoas['Ana'] = 31
print('Dicionario Atualizado: ', pessoas)

def maior_idade(dicionario):
    if not dicionario:
        return None
    pessoa_mais_velha = max(dicionario, key=dicionario.get)
    return pessoa_mais_velha

pessoa_mais_velha = maior_idade(pessoas)

print(f'A pessoa com maior idade é: {pessoa_mais_velha}')