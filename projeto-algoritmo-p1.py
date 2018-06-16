#coding: utf-8

# Aluno: Gabriel de Carvalho Andrade - Matrícula: 1810021814
# Curso: Ciências da Computação - 1º Período

# Aplicação ja preparada para rodar diretamente no ambiente do Windows para melhor correção do exercício.



from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Função de tratamento do arquivo.

def trataTextos(diretorio):
	# Trata o diretorio de entrada para pegar apenas o arquivo .txt
	listaDeCaminhos = diretorio.split('/')
	arquivo = listaDeCaminhos[len(listaDeCaminhos)-1]
	
	# Abre o arquivo .txt e trata os caracteres especiais inseridos dentro dele.
	arquivo = open(arquivo, 'r')
	listaDeConvidados = []
	dicionario = {}
	for linha in arquivo:
		novaLinha = str(linha)
		tratarLinha = novaLinha.replace('#', ' ').replace('--', ' ').replace('\n', ' ').split(' ')
		for i in tratarLinha:
			if (i != ''):
				listaDeConvidados.append(i)

	# Reagrupa cada nome em uma lista e cada telefone em outra lista.			
	listaDeNomes = []
	listaDeTelefones = []
	for i in listaDeConvidados:
		if (listaDeConvidados.index(i) % 2):
			listaDeTelefones.append(i)
		else:
			listaDeNomes.append(i)

	# Cria um dicionário e coloca telefone como chave e nome como valor.
	dicionario = {}
	for (nome, telefone) in zip(listaDeNomes, listaDeTelefones):
		dicionario[telefone] = nome
	
	# Fecha o arquivo e retorna o dicionário.
	arquivo.close()
	print()
	return dicionario

# Função de conversão de um dicionario para um arquivo .pdf

def colocarEmPDF (dicionario):
	# Recebe o dicionário
	convidados = dicionario

	# Cria um arquivo chamado 'convidados.pdf'
	doc = canvas.Canvas('convidados.pdf')

	# Nesse pixel de linha e coluna (padrão) coloca as informações.
	coluna = 80
	linha = 800

	# Escreve na linha e coluna definida a informação: 'Nomes e telefones'
	doc.drawString(coluna, linha, 'Nomes e Telefones')

	# Vai escrevendo linha abaixo de linha as informações de nome e telefone respectivamente.
	for convidado in convidados:
		linha -= len(convidados)
		contato = convidados[convidado] + ':' + convidado
		doc.drawString(coluna, linha, contato)
	
	# Salva o documento, possibilitando o acesso ao arquivo.
	doc.save()
	print ("Arquivo salvo com sucesso!")
	print ()
	print ("O arquivo .pdf se encontra no mesmo lugar que o arquivo .txt")

# Função de enviar e-mail automaticamente.

def enviarEmail():
	fromaddr = "gca.evl@gmail.com"
	toaddr = "app.p1.unipe@gmail.com"

	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr

	#Assunto
	msg['Subject'] = "Contatos - Gabriel de Carvalho Andrade"

	#Corpo do texto 
	body = "Segue os contatos em anexo!"

	msg.attach(MIMEText(body, 'plain'))

	#Anexo 
	filename = "convidados.pdf"
	attachment = open(filename, "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "@#Gabriel159")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)

	print ("E-mail enviado com sucesso!")

	server.quit()

# Interface do sistema

print ('''
	#####################################################
	#                                                   #
	#                                                   #
	#       Bem vindo à primeira parte do Projeto       #
	#                                                   #
	#   Aluno: Gabriel de Carvalho Andrade              #
	#   Curso: Ciências da Computação - 1º Período      #
	#   Matrícula: 1810021814                           #
	#                                                   #
	#                                                   #
	#     Esse aplicativo é responsável por tratar      #
	#   um texto de extensão .txt com as informações    #
	#   de nome e telefone, referente à lista de con-   #
	#   vidados e transformar em um arquivo .pdf        #
	#                                                   #
	#                                                   #
	#####################################################
''')

# Primeira parte do exercício.

print ("Digite o caminho do arquivo. Não esqueça que sua extensão deve ser .txt:\n")
caminho = input("")

print ("Parte 1 do exercício!")
print ()
print (trataTextos(caminho))

# Segunda parte do exercício.

print ("Parte 2 do exercício!")
print ()
colocarEmPDF(trataTextos(caminho))

# Terceira parte do exercício.

print ("Parte 3 do exercício!")
print ()
enviarEmail()
