# -*- coding: latin-1 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import psycopg2
from config import *
import requests
from flask_cors import CORS, cross_origin
from collections import OrderedDict 
import hashlib
from hashlib import md5
import requests
import json



import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()



app = Flask(__name__)
api = Api(app)
CORS(app)





# http://127.0.0.1:5002/perfil/<id_aluno>
class CursoPerfil(Resource):
	def get(self,id_aluno):
		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()
		query = cur.execute(("select nome_curso,carga_horaria,data_criacao,qtd_horas_extras,descricao,id_coordenador from aluno a, curso c where a.id_aluno = %i and c.id_curso = a.id_curso")%int(id_aluno))
		result = cur.fetchall()

		values = []
		for i in result[0]:
			values.append(i)

		session = requests.session()

		coord = session.get('http://dev2.unifacef.com.br:8000/api/docente/'+str(values[5]))
		coord = json.loads(coord.text)

		keys = ['nome_curso','carga_horaria','data_criacao', 'qtd_horas_extras', 'descricao','nome_coordenador']

		result = OrderedDict(zip(keys,values))
		result.update({'nome_coordenador':coord[0]['nome_docente']})


		return jsonify(result)


class alunoSession(Resource):
	def get(self,id_aluno):
		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()

		query = cur.execute("select nome_aluno,id_aluno,nome_curso from aluno a, curso c where a.id_aluno = %i and a.id_curso = c.id_curso"%int(id_aluno))
		keys = ['nome_aluno','id_aluno','nome_curso']

		result = cur.fetchall()

		values = []
		for i in result[0]:
			values.append(i)


		result = OrderedDict(zip(keys,values))


		return jsonify(result)


class insereAtividade(Resource):
	def post(self,nome_atividade,local_atividade,data_atividade,categoria,fornecido,descricao,imagem):
		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()


		horas_ativ = 0
		result = cur.execute("insert into atividades(nome_atividade,id_evento,tipo_atividade,horas,fornecido,data_atividade,ds_evento) values ('%s',0,'%s',%i,%s,'%s','%s')"%(nome_atividade,categoria,horas_ativ, fornecido,data_atividade,descricao))
		conn.commit()

		cur.close()
		conn.close()
		file = open('C:\\Users\\vitor\\Desktop\\TIC-2018\\TESTE.png','w')
		print imagem
		image  = plt.imsave('C:\\Users\\vitor\\Desktop\\TIC-2018\\TESTE.png', np.array(imagem), cmap=cm.gray)

		print image
		
		print result
		return result






class dadosChart(Resource):
	def get(self, id_aluno):
		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()

		query = cur.execute("select horas,qtd_horas_extras from aluno a, curso c where a.id_aluno = %i and a.id_curso = c.id_curso"%int(id_aluno))
		keys = ['horas_aluno','horas_totais']

		result = cur.fetchall()

		values = []
		for i in result[0]:
			values.append(i)


		result = OrderedDict(zip(keys,values))


		return jsonify(result)	


class validaUsuario(Resource):
	def get(self, usuario,senha):
		conn = psycopg2.connect(host="localhost",database="DaHora", user="postgres", password="1234")
		cur = conn.cursor()
		senha = computeMD5hash(str(senha))



		quer = '''
		select count(*)
		from(
		  select id_aluno
		  from aluno
		  where id_aluno = %i
		) as search
		'''%int(usuario)


		quer2 = '''
		select id_aluno, senha from aluno where id_aluno = %i
		'''%int(usuario)

		try:
			query = cur.execute(quer)
			numero_usuarios = cur.fetchall()

			if numero_usuarios[0][0] > 0:
				query = cur.execute(quer2)
				result = cur.fetchall()


				if str(result[0][0]) == str(usuario) and result[0][1] == senha:
					print "LOGIN AUTENTICADO"
					return True

				else:
					print "LOGIN OU SENHA INVÁLIDOS."
					return False
				
			else:
				return False

		except Exception as err:
			print "LOGIN OU SENHA INVÁLIDOS."
			return False


		



class principal(Resource):
	def get(self):
		Arquivo = {
		'encontra dados do aluno': '/<id_aluno>',
		'valida o usuário no BD':'/login/<usuario>.<senha>',
		'dados para o gráfico 1':'/chart/<id_aluno>',
		'principal':'/',
		'insere Atividade': '/insere/<nome_atividade>.<local_atividade>.<data_atividade>.<categoria>.<fornecido>.<descricao>.<imagem>',
		'verifica o perfil completo de um aluno':'/perfil/<id_aluno>',
		}

		
		return Arquivo
		


api.add_resource(alunoSession, '/<id_aluno>')
api.add_resource(validaUsuario,'/login/<usuario>.<senha>')
api.add_resource(dadosChart,'/chart/<id_aluno>')
api.add_resource(principal,'/')
api.add_resource(insereAtividade, '/insere/<nome_atividade>.<local_atividade>.<data_atividade>.<categoria>.<fornecido>.<descricao>.<imagem>')
api.add_resource(CursoPerfil, '/perfil/<id_aluno>')




if __name__ == '__main__':
	 app.run(port='5002')