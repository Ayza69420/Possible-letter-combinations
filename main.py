def alg(n: str) -> str:
    x = [i for i in n]
    output = []

    for _ in range(len(n)):
        for i in range(1,len(n)):
            x[i-1], x[i] = x[i], x[i-1]
            
            output.append("".join(x))
    return output

print(alg("test"))