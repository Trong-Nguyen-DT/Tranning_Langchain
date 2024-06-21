def hamMu(n):
    return lambda x:x**n

hamMu2 = hamMu(2)
hamMu3 = hamMu(3)

print("ham mu 2 cua 3: " + str(hamMu2(3)))
print("ham mu 3 cua 3: " + str(hamMu3(3)))