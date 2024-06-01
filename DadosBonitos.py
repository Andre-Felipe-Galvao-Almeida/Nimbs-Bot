from random import randint


def Dados(DiceValue, Estouravel=False):
    """Retorna uma rolagem com minimo de 1 e maximo definido
    DiceValue: É o valor maximo que o dado pode receber
    Estouravel: Se verdadeiro, quando o dado rolado for o maximo, outro dado é rolado e somado"""
    if Estouravel:
        soma = [randint(1, DiceValue)]
        while soma[-1] == DiceValue:
            soma.append(randint(1, DiceValue))
        return soma
    else:    

        return randint(1, DiceValue)



def QuantidadeVezes(ReceivedMessage):
    """Retorna quantas vezes será rolado, definido pelo valor antes do #"""
#Checa se existe '#' na string, se houver, coleta o numero anterior a ela 
#calculando ou roletando dados anteriores a ela
    if "#" in ReceivedMessage:
        while 'd' in ReceivedMessage[0: ReceivedMessage.find('#')]:
            return Recorte(ReceivedMessage[0:ReceivedMessage.find('#')])
    

    else:
        return int(1)



def Recorte(ReceivedMessage):
    """Recebe uma string com calculos usando dados,
    retira os dados do calculo, para poder ser processado.
    Os dados são identificados usando com base o 'd'
    Retorna uma string com o dado separado, e a string que recebida sem o dado"""
    dado = []

#checa todos os caracteres até chegar em um operador aritimetico ou "#", que marca o inicio do dado
    for x in range(ReceivedMessage.find('d'),0,-1):
        if ReceivedMessage[x] in '+-/*&#':
            dado.append(ReceivedMessage[x+1: ReceivedMessage.find('d')])
            break
        
        
        
        
#checa todos os caracteres até chegar a um operador aritimetico, '#' ou espaço, que marca o fim do dado
    for x in range(ReceivedMessage.find('d'),len(ReceivedMessage)):
        if ReceivedMessage[x] in '+-/*&# ':
            dado.append(ReceivedMessage[ReceivedMessage.find('d'): x])
            break
    return {'Dado': str(dado[0]+dado[1]), 'StringAlterada': ReceivedMessage.replace(str(dado[0]+dado[1]),"@  @")}


def esqueleto(ReceivedMessage):
    
    for x in range(0, QuantidadeVezes(ReceivedMessage)):
        print('Ta aqui para debugar')

print(Recorte('6d6'))