from random import randint


def dados(recebeA):
    mensagemA = []

    valorEMod = valor_e_modificador(recebeA)
    TaAquiPqSim = valorEMod['modificador']
    for x in range(0, multiplicador(recebeA)):
        soma = 0
        listaDeDados = []
        for y in range(0, quantidade(recebeA)):
            dadoRolado = randint(1, int(valorEMod['valor']))
            if dadoRolado == 1 or dadoRolado == int(valorEMod['valor']):
                listaDeDados.append(f'**{dadoRolado}**')
            else:
                listaDeDados.append(str(dadoRolado))
            soma += dadoRolado
            if '!' in recebeA and int(valorEMod['valor']) != 1:
                while dadoRolado == int(valorEMod['valor']):
                    dadoRolado = randint(1, int(valorEMod['valor']))
                    soma += dadoRolado
                    if dadoRolado == 1 or dadoRolado == int(valorEMod['valor']):
                        listaDeDados.append(f'**{dadoRolado}**')
                    else:
                        listaDeDados.append(str(dadoRolado))
            elif '!' in recebeA and int(valorEMod['valor']) == 1:
                return '**( Sim )** | [**\'Sim\'**] | d1!'

        if TaAquiPqSim == ():
            formataçãoDosDados = f'**( {soma} )** | {listaDeDados} | {recebeA}'

        else:
            soma = eval(str(soma)+str(TaAquiPqSim))
            formataçãoDosDados = f'`` {soma} `` ⟵ {listaDeDados}{TaAquiPqSim} | {recebeA}'
    
        mensagemA.append(formataçãoDosDados)
    mensagemA = '\n'.join(mensagemA)
    return mensagemA

def multiplicador(recebeB):
    if '#' in recebeB:
        return int(recebeB[:recebeB.find('#')])
    
    else:
        return int(1)

def quantidade(recebeC):
    if '#' in recebeC:
        if recebeC[recebeC.find('#')+1:recebeC.find('d')].isnumeric():
            return int(recebeC[recebeC.find('#')+1:recebeC.find('d')])
        else:
            return int(1)
    elif recebeC[recebeC.find('d')-1::-1].isnumeric():
        recebeC = recebeC[recebeC.find('d')-1::-1]
        return int(recebeC[::-1])

    else:
        return int(1)
        

def valor_e_modificador(recebeD):
    ValorEMod = {'valor': '', 'modificador': ''}
    if '!' in recebeD:
        recebeD = recebeD.replace('!', '')

    if '+' in recebeD or '-' in recebeD or '*' in recebeD or '/' in recebeD:
        ValorEMod['valor'] = recebeD[recebeD.find('d')+1 : recebeD.translate(recebeD.maketrans('*/-', '+++')).find('+')]
        ValorEMod['modificador'] = str(recebeD[recebeD.translate(recebeD.maketrans('*/-', '+++')).find('+') : ])
    else:
        ValorEMod['valor'] = recebeD[recebeD.find('d')+1 : ]
        ValorEMod['modificador'] = ()
    return ValorEMod 