print("Exercício 5")
string = input("Insira uma string: ")

def reverseString(string):
    size = len(string)
    
    while size > 0:
        print(string[size - 1], end="")
    
        size -= 1
    
    print("\n")
    
reverseString(string)