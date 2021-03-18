#ex 2

def media(x,y):
    return (x+y)/2.0


def main():
    nome1 = raw_input("Digite o primeiro nome:")
    idade1 = input("Digite a primeira idade:")
    nome2 = raw_input("Digite o segundo nome:")
    idade2 = input("Digite a segunda idade:")
    print "A primeira pessoa se chama %s e tem %d anos." %(nome1,idade1)
    print "A segunda pessoa se chama %s e tem %d anos." %(nome2,idade2)
    print "A média das idades é %.1f" %(media(idade1,idade2))

if __name__ =="__main__":
    main()
