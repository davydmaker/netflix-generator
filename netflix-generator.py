# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint
import random
import time

__author__ = "Davyd Maker"
__version__ = "2.0"

browser = 'Chrome'
emailHosts = ['moakt.ws', 'mohmal.com', 'divismail.ru', 'sharklasers.com', 'guerrillamail.info', 'grr.la', 'guerrillamail.biz', 'guerrillamail.com', 'guerrillamail.de', 'guerrillamail.net', 'guerrillamail.org', 'guerrillamailblock.com', 'spam4.me', 'kismail.ru', 'extremail.ru']
nomes = ['Bertlas', 'Ewise', 'Ruthbri', 'Freamond', 'Wigfled', 'Sephra', 'Markcrow', 'Frid', 'Man', 'Ferumchael', 'Vidnald', 'Richter', 'Halwil', 'Samjohn', 'Fridsig', 'Ceolfrea', 'Sonla', 'Grimkim', 'Rahli', 'Wardu', 'Icen', 'Edhes', 'Leyfridchar', 'Gardwaru', 'Connald', 'Meriald', 'Lenles', 'Riemeri', 'Elitine', 'Macchar', 'Danan', 'Anne', 'Lauty', 'Freacyn', 'Thas', 'Phiadon', 'Brandhal', 'Ciavin', 'Shaelf', 'Joguth']
nT = 0

if browser == 'Chrome':
	browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe")
elif browser == 'Firefox':
	browser = webdriver.Firefox()

def gerarNetflix(op):
	global nT

	while op == 1:
		#Primeira página
		browser.get('https://www.netflix.com/getstarted?action=startAction&locale=pt-BR')
		for option in browser.find_elements_by_tag_name('div'):
			if option.get_attribute('data-reactid') == '44':
				option.click()
		browser.find_elements_by_tag_name('button')[0].click()
		email = "netgen" + gerarString(6) + "@" + emailHosts[randint(0,14)]
		browser.find_element_by_name('email').send_keys(email)
		senha = gerarString(7)
		browser.find_element_by_name('password').send_keys(senha)
		browser.find_elements_by_tag_name('button')[0].click()
		op = 2

	while op == 2:
		#Segunda página
		browser.get('http://www.4devs.com.br/gerador_conta_bancaria')
		select = Select(browser.find_element_by_name('cc_banco'))
		select.select_by_value('5')
		while True:
			browser.find_element_by_id('btn_gerar_conta').click()
			time.sleep(1.5)
			contaCorrente = browser.find_element_by_id('conta_corrente').get_attribute('value').split('-')
			if contaCorrente[0].startswith('001') or contaCorrente[0].startswith('013') or contaCorrente[0].startswith('023'):
				break 
		agencia = browser.find_element_by_id('agencia').get_attribute('value')
		numeroConta = contaCorrente[0]
		tipoConta = numeroConta[:3]
		numeroConta = numeroConta[3:]
		digitoFinal = contaCorrente[1]
		op = 3

	while op == 3:
		#Terceira página
		browser.get('https://www.netflix.com/YourAccountPayment')
		for option in browser.find_elements_by_tag_name('div'):
			if option.get_attribute('data-mop-type') == 'directDebitOption' and nT == 0:
				option.click()
		browser.find_element_by_name('firstName').send_keys(nomes[randint(0,39)])
		browser.find_element_by_name('lastName').send_keys(nomes[randint(0,39)])
		browser.find_element_by_name('customerIdentification').send_keys(gerarCPF())
		select = Select(browser.find_element_by_name('bankChoice'))
		select.select_by_value('CAIXA_BRAZIL')
		browser.find_element_by_name('branchCode').send_keys(agencia)
		select = Select(browser.find_element_by_name('accountType'))
		select.select_by_value(tipoConta)
		browser.find_element_by_name('accountNumber').send_keys(numeroConta)
		browser.find_element_by_name('accountNumberCheckDigits').send_keys(digitoFinal)
		browser.find_elements_by_tag_name('button')[0].click()
		if browser.current_url == 'https://www.netflix.com/YourAccountPayment':
			print('Não foi possível criar a conta, tentando novamente. '+str(nT)+' tentativa(s).\n')
			nT += 1
			gerarNetflix(2)
			break
		else:
			print('Conta criada depois de .'+str(nT)+' tentativa(s).\n')
			print('Login: '+email)
			print('\nSenha: '+senha)
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

def gerarCPF():
	def calcula_digito(digs):
		s = 0
		qtd = len(digs)
		for i in xrange(qtd):
			s += n[i] * (1+qtd-i)
		res = 11 - s % 11
		if res >= 10: return 0
		return res                                                                              
	n = [random.randrange(10) for i in xrange(9)]
	n.append(calcula_digito(n))
	n.append(calcula_digito(n))
	return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

gerarNetflix(1)
