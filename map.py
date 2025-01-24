def mifuncion(n):
    return len(n)

print(len("Valerntina"))

x = map(mifuncion, ("Manzana", "Banano", "Cereza"))

for i in x:
    
    print(i)

print(x)
