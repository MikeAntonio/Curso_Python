#!/usr/bin/env python
# coding: utf-8

# In[30]:


import sqlite3

banco = sqlite3.connect('empresa_modulo3.db')


# In[31]:


cursor = banco.cursor()


# In[48]:


cursor.execute('''CREATE TABLE funcionarios (
codigo integer PRIMARY KEY NOT NULL, 
primeiroNome text NOT NULL, 
segundoNome text NOT NULL, 
ultimoNome text NOT NULL, 
DataNasci text NOT NULL, 
CPF integer NOT NULL, 
RG text NOT NULL, 
Endereco text NOT NULL, 
CEP text NOT NULL, 
Cidade text NOT NULL, 
Fone integer NOT NULL, 
codigoDepartamento integer NOT NULL, 
funcao text NOT NULL, 
salario integer NOT NULL);''')

cursor.execute('''CREATE TABLE departamentos(
codigo integer PRIMARY KEY NOT NULL,
nome text NOT NULL,
localizacao NOT NULL,
codigoFuncionarioGerente NOT NULL);''')




# In[6]:


cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())


# In[49]:


lista_funcionarios = [('2', 'Jose', 'Lucas', 'Santos', '1998-01-26', '27643428177', '453456292X', 'Augusta 38', '0564304', 'Sao Paulo', '11934356789', '1', 'Analista Sistemas SR', '12000'),
                     ('3', 'Fernando', 'Henrique', 'Hideki', '1999-02-26', '27645828177', '4534345292X', 'Av Paulista 356', '0564304', 'Sao Paulo', '11934356789', '1', 'Analista Sistemas SR', '12000'),
                     ('4', 'Cleiton', 'Leonardo', 'Gomes', '2001-04-26', '276345828177', '4534565292X', 'Av Gomes sales 383', '0564304', 'Osaco', '11934356789', '1', 'Analista Sistemas PL', '8000'),
                     ('5', 'Lourenco', 'Lucas', 'Santos', '2005-03-26', '27687828177', '45342345292X', 'Av Teoro 238', '0564304', 'Osasco', '11934356789', '2', 'Analista Financeiro JR', '2000'),
                     ('6', 'Jenivalda', 'Celia', 'Silva', '1979-12-26', '2763654828177', '4523345292X', 'Av JARDIM 4338', '0564304', 'Santana', '11934356789', '2', 'Analista Financeiro PL', '8000'),
                     ('7', 'Alcione', 'Lucia', 'Sales', '1999-05-26', '27665848177', '4534524292X', 'Av cRUZEIRO 5438', '0564304', 'Santana', '11934356789', '1', 'Analista Sistemas PL', '12000'),
                     ('8', 'Marcelo', 'Matheus', 'Watanabe', '2008-10-26', '27640828177', '4542345292X', 'Av Sampolioa 3438', '0564304', 'Sao Paulo', '11934356789', '2', 'Analista Sistemas JR', '1000'),
                     ('9', 'Ludmila', 'Luana', 'Rocha', '1972-01-26', '2764084658177', '4534534292X', 'Av Guedes 3428', '0564304', 'Sao Paulo', '11934356789', '1', 'Analista Sistemas SR', '12000'),
                     ('10', 'Eloisa', 'Nathalia', 'Santos', '2000-09-26', '2767540828177', '4345345292X', 'Av Ilinoia 338', '0564304', 'Braganca', '11934356789', '4', 'Analista Suporte SR', '12000'),
                     ('11', 'Monica', 'Julia', 'Silva', '1983-10-26', '276408238177', '4534345292X', 'Av Los angeles 838', '0564304', 'Sao Paulo', '11934356789', '4', 'Analista Suporte PL', '8000'),
                     ('12', 'Fabiano', 'Matheus', 'Santos', '1994-07-26', '276540828177', '245345292X', 'Av Orlando 438', '0564304', 'Bragança', '11934356789', '3', 'Analista InfraCloud PL', '2000'),
                     ('13', 'Paulo', 'Henrique', 'Sales', '2005-06-26', '276460828177', '445345292X', 'Av Serra 38', '0564304', 'Sao Paulo', '11934356789', '3', 'Analista InfraCloud SR', '8000')
                     ]
cursor.executemany("""INSERT INTO funcionarios VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", lista_funcionarios)
banco.commit()


# In[56]:


lista_departamento = [('1', 'TI', '13 Andar', '1' ),
                      ('2', 'Financeiro', '12 Andar', '2' ),
                      ('3', 'Infraestrutura', '11 Andar', '1' ),
                      ('4', 'Suporte TI', '10 Andar', '1' )]
cursor.executemany("""INSERT INTO departamentos VALUES (?,?,?,?)""", lista_departamento)
banco.commit()


# In[41]:


#A
cursor.execute('''SELECT primeiroNome, segundoNome FROM funcionarios ORDER BY segundoNome ''')
print(cursor.fetchall())


# In[22]:


#B
cursor.execute('''SELECT * FROM funcionarios ORDER BY cidade ''')
print(cursor.fetchall())


# In[42]:


#C
cursor.execute('''SELECT primeiroNome FROM funcionarios WHERE salario > 1000 ''')
print(cursor.fetchall())


# In[51]:


#D
cursor.execute('''SELECT DataNasci, primeiroNome FROM funcionarios ORDER BY DataNasci DESC; ''')
print(cursor.fetchall())


# In[52]:


#E
cursor.execute('''SELECT SUM(salario) FROM funcionarios ''')
print(cursor.fetchall())


# In[61]:


#F
cursor.execute('''SELECT a.primeiroNome, b.nome, a.funcao FROM funcionarios a INNER JOIN departamentos b ON a.codigoDepartamento = b.codigo  ''')
print(cursor.fetchall())


# In[63]:


#G
cursor.execute('''SELECT COUNT(*) FROM funcionarios ''')
print(cursor.fetchall())


# In[69]:


#H
cursor.execute('''SELECT b.nome, a.primeiroNome FROM funcionarios a INNER JOIN departamentos b ON a.codigoDepartamento = b.codigo ORDER BY b.nome, a.primeiroNome''')
print(cursor.fetchall())

