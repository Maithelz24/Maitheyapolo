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

def num_pri(m):
     if m == 1 or m == 0:
          return False
     elif m == 2:
          return True
     elif m > 2:
          for d in range(2, m):
               if m % d == 0:
                    return False
               elif m % d != 0 and d == m-1:
                    return True
print(num_pri(7))


print(numero_primo(7))

def todos_los_primos(n):
     primos = []
     for m in range(2, n+1):
          s_primo = True
          for divisor in range(2, int(m ** 0.5) + 1):
               if m % divisor == 0:
                    s_primo = False
                    break
          if s_primo:
               primos.append(m)
     return primos
print(todos_los_primos(20))

print("holi")



