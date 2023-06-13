def numero_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return  True
    elif n > 2:
        for divisor in range(2, int(n ** 0.5) + 1):
                if n % divisor == 0:
                     return False
        return True
            
print(numero_primo(7))



