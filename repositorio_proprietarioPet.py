from conexao_bd import getConnectionPostegre
from models import ProprietarioPet


def getDados():
    conn = getConnectionPostegre()
    cursor = conn.cursor()
    cursor.execute("SELECT id,matricula,nome,cpf,telefone FROM proprietarioPet")
    rows = cursor.fetchall()
    result = []
    for i in rows:
        proprietarioPet = ProprietarioPet(i[0], i[1], i[2], i[3],i[4])
        #print ("ID: {} Matricula: {} Nome: {} CPF: {} Telefone: {}".format(i[0], i[1], i[2], i[3],i[4]))
        result.append(proprietarioPet.serialize())
    conn.close()
    return result

#print (getDados())
   
def insert(matricula, nome, cpf, telefone):
    conn = getConnectionPostegre()
    cur = conn.cursor()
    cur.execute("INSERT INTO aluno(	matricula, nome, cpf, telefone)	VALUES ( %s,%s,%s,%s)", (
        matricula,
        nome,
        cpf,
        telefone
    ))
    conn.commit()
    conn.close()
#insert(3,'Maga','456798','121212')
#print("Aluno cadastrado!")


def update(id, matricula, nome, cpf, telefone):
    conn = getConnectionPostegre()
    cur = conn.cursor()
    cur.execute("UPDATE proprietarioPet SET matricula=%s, nome=%s, cpf=%s, telefone=%s WHERE id = %s", (
        matricula,
        nome,
        cpf,
        telefone,
        id
    ))
    conn.commit()
    conn.close()
#update(6, 3,'Maga atualizada','654321','333333')
#print("Dados atualizados!")


def delete(id):
    conn = getConnectionPostegre()
    cur = conn.cursor()
    cur.execute("DELETE FROM aluno WHERE id = %s", (
        id,
    ))
    conn.commit()    
#delete(6)
#print("Dados removidos!")

def getProprietarioPetId(id):
    conn = getConnectionPostegre()
    cursor = conn.cursor()
    cursor.execute("select * FROM aluno WHERE id = %s", (
        id,
    ))
    rows = cursor.fetchall()
    proprietarioPet = ProprietarioPet(0, 0, '', '','')
    for i in rows:
        proprietarioPet = ProprietarioPet(i[0], i[1], i[2], i[3],i[4])
    conn.close()
    return proprietarioPet