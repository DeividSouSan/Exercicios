print("Exercício 2: ")

def fibonacci(n):
    sequence = [0, 1]
    
    for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        
    return sequence

n = int(input("Digite um número: "))
i = 0

while True:
    
    sequence = fibonacci(i)
    
    if n in sequence:
        print("O número faz parte da sequencia.")
        print(sequence)
        break
    else:
        if sequence[-1] > n:
            print("O número não faz parte da sequencia.")
            print(sequence)
            break
        else:
            i += 1  