class Banca:
    
    def __init__(self, nome_banca):
        self.nome_banca = nome_banca
        clienti = []
        conti_correnti = []
    
    def __repr__(self):
        return "Banca({0})".format(self.nome_banca)