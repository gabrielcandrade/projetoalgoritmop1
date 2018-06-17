#coding: utf-8

# Aluno: Gabriel de Carvalho Andrade - Matrícula: 1810021814
# Curso: Ciências da Computação - 1º Período

# Aplicação já preparada para rodar diretamente no ambiente do Windows para melhor correção do exercício.

# Função de tratamento do arquivo.

from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

# Main

print ("Digite o caminho do arquivo. Não esqueça que sua extensão deve ser .txt:\n")
caminho = input("")

print ('''
Parte 2 do exercício!''')

colocarEmPDF(trataTextos(caminho))
input()