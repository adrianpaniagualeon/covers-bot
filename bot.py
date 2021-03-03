import requests 
import telebot
from telebot import types
from flask import Flask
from datetime import date, datetime, timedelta
from PIL import Image
import os


TOKEN =  os.environ['TOKEN']


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)



@bot.message_handler(commands={"start"})
def start(message):
	chat_id= message.chat.id
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Diario de León')
	itembtnb = types.KeyboardButton('La Nueva Crónica')
	itembtnc = types.KeyboardButton('El Mundo')
	itembtnd = types.KeyboardButton('La Razón')
	itembtne = types.KeyboardButton('El Pais')
	itembtnf = types.KeyboardButton('ABC')
	itembtng = types.KeyboardButton('La Vanguardia')
	itembtnh = types.KeyboardButton('Marca')
	markup.row(itembtna, itembtnb)
	markup.row(itembtnc, itembtnd, itembtne)
	markup.row(itembtnf, itembtng, itembtnh)
	bot.send_message(chat_id, "¿Qué portada quieres ver?", reply_markup=markup)



@bot.message_handler(regexp="La Nueva Crónica")
def lanuevacronica(message):
	chat_id= message.chat.id
	today = date.today() 
	hoy = today.strftime("%Y%m%d")
	year_today = today.strftime("%Y")
	yesterday = date.today() - timedelta(days=1)
	ayer = yesterday.strftime("%Y%m%d")
	year_yesterday = yesterday.strftime("%Y")
	markup = types.ReplyKeyboardRemove(selective=True)
	url = "https://www.lasportadas.es/data/"+str(year_today)+"/"+str(hoy)+"/GLaNuevaCronicaI.jpg"
	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("lanuevacronica.png", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://www.lasportadas.es/data/"+str(year_yesterday)+"/"+str(ayer)+"/GLaNuevaCronicaI.jpg")
		foto_portada = open("lanuevacronica.png", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('lanuevacronica.png', 'rb')
	bot.send_photo(chat_id, photo)



@bot.message_handler(regexp="El Mundo")
def elmundo(message):
	chat_id= message.chat.id
	today = date.today() 
	hoy = today.strftime("%Y%m%d")
	year_today = today.strftime("%Y")
	yesterday = date.today() - timedelta(days=1)
	ayer = yesterday.strftime("%Y%m%d")
	year_yesterday = yesterday.strftime("%Y")
	markup = types.ReplyKeyboardRemove(selective=True)
	url = "https://www.lasportadas.es/data/"+str(year_today)+"/"+str(hoy)+"/GElMundoI.jpg"
	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("elmundo.png", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://www.lasportadas.es/data/"+str(year_yesterday)+"/"+str(ayer)+"/GLaNuevaCronicaI.jpg")
		foto_portada = open("elmundo.png", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('elmundo.png', 'rb')
	bot.send_photo(chat_id, photo)


@bot.message_handler(regexp="La Razón")
def larazon(message):
	chat_id= message.chat.id
	today = date.today() 
	hoy = today.strftime("%Y%m%d")
	year_today = today.strftime("%Y")
	yesterday = date.today() - timedelta(days=1)
	ayer = yesterday.strftime("%Y%m%d")
	year_yesterday = yesterday.strftime("%Y")
	markup = types.ReplyKeyboardRemove(selective=True)
	url = "https://www.lasportadas.es/data/"+str(year_today)+"/"+str(hoy)+"/GLaRazonI.jpg"
	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("larazon.png", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://www.lasportadas.es/data/"+str(year_yesterday)+"/"+str(ayer)+"/GLaRazonI.jpg")
		foto_portada = open("larazon.png", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('larazon.png', 'rb')
	bot.send_photo(chat_id, photo)

@bot.message_handler(regexp="La Razón")
def larazon(message):
	chat_id= message.chat.id
	today = date.today() 
	hoy = today.strftime("%Y%m%d")
	year_today = today.strftime("%Y")
	yesterday = date.today() - timedelta(days=1)
	ayer = yesterday.strftime("%Y%m%d")
	year_yesterday = yesterday.strftime("%Y")
	markup = types.ReplyKeyboardRemove(selective=True)
	url = "https://www.lasportadas.es/data/"+str(year_today)+"/"+str(hoy)+"/GLaRazonI.jpg"
	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("larazon.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://www.lasportadas.es/data/"+str(year_yesterday)+"/"+str(ayer)+"/GLaRazonI.jpg")
		foto_portada = open("larazon.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('larazon.jpg', 'rb')
	bot.send_photo(chat_id, photo)


@bot.message_handler(regexp="Diario de León")
def diariodeleon(message):
	chat_id= message.chat.id
	today = date.today() 
	year_today = today.strftime("%Y")
	month_today = today.strftime("%m")
	day_today = today.strftime("%d")

	yesterday = date.today() - timedelta(days=1)
	year_yesterday = yesterday.strftime("%Y")
	month_yesterday = yesterday.strftime("%m")
	day_yesterday = yesterday.strftime("%d")

	url = "https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/diario_leon.750.jpg"

	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("diariodeleon.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/diario_leon.750.jpg")
		foto_portada = open("diariodeleon.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('diariodeleon.jpg', 'rb')
	bot.send_photo(chat_id, photo)



@bot.message_handler(regexp="El Pais")
def elpais(message):
	chat_id= message.chat.id
	today = date.today() 
	hoy = today.strftime("%Y%m%d")
	year_today = today.strftime("%Y")
	month_today = today.strftime("%m")

	yesterday = date.today() - timedelta(days=1)
	ayer = yesterday.strftime("%Y%m%d")
	year_yesterday = yesterday.strftime("%Y")
	month_yesterday = yesterday.strftime("%m")

	url = "https://srv00.epimg.net/pdf/elpais/snapshot/"+str(year_today)+"/"+str(month_today)+"/elpais/"+str(hoy)+"Big.jpg"

	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("elpais.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://srv00.epimg.net/pdf/elpais/snapshot/"+str(year_today)+"/"+str(month_today)+"/elpais/"+str(hoy)+"Big.jpg")
		foto_portada = open("elpais.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('elpais.jpg', 'rb')
	bot.send_photo(chat_id, photo)

@bot.message_handler(regexp="ABC")
def abc(message):
	chat_id= message.chat.id
	today = date.today() 
	year_today = today.strftime("%Y")
	month_today = today.strftime("%m")
	day_today = today.strftime("%d")

	yesterday = date.today() - timedelta(days=1)
	year_yesterday = yesterday.strftime("%Y")
	month_yesterday = yesterday.strftime("%m")
	day_yesterday = yesterday.strftime("%d")

	url = "https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/abc.750.jpg"

	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("abc.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/abc.750.jpg")
		foto_portada = open("abc.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('abc.jpg', 'rb')
	bot.send_photo(chat_id, photo)

@bot.message_handler(regexp="La Vanguardia")
def lavanguardia(message):
	chat_id= message.chat.id
	today = date.today() 
	year_today = today.strftime("%Y")
	month_today = today.strftime("%m")
	day_today = today.strftime("%d")

	yesterday = date.today() - timedelta(days=1)
	year_yesterday = yesterday.strftime("%Y")
	month_yesterday = yesterday.strftime("%m")
	day_yesterday = yesterday.strftime("%d")

	url = "https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/lavanguardia.750.jpg"

	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("lavanguardia.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/lavanguardia.750.jpg")
		foto_portada = open("lavanguardia.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('lavanguardia.jpg', 'rb')
	bot.send_photo(chat_id, photo)

@bot.message_handler(regexp="Marca")
def marca(message):
	chat_id= message.chat.id
	today = date.today() 
	year_today = today.strftime("%Y")
	month_today = today.strftime("%m")
	day_today = today.strftime("%d")

	yesterday = date.today() - timedelta(days=1)
	year_yesterday = yesterday.strftime("%Y")
	month_yesterday = yesterday.strftime("%m")
	day_yesterday = yesterday.strftime("%d")

	url = "https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/marca.750.jpg"

	print(url)
	portada = requests.get(url)
	print (portada.status_code)

	if (portada.status_code == 200):
		foto_portada = open("marca.jpg", "wb")
		foto_portada.write(portada.content)
		foto_portada.close()

	else:
		portada_ayer = requests.get("https://img.kiosko.net/"+str(year_today)+"/"+str(month_today)+"/"+str(day_today)+"/es/marca.750.jpg")
		foto_portada = open("marca.jpg", "wb")
		foto_portada.write(portada_ayer.content)
		foto_portada.close()

	photo = open('marca.jpg', 'rb')
	bot.send_photo(chat_id, photo)


bot.polling()