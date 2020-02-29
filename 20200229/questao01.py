h, m, s = input("Tempo: ").split(":")
h, m, s = int(h), int(m), int(s)

tempo = (h * 3600) + (m * 60) + s

print(f"Tempo = {tempo}")