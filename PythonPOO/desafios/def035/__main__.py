from def035 import *

def main():
    a1 = PDF("documento", 10_000_000)
    a2 = DOC("documento", 2_000_000)
    
    print(a1)
    print(a2)
    
    a1.abrir()
    a2.abrir()


if __name__ == "__main__":
    main()