name = {"BMW", "Toyota", "Huyndai", "Mazda"}

iterName = iter(name)

print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))


def myRange(stop, start = 0, step = 1):
    while start < stop:
        print("Generators: {}".format(start))
        yield start
        start+=step
        
for i in myRange(10):
    print(i)
        
# Tạo một generator expression để tạo ra các số chẵn từ 0 đến 10
even_numbers_generator = (x for x in range(11) if x % 2 == 0)

# Lặp qua generator và in ra các số chẵn
for number in even_numbers_generator:
    print(number)

