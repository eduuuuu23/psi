from classe_projeto import EquipaApresentada
from classe_projeto import Equipa

jogadores_da_equipa = [
    {"nome": "Humberto Delgado", "idade": 40, "numero_da_camisa": 99, "posicao": "[C]GR-"},
    {"nome": "Jubiscreldo JR", "idade": 17, "numero_da_camisa": 69, "posicao": "DE-"},
    {"nome": "Elizeu Almeida", "idade": 32, "numero_da_camisa": 4, "posicao": "DC-"},
    {"nome": "Luva di abidisi", "idade": 22, "numero_da_camisa": 3, "posicao": "DC-"},
    {"nome": "Tiaguin da roci", "idade": 16, "numero_da_camisa": 28, "posicao": "DD-"},
    {"nome": "Duduzin", "idade": 16, "numero_da_camisa": 23, "posicao": "MC-"},
    {"nome": "Abreu Morreu", "idade": 35, "numero_da_camisa": 8, "posicao": "MC-"},
    {"nome": "Comedor de casadas", "idade": 20, "numero_da_camisa": 10, "posicao": "MCO-"},
    {"nome": "Rei das Baladas", "idade": 18, "numero_da_camisa": 11, "posicao": "EE-"},
    {"nome": "Anão", "idade": 17, "numero_da_camisa": 9, "posicao": "ED-"},
    {"nome": "Cristiano REInaldo JR", "idade": 39, "numero_da_camisa": 7, "posicao": "PL-"}
]
equipa = EquipaApresentada(jogadores_da_equipa)
print(equipa.apresentacao())
###################################################
clube = [
    {"nome": "Peixinhos FC", "idade": 100, "premios": "Champions League- 17\n Taças de Portugal- 20\n Campeonato- 119\n Taças de Liga- 21\n Mundial de clubes- 16\n Europe League- 3\n Conference League- 2\n Base- 200"},
]
clube = Equipa(clube)
print(clube.apresentacao_do_clube())