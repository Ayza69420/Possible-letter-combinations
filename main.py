def alg(n: str) -> list:
    x = [i for i in n]
    output = []

    for _ in range(len(n)):
        for i in range(1,len(n)):
            x[i-1], x[i] = x[i], x[i-1]
            
            output.append("".join(x))
    return output

print(alg("test")) # Pass the word as the argument and it's gonna return all the possible combinations of the word's letters.

# Amount of combinations = x * x-1 (x = length of alg(n))
