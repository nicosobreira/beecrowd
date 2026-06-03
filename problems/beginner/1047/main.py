hi, mi, hf, mf = map(int, input().split())

delta = (hf * 60 + mf) - (hi * 60 + mi)

if delta <= 0:
    delta += 1440  # 24h * 60min

print(f"O JOGO DUROU {delta // 60} HORA(S) E {delta % 60} MINUTO(S)")

# 1. Eliminação das variáveis auxiliares aumenta a velocidade na digitação
# 2. Identificar que `delta <= 0` é equilvalente a `m_inicial >= m_final`

"""
m_inicial = hi * 60 + mi
m_final = hf * 60 + mf

if m_inicial >= m_final:
    delta = (24 * 60) + m_final - m_inicial
else:
    delta = m_final - m_inicial

horas = delta // 60
minutos = delta % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
"""
