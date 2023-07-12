
# this function return only prime numbers
def prime_nmbr(x):
    count_prime_numbers = 0
    
    for i in range(1, x+1):
        count_modulos = 0
        for j in range(1, i):
            if i % j == 0:
                count_modulos += 1
            if count_modulos > 1:
                break
        if count_modulos <= 1:
            count_prime_numbers += 1
            print(i)
    
    return "\nCount of prime numbers between 1 and " + str(x) + " is: " + str(count_prime_numbers) + "\n"
