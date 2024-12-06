
# #equipa de futebol ou outro desporto
class EquipaApresentada:
    def __init__(self, jogadores_da_equipa):
        self.jogadores_da_equipa = jogadores_da_equipa
    def apresentacao(self):
        apresentacoes = []
        # Criando uma apresentação para cada jogador na lista
        for jogador in self.jogadores_da_equipa:
            apresentacoes.append(f"{jogador["posicao"]}{jogador["nome"]}, {jogador["idade"]} anos, número {jogador["numero_da_camisa"]}")
        return "\n".join(apresentacoes)

class Equipa:
    def __init__(self, clube):
        self.clube = clube
    def apresentacao_do_clube(self):
        apresentacao = []
        
        for equipa in self.clube:
            apresentacao.append(f"O clube tem:{clube["premios"]} prêmios.\n O nome do clube é{clube["nome"]}, e tem{clube["idade"]} anos")
        return "\n".join(apresentacao)