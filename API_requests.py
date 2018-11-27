import requests
import psycopg2
import json
import pprint

for i in range(16000,99999):
	url = 'http://dev2.unifacef.com.br:8000/api/matriculadoGrad/'+str(i)
	session = requests.session()
	teste = session.get(url)
	
	organiza = 	json.loads(teste.text)
	if organiza:
		with open('C:\\Users\\vitor\\Desktop\\TIC-2018\\files\\aluno_'+str(organiza[0]['id_aluno']) +'.json', 'w') as file:
			json.dump(organiza, file)
			print 'Aluno '+ str(organiza[0]['id_aluno']) +' salvo'