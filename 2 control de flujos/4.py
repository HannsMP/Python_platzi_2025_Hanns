list = [1, 2, 3, 4]

list_iter = iter(list)

print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

text = "hola mundo"

text_iter = iter(text)

print(next(text_iter))
print(next(text_iter))
print(next(text_iter))
print(next(text_iter))

limit = 10

odd_iter = iter(range(1, limit + 1, 2))

print(next(odd_iter))
print(next(odd_iter))
print(next(odd_iter))
print(next(odd_iter))