from datetime import date

# CLASSE ENDEREÇO
class Endereco:
    def __init__(self, logradouro='', numero='', endereco_comercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial

# CLASSE PESSOA
class Pessoa:
    def __init__(self, nome='', rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco if endereco is not None else Endereco()

    def calcular_imposto(self):
        return self.rendimento

# CLASSE PESSOA FÍSICA
class PessoaFisica(Pessoa):
    def __init__(self, nome='', rendimento=0.0, endereco=None, cpf='', data_nascimento=None):
        if endereco is None:
            endereco = Endereco()
        
        if data_nascimento is None:
            data_nascimento = date.today()

        super().__init__(nome, rendimento, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def calcular_imposto(self, rendimento: float) -> float:
        # sem imposto para rendimentos até 1500
        if self.rendimento <= 1500:
            return 0
        # 2% de imposto para rendimento entre 1500 e 3500
        elif 1500 < self.rendimento <= 3500:
            return (self.rendimento - 1500) * 0.02
        # 3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3500 < self.rendimento <= 6000:
            return (self.rendimento - 3500) * 0.035 + (3500 - 1500) * 0.02
        # 5% de imposto para rendimentos acima de 6000
        else:
            return (self.rendimento - 6000) * 0.05 + (6000 - 3500) * 0.035 + (3500 - 1500) * 0.02

# CLASSE PESSOA JURÍDICA
class PessoaJuridica(Pessoa):
    def __init__(self, nome='', rendimento=0.0, endereco=None, cnpj=''):
        super().__init__(nome, rendimento, endereco)
        self.cnpj = cnpj
        if endereco is None:
            endereco = Endereco()     
    
    def calcular_imposto(self, rendimento: float) -> float:

        # sem imposto para rendimentos até 55000
        if self.rendimento <= 55000:
            return 0
        # 2% de imposto para rendimento entre 55000 e 75000
        elif 1500 < self.rendimento <= 75000:
            return (self.rendimento - 55000) * 0.02
        # 3.5% de imposto para rendimentos entre 75000 e 90000
        elif 3500 < self.rendimento <= 6000:
            return (self.rendimento - 75000) * 0.035 + (75000 - 55000) * 0.02
        # 5% de imposto para rendimentos acima de 90000
        else:
            return (self.rendimento - 90000) * 0.05 + (9000 - 55000) * 0.035 + (75000 - 55000) * 0.02
    

