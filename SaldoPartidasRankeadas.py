# Instruções para entrega
#  # 2️⃣ Calculadora de partidas Rankeadas
# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

# ## Objetivo:

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

# Se vitórias for menor do que 10 = Ferro
# Se vitórias for entre 11 e 20 = Bronze
# Se vitórias for entre 21 e 50 = Prata
# Se vitórias for entre 51 e 80 = Ouro
# Se vitórias for entre 81 e 90 = Diamante
# Se vitórias for entre 91 e 100= Lendário
# Se vitórias for maior ou igual a 101 = Imortal

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

def saldo_e_nivel(v,d):
  saldo = v-d
  nivel = "None"
  if saldo < 10:
    nivel = "Ferro"
  elif saldo <= 20 and saldo >= 11:
    nivel = "Bronze"
  elif saldo <= 50 and saldo >= 21 :
    nivel = "Prata"
  elif saldo <= 80 and saldo >=  51:
    nivel = "Ouro"
  elif saldo <= 90 and saldo >=  81:
    nivel = "Diamante"
  elif saldo <= 100 and saldo >=  91:
    nivel = "Lendário"
  else:
    nivel = "Imortal"
  respostaFinal = "O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**".format(saldo = saldo, nivel = nivel)
  return respostaFinal

print(saldo_e_nivel(85,5))
  