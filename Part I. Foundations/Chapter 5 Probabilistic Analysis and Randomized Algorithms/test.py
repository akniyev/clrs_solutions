product = 1
i = 1

while product > 0.5:
    product *= (365.0 - i) / 365.0
    i += 1

print(product, i)
