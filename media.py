
def main():
    N = input ("quantas notas deseja calcular a media?")
    print media (N)
def media (N):
    cont = 1
    soma=0
    while cont <= N:
        nota = input ("digite uma nota:")
        soma = nota+soma
        cont = cont + 1
    media = float(soma/N)
    
    return media


if __name__ == "__main__":
    main()
