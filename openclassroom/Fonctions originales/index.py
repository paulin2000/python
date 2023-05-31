# Variable globale
a = 15
def monter():
 global a
 a = a+1
 print(a)
monter() #16
monter() #17
print (a) #17

