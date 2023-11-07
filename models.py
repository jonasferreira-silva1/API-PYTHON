class ProprietarioPet:
  def __init__(self, id, matricula, nome, cpf, telefone):
    self.id = id
    self.matricula = matricula
    self.nome = nome
    self.cpf = cpf
    self.telefone = telefone
  

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'matricula': self.matricula,
      'nome': self.nome,
      'cpf':self.cpf,
      'telefone':self.telefone
    }