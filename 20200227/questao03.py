v1, v2, v3 = input("Três valores: ").split()
v1, v2, v3 = int(v1), int(v2), int(v3)

tri_ret = (v1 * v3) / 2
circulo = 3.14159 * v3**2
trap = ((v1 + v2) * v3) / 2
quad = v2**2
ret = v1 * v2

print(f"Triângulo Retângulo = {tri_ret}")
print(f"Círculo = {circulo}")
print(f"Trapézio = {trap}")
print(f"Quadrado = {quad}")
print(f"Retângulo = {ret}")