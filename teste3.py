#ex3

def trapezio(B,b,h):
    return (B+b)*h/2.0

def main():
    B = input("Digite a base maior:")
    b = input("Digite a base menor:")
    h = input("Digite a altura:")
    print "A �rea do trap�zio � %.2f" %(trapezio(B,b,h))

if __name__ =="__main__":
    main()
