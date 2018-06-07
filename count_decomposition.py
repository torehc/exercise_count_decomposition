contador = 0

def contar_pasos(num_int,start=True):
    global contador
    if(start): contador = 0

    if(len(str(num_int))>1):
        resultado = multiplicar(num_int)
        contador += 1
        contar_pasos(resultado,start=False)

    return contador

def un_digito(num):
    if(len(list(str(num)))>1):
        return False
    else:
        return True

def multiplicar(num_int):
    product = 1
    for num in list(str(num_int)):
        product = product * int(num)
    return product


def main():

    print(contar_pasos(33))
    print(contar_pasos(135))

if __name__ == "__main__":
    main()