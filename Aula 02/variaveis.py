'''
Variáveis

As variáveis são espaços na memória que a sua aplicação utiliza para armazenar
os dados em tempo de execução.

Regras de nomenclatura:
    * Não pode começar com símbolos (exceção do _) e números.
    * Os nomes devem ser descritivos e de simples entendimento.
    * Cada nova palavra da variável deve ser separada por _. (Python)

Linguagens dinâmicamente tipadas x Linguagens estaticamente tipadas

'''

nome: str = "William"
cpf: str = "010.101.010-10"
idade: int = 22
altura: float = 1.80
presente: bool = True
vazio = None

print(cpf)
print(type(nome))
print(type(vazio))
print(hex(id(cpf)))

valor1, valor2 = 10, 20
print(valor1, valor2)

a, b = 1, 2
auxiliar = a # a = 1, b = 2, auxiliar = 1
a = b # a = 2, b = 2, auxiliar = 1
b = auxiliar # a = 2, b = 1, auxiliar = 1
print(a, b)

# Isso é exclusivo do Python
c, d = 1, 2
d, c = c, d
print(c, d)