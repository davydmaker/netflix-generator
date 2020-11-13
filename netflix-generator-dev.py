# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint
import random
import time

__author__ = "Davyd Maker"
__version__ = "2.1"

browser = 'Chrome'
emailHosts = ['moakt.ws', 'mohmal.com', 'divismail.ru', 'sharklasers.com', 'guerrillamail.info', 'grr.la', 'guerrillamail.biz', 'guerrillamail.com', 'guerrillamail.de', 'guerrillamail.net', 'guerrillamail.org', 'guerrillamailblock.com', 'spam4.me', 'kismail.ru', 'extremail.ru']
nomes = ['Bertlas', 'Helena', 'Ewise', 'Miguel', 'Ruthbri', 'Alice', 'Freamond', 'Arthur', 'Wigfled', 'Laura', 'Sephra', 'Heitor', 'Markcrow', 'Manuela', 'Frid', 'Bernardo', 'Man', 'Valentina', 'Ferumchael', 'Davi', 'Vidnald', 'Sophia', 'Richter', 'Theo', 'Halwil', 'Isabella', 'Samjohn', 'Lorenzo', 'Fridsig', 'Heloisa', 'Ceolfrea', 'Gabriel', 'Sonla', 'Luiza', 'Grimkim', 'Pedro', 'Rahli', 'Julia', 'Wardu', 'Benjamin', 'Icen', 'Lorena', 'Edhes', 'Matheus', 'Leyfridchar', 'Livia', 'Gardwaru', 'Lucas', 'Connald', 'Meriald', 'Lenles', 'Riemeri', 'Elitine', 'Macchar', 'Danan', 'Anne', 'Lauty', 'Freacyn', 'Thas', 'Phiadon', 'Brandhal', 'Ciavin', 'Shaelf', 'Joguth']
nT = 1

if browser == 'Chrome':
	browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
elif browser == 'Firefox':
	browser = webdriver.Firefox()

def gerarNetflix(op):
	global nT

	while op == 1:
		#Primeira página
		browser.get('https://www.netflix.com/getstarted?action=startAction&locale=pt-BR')

		# Botão 'Veja nosso Planos'
		browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[2]/div/div[2]/button').click()

		time.sleep(1.5)

		# Botão 'Continuar'
		browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[2]/div/div[3]/button').click()

		time.sleep(1.5)

		# Botão 'Continuar'
		browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[2]/div/div[2]/button').click()

		time.sleep(1.5)

		# Dados Form
		email = "netgen" + gerarString(6) + "@" + emailHosts[randint(0,len(emailHosts)-1)]
		browser.find_element_by_name('email').send_keys(email)
		senha = gerarString(7)
		print('login: ', email)
		print('senha: ', senha)
		browser.find_element_by_name('password').send_keys(senha)
		# Botão 'Continuar'
		browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[2]/div/form/div[2]/button').click()
		input()
		op = 2

	while op == 2:
		#Segunda página
		browser.get('https://www.4devs.com.br/gerador_de_numero_cartao_credito')
		browser.find_element_by_xpath('//*[@id="app-wrapper"]/div[2]/div[2]/div[2]/div[3]/label/span').click()
		browser.find_element_by_xpath('//*[@id="area_botoes"]/label/input').click()

		time.sleep(1.5)

		cc = browser.find_element_by_id('cartao_numero').text.strip()
		validate = browser.find_element_by_id('data_validade').text[3:].replace('/','')
		csv = browser.find_element_by_id('codigo_seguranca').text

		op = 3

	while op == 3:
		#Terceira página
		browser.get('https://www.netflix.com/signup/password?locale=pt-BR')

		try:
			browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button').click()

			time.sleep(1)

			browser.find_element_by_id('id_password').send_keys(senha)

			browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[2]/div/form/div/div[4]/button').click()
			pass
		except:
			browser.find_element_by_xpath('//*[@id="formstart"]/button/span[1]').click()
			pass

		time.sleep(1.5)
		#
		browser.find_element_by_xpath('//*[@id="creditOrDebitCardDisplayStringId"]/a/div').click()

		time.sleep(1.5)

		nome = nomes[randint(0, len(nomes)-1)]
		sobrenome = nomes[randint(0, len(nomes)-1)]

		browser.find_element_by_id('id_firstName').send_keys(nome)
		browser.find_element_by_id('id_lastName').send_keys(sobrenome)
		browser.find_element_by_id('id_creditCardNumber').send_keys(cc)
		browser.find_element_by_id('id_creditExpirationMonth').send_keys(validate)
		browser.find_element_by_id('id_creditCardSecurityCode').send_keys(csv)

		browser.find_element_by_id('simplicityPayment-INICI').click()

		input()

		if 'orderfinal' not in browser.current_url:
			print('Não foi possível criar a conta, tentando novamente. '+str(nT)+' tentativa(s).\n')
			nT += 1
			gerarNetflix(2)
			break
		else:
			print('Conta criada depois de .'+str(nT)+' tentativa(s).\n')
			print('Login: '+email)
			print('Senha: '+senha)
			op = 4

def gerarString(qtd):
	carac = list("abcdefhijklmnopqrstuvxwyz123456789")
	random.shuffle(carac)

	i = 0
	strg = ""
	for i in range(qtd):
		strg = strg + carac[i]
		i+=1

	return strg

gerarNetflix(1)