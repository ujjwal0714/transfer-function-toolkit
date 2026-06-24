if __name__=="__main__":
    from polynomial import Polynomial

    def examples():
        p = Polynomial(coffs=[4,5,6])
        q = Polynomial(coffs=[0,1,2,3])
        r = Polynomial(coffs=[3,4,5,6,7])
        s = Polynomial(coffs=[1,2,3,4])

        return p,q,r,s

    p,q,r,s = examples()
    
    print ("p:", p)
    print ("q:", q)
    print ("p+q:", p+q)
    print ("p-q:", p-q)
    print ("p*q:", p*q)
    print ("2*q:", 2*q)
    print ("q*2:", q*2)

    print("\n")
    
    print ("r:", r)
    print ("s:", s)
    print ("r+s:", r+s)
    print ("r-s", r-s)
    print ("r*s:", r*s)
    print ("2*s:", 2*s)
    print ("s*2:", s*2)

