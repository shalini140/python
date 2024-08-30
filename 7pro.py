def pythagorean_triples(limit):
    return [(a, b, int((a**2 + b**2)**0.5)) 
            for a in range(1, limit) 
            for b in range(a, limit) 
            if (a**2 + b**2)**0.5 < limit and (a**2 + b**2)**0.5 == int((a**2 + b**2)**0.5)]

limit = 20
print(pythagorean_triples(limit))
