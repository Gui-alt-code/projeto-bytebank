from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario, ano_que_entrou_na_empresa):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        self._ano_que_entrou_na_empresa = ano_que_entrou_na_empresa

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasciemnto_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    
    def _eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
            
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor
    
    def tempo_que_o_funcionario_esta_na_empresa(self):
        data_de_entrada = int(self._ano_que_entrou_na_empresa)
        data_atual = date.today().year
        return data_atual - data_de_entrada

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario}, {self._ano_que_entrou_na_empresa}, {self._ano_que_saiu_da_empresa})'