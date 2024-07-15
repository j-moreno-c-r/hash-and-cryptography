
def main():
    g=5 # publicly known
    x=7 # only Alice knows this 
    y=3 # only Bob knows this
    aliceSends = (g**x)
    bobSends = (g**y)
    aliceComputes = (bobSends**x)
    bobComputes = (aliceSends**y)
    bobSends = (g**y)
    bobComputes = (aliceSends**y) 
    print (f"Alice sends: 💌 {aliceSends}")
    print (f"Bob sends: 💌 {bobSends} ")
    print (f"Bob computes: ✏️ {bobComputes}")
    print (f"Alice computes:✏️ {aliceComputes}")
main()

