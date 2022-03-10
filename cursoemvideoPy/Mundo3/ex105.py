

def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num)/len(num)
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


resp = notas(5.5, 9.5, 10, 6.5)
com_sit = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print(com_sit)
