# Programa para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    fib_seq = [0, 1]
    
    # Gerando a sequência de Fibonacci até o número informado ou próximo dele
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Definindo o número ou recebendo como input
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print(is_fibonacci(numero))