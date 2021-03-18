def main():
    cont = 1
    soma=0
    nota = input ("digite uma nota:")
    while nota!= 0:
        soma = nota+soma
        media = float (soma)/cont
        nota = input ("digite uma nota:")
        cont = cont + 1
    
    print media


if __name__ == "__main__":
    main()
