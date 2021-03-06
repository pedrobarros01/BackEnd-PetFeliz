from sql_alchemy import banco


class ClienteModel(banco.Model):
    __tablename__ = 'TB_CLIENTE'
    cpf = banco.Column(banco.String(12), primary_key=True)
    nome = banco.Column(banco.String(100))
    rg = banco.Column(banco.String(8))
    telefone = banco.Column(banco.String(20))
    endereco = banco.Column(banco.String(120))
    email = banco.Column(banco.String(50))
    senha = banco.Column(banco.String(74))
    nivel = banco.Column(banco.String(80))
    quantidade_gasta = banco.Column(banco.Float(precision=2))
    creditos = banco.Column(banco.Float(precision=2))
    pets = banco.relationship('PetModel')

    def __init__(self, cpf, nome, rg, telefone, endereco, email, senha, creditos):
        self.cpf = cpf
        self.nome = nome
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.nivel = 'Sem nível'
        self.quantidade_gasta = 0
        self.creditos = creditos

    @classmethod
    def encontrar_cliente_por_cpf(cls, cpf):
        cliente = cls.query.filter_by(cpf=cpf).first()
        if cliente:
            return cliente
        return None
    
    @classmethod
    def encontrar_cliente_por_rg(cls, rg):
        cliente = cls.query.filter_by(rg=rg).first()
        if cliente:
            return cliente
        return None

    @classmethod
    def encontrar_cliente_por_email(cls, email):
        cliente = cls.query.filter_by(email=email).first()
        if cliente:
            return cliente
        return None

    def get_senha(self):
        return self.senha

    def get_cpf(self):
        return self.cpf

    def get_quantidade_gasta(self):
        return self.quantidade_gasta

    
    def salvar_cliente(self):
        banco.session.add(self)
        banco.session.commit()

    def deletar_cliente(self):
        [pet.deletar_pet() for pet in self.pets]
        banco.session.delete(self)
        banco.session.commit()
    
    def atualizar_cliente(self, nome, rg, telefone, endereco, email, senha, creditos, cpf='', quantidade_gasta=0):
        self.cpf = cpf
        self.nome = nome
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.creditos = creditos
        self.quantidade_gasta = quantidade_gasta

    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'rg': self.rg,
            'telefone': self.telefone,
            'endereço': self.endereco,
            'email': self.email,
            'senha': self.senha,
            'nível': self.nivel,
            'quantidade_gasta': self.quantidade_gasta,
            'creditos': self.creditos,
            'pets': [pet.json() for pet in self.pets]
        }

