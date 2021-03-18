'''
1. Uma pista de Kart permite 10 voltas para cada um dos 6 corredores. 
Faça um programa que leia todos os tempos em segundos e guarde em uma 
matriz 6 x 10. Ao final diga:
• De quem foi a melhor volta da prova, com qual tempo e em que volta?
• Qual o campeão, considerando a média dos tempos de todas as voltas?
'''



def main():

    matriz = []
    for i in range(2):
        linha = []
        menorI=0
        for j in range(4):
            t = input("Digite o tempo %d do corredor %d: " %(j+1,i+1))
            linha+=[t]
            menorL = min(linha)
            if menorL>menorI:
                menorI=menorL
        matriz+=[linha]
        
        
    
#Imprimindo matriz
    for i in range(2):
        for j in range (4):
            print matriz[i][j],
        print
    print menorL
    
    

if __name__ == "__main__":
    main()

