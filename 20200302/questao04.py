inicio, fim = input().split()

di, mi, ai = inicio.split('/')
df, mf, af = fim.split('/')

di, mi, ai = int(di), int(mi), int(ai)
df, mf, af = int(df), int(mf), int(af)

dias_i = di + mi * 30 + ai * 365
dias_f = df + mf * 30 + af * 365

print(dias_f - dias_i + 1)