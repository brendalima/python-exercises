#1. Faça um programa que guarde o nome e o telefone de seus
#amigos. Apresente as seguintes opções:
#(a) inserir o telefone de um amigo
#(b) consultar o telefone de uma pessoa dado seu nome.
#(c) para finalizar o programa


def main():
    lista=[]
    x=0
    while x != "c":
        x=raw_input("Digite: \n(a) inserir o telefone de um amigo \n(b) consultar o telefone de uma pessoa dado seu nome \n(c) para finalizar o programa")
        
        if x=="a":
            n=raw_input("Digite o nome:")
            m=input("digite o numero:")
            lista=lista+[[n,m]]
        elif x=="b":
            n=raw_input("Digite o nome:")
            for p in lista:
                if p[0]==n:
                    print p[1] 
                    
                
            
            
        
if __name__ == "__main__":
    main()

