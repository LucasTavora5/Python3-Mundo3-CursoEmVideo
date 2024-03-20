'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time 'Vasco'.'''
cont = 0
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')
#lista de times
print('-=' * 50)
print(f'Lista de Times {times}')
print('-=' * 50)
#os 5 primeiros colocados
print(f'Os cinco primeiros colocados são:{times[0:5]}')
#Os últimos 4 colocados.
print(f'Os últimos 4 colocados são {times[16:21]}') #[-4] também serviria
#Times em ordem alfabética.
print(f'Times em órdem alfabétca: {sorted(times)}')
#posição do vasco
print(f'O vasco está na {times.index("Vasco")+1}ª posição')

