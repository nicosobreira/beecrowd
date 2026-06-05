dia_i = int(input().replace("Dia", ""))
h_i, m_i, s_i = map(int, input().replace(":", " ").split())

dia_f = int(input().replace("Dia", ""))
h_f, m_f, s_f = map(int, input().replace(":", " ").split())

segundos_i = dia_i * 24 * 60 * 60 + h_i * 60 * 60 + m_i * 60 + s_i

segundos_f = dia_f * 24 * 60 * 60 + h_f * 60 * 60 + m_f * 60 + s_f

total = segundos_f - segundos_i

# PRECISO DOS PARÊNTESES!
print(f"{total // (24 * 60 * 60)} dia(s)")
total %= 24 * 60 * 60

print(f"{total // (60 * 60)} hora(s)")
total %= 60 * 60

print(f"{total // 60} minuto(s)")
total %= 60

print(f"{total} segundo(s)")

"""
tempo_i = h_i * 60 * 60 + m_i * 60 + s_i

tempo_f = h_f * 60 * 60 + m_f * 60 + s_f

delta = tempo_f - tempo_i

if delta < 0:
    delta += 24 * 60 * 60

delta += (dia_f - dia_i) * 24 * 60 * 60

print(f"{delta // 24*60*60} dia(s)")
"""
