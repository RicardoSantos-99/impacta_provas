import numeros
import os.path


def testa_imports_inputs(arq="numeros.py"):
    if os.path.exists(arq):
        with open(arq, 'r') as f:
            conteudo = f.read()
            if "import " in conteudo:
                raise Exception(
                    'Erro: o arquivo "numeros.py" não pode importar bibliotecas externas!')
            elif "input(" in conteudo:
                raise Exception(
                    'Erro: o arquivo "numeros.py" não pode usar o comando input(). Você não deve ler entradas do usuário diretamente. Você só pode usar os valores passados por parâmetro para as funções.')


def print_cabecalho(titulo):
    n = len(titulo)
    print()
    print('#'*(n+6))
    print(f'# {titulo:^{n+2}} #')
    print('#'*(n+6))
    print()


def compara_respostas(funcao, testes, respostas):
    print('Entrada | Saída obtida | Saída esperada')
    padrao_saida = '{:^7} | {:^12} | {:^14}'
    for teste, resp in zip(testes, respostas):
        print(padrao_saida.format(
            teste,
            str(funcao(teste)),
            str(resp)
        ))


# --------------------------------------------------------------------- #

testa_imports_inputs()
pausar = input('Deseja pausar após cada teste? (s/n): ').lower() == 's'

# --------------------------------------------------------------------- #
print_cabecalho("função eh_primo")
testes = [7, 13, 19, 10, 15, 21]
respostas = [True, True, True, False, False, False]
compara_respostas(numeros.eh_primo, testes, respostas)

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_primos")
print('primos até 20:')
print('resposta obtida:  ', numeros.lista_primos(20))
print('resposta esperada:', [2, 3, 5, 7, 11, 13, 17, 19])

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função conta_primos")
d = numeros.conta_primos([11, 2, 3, 4, 11, 2, 5, 2])
resposta_esperada = {11: 2, 2: 3, 3: 1, 5: 1}
print('resposta obtida:  ', d)
print('resposta esperada:', resposta_esperada)
print('os dicionários são iguais?', d == resposta_esperada)

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_armstrong")
testes = [0, 5, 15, 28, 153]
respostas = [True, True, False, False, True]
compara_respostas(numeros.eh_armstrong, testes, respostas)

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_quase_armstrong")
testes = [0, 7, 35, 75, 153]
respostas = [False, False, True, True, False]
compara_respostas(numeros.eh_quase_armstrong, testes, respostas)

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_armstrong")
print('números de armstrong de 0 até 1000:')
print('resposta obtida:  ', numeros.lista_armstrong(1000))
print('resposta esperada:', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função eh_perfeito")
testes = [4, 6, 12, 28, 350, 496]
respostas = [False, True, False, True, False, True]
compara_respostas(numeros.eh_perfeito, testes, respostas)

if pausar:
    input('Tecle enter para continuar...')

# --------------------------------------------------------------------- #
print_cabecalho("função lista_perfeitos")
print('números perfeitos de 2 até 1000:')
print('resposta obtida:  ', numeros.lista_perfeitos(1000))
print('resposta esperada:', [6, 28, 496])
