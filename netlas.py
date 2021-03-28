#Network Connection IP LookUp
#Author: 0xWraith
#Date: 24/03/2021
import psutil as ps
import time, requests, json, sys
import threading
from geoip import geolite2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main():
	
	# PyQt Setup
	app = QApplication(sys.argv)
	app.setStyle('fusion')
	window = QWidget()
	window.setMaximumSize(1080, 736)
	window.setMinimumSize(1080, 736)
	window.setWindowTitle('Netlas')
	window.setWindowIcon(QIcon("assets/icon_01.png"))

	#Text Output
	text_area = QTextEdit(window)
	text_area.move(0,536)
	text_area.resize(1080,200)
	text_area.setReadOnly(True)
	text_area.setFrameStyle(QFrame.HLine)
	text_area.setStyleSheet("background-color: black")

	#Adding Image
	label = QLabel(window)
	label.setPixmap(QPixmap('assets/world_map_1080_Dark.jpg'))

	ZA = QLabel(window)
	ZA.setPixmap(QPixmap('assets/ZA.png'))
	ZA.setVisible(False)
	#ZA.move(0,0)
	#ZA.resize(1080,536)
	#ZA.setStyleSheet("border: 3px solid white;border-radius: 10px;background-color: white")

	US = QLabel(window)
	US.setPixmap(QPixmap('assets/US.png'))
	US.setVisible(False)
	#US.move(120,145)
	#US.resize(30,30)
	#US.setStyleSheet("border: 3px solid white;border-radius: 15px;background-color: white")

	UK = QLabel(window)
	UK.setPixmap(QPixmap('assets/UK.png'))
	UK.setVisible(False)
	#UK.move(435,100)
	#UK.resize(10,10)
	#UK.setStyleSheet("border: 3px solid white;border-radius: 5px;background-color: white")

	FR = QLabel(window)
	FR.setPixmap(QPixmap('assets/FR.png'))
	FR.setVisible(False)
	#FR.move(445,120)
	#FR.resize(15,15)
	#FR.setStyleSheet("border: 3px solid white;border-radius: 7px;background-color: white")


	window.show()

	#Threading
	loop = threading.Thread(target=netCheck, args=(text_area,window,ZA,US,UK,FR,))
	loop.start();

	sys.exit(app.exec_())

def netCheck(ta, win, ZA, US, UK, FR):
	results = ps.net_connections()
	count = 0
	scrollbar = ta.verticalScrollBar();
	scrollbar.setStyleSheet("background-color: black;color:black")

	while (True):
		new = ps.net_connections()
		if results != new:
			results = new
		for ip in results:
			if ip[4] != () and ip[4][0] != "::1" and ip[4][0] != "127.0.0.1":
				count+=1
				curr = str(ip[4][0])
				time.sleep(2)

				#RESET MARKERS
				ZA.setVisible(False)
				US.setVisible(False)
				UK.setVisible(False)
				FR.setVisible(False)

				#USING API
				response = requests.get("http://ip-api.com/json/"+str(curr)+"?fields=status,country,city,query")
				if 'json' in response.headers.get('Content-Type'):
					details = response.json()
					if details["status"] == "success":
						if details["country"] == "South Africa":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ZA.setVisible(True)
							ta.append(text)
						elif details["country"] == "United States": 
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							US.setVisible(True)
							ta.append(text)
						elif details["country"] == "France":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							FR.setVisible(True)
							ta.append(text)
						elif details["country"] == "United Kingdom":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							UK.setVisible(True)
							ta.append(text)
						else:
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ta.append(text)
						scrollbar.setValue(scrollbar.maximum())

if __name__ == "__main__":
    main()
