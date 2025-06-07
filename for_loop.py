# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# import random

# scores = [random.randint(0, 50) for _ in range(10)]
scores = [8, 11, 48, 5, 13, 14, 25, 48, 12, 11]
# print(scores)
# print("El maximo valor de la lista es:")
# print(max(scores))

max_score = 10

while max_score < 50:
    max_score += 1
    print(max_score)
    if max_score == 25:
        print("Breaking the loop")
        break
    else:
        print("Continuing the loop")
        continue

# for score in scores:
#     if score > max_score:
#         max_score = score
    
# print(f"El maximo valor de la lista es: {max_score}")