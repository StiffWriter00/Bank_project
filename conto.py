class Conto:
    
    def __init__(self, bilancio_conto, numero_conto, saldo = 0):
        self.bilancio_conto = bilancio_conto
        self.numero_conto = numero_conto
        self.saldo = saldo
        operazioni_effettuate = []
        
    def __repr__(self):
        return "Conto({0}, {1}, {2})".format(self.bilancio_conto, self.numero_conto, self.saldo)