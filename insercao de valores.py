from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import psycopg2
from config import *

import os
import json

#C:\Users\vitor\Desktop\TIC-2018\files


import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()



diretorio = 'C:\\Users\\vitor\\Desktop\\TIC-2018\\files\\'



def insereAluno():
	for filename in os.listdir(diretorio):
		file = open(diretorio + filename, 'r')
		arq = json.load(file)
		arq = arq[0]
		senha = arq['cpf'].replace('.','')
		senha = senha.replace('-','')
		senha = senha[0:6]
		senha = computeMD5hash(senha)
		senha = str(senha)

		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()
		cur.execute("insert into aluno(id_aluno,id_curso, nome_aluno,login_,senha,horas,quant_eventos) values (%s,%s,%s,%s,%s,0,0)"%(arq['id_aluno'], arq['id_curso'], "'"+arq['sobrenome_aluno'].replace("'","*")+"'", "'"+str(arq['id_aluno'])+"'","'"+senha+"'"))

		conn.commit()

		cur.close()
		conn.close()

		print 'aluno:',arq['id_aluno'],'adicionado'


def insereCurso():
	for filename in os.listdir(diretorio):
		file = open(diretorio + filename, 'r')
		arq = json.load(file)
		arq = arq[0]

		try:
			conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
			cur = conn.cursor()
			cur.execute("insert into curso(id_curso, nome_curso, carga_horaria, data_criacao, qtd_horas_extras, descricao) values (%s,%s,3200,'01/01/2010',180,%s);"%(arq['id_curso'], "'"+arq['nome_curso']+"'", "'"+arq['nome_curso']+"'"))

			conn.commit()

			cur.close()
			conn.close()
			print 'curso: '+arq['nome_curso']+' adicionado'

		except Exception as err:
			# print err
			print 'curso existente'
			pass



insereCurso()

insereAluno()