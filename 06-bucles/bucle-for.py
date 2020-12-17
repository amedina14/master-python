"""
#For
for variable in elemento_iterable
    instruzioni
"""

c = 0
somma = 0
for i in range(0,10):
    #i+=1
    print("iterazione: "+str(i)+"\tsomma ("+str(somma)+") + i:"+str(somma+i))
    #somma=c+i
    somma+=i
print("somma totale",somma)
