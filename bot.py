import telebot
import os
import subprocess
f = open("secrets", "r")
bot = telebot.TeleBot(f.readline(), parse_mode=None)
f.close()
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "цей бот завантажує мультфільми із посилання на ютуб")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text 
	print(msg)
	if("&list=" in msg):
		bot.reply_to(message,"Ми не завантажуємо плейлисти")
		return
	bot.send_message(message.chat.id, "starting download...")
	
	process = subprocess.Popen(['C:\\Users\\Admin\\Desktop\\Ivan\\youtube-dl.exe', msg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	print(stdout)
	print(stderr)
	
	if("ERROR" in str(stderr)):
		print("ERROR")
		bot.send_message(message.chat.id, "посилання не правильне")
	else:
		for file in os.listdir(".\\"):
			if(file.endswith(".mp4")):
				file_path = os.path.join(".\\", file)
				print(file_path)
				d = open(file_path, "rb")
				bot.send_document(message.chat.id, d)
				d.close()
				os.remove(file_path)



bot.polling()



