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

	#Countries
	ZA = QLabel(window)
	ZA.setPixmap(QPixmap('assets/ZA.png'))
	ZA.setVisible(True)

	US = QLabel(window)
	US.setPixmap(QPixmap('assets/US.png'))
	US.setVisible(True)

	UK = QLabel(window)
	UK.setPixmap(QPixmap('assets/UK.png'))
	UK.setVisible(True)

	FR = QLabel(window)
	FR.setPixmap(QPixmap('assets/FR.png'))
	FR.setVisible(True)

	AU = QLabel(window)
	AU.setPixmap(QPixmap('assets/AU.png'))
	AU.setVisible(True)

	BR = QLabel(window)
	BR.setPixmap(QPixmap('assets/BR.png'))
	BR.setVisible(True)

	CA = QLabel(window)
	CA.setPixmap(QPixmap('assets/CA.png'))
	CA.setVisible(True)

	CN = QLabel(window)
	CN.setPixmap(QPixmap('assets/CN.png'))
	CN.setVisible(True)

	IN = QLabel(window)
	IN.setPixmap(QPixmap('assets/IN.png'))
	IN.setVisible(True)

	RU = QLabel(window)
	RU.setPixmap(QPixmap('assets/RU.png'))
	RU.setVisible(True)

	countries = [ZA, US, UK, FR, AU, BR, CA, CN, IN, RU]


	window.show()

	#Threading
	loop = threading.Thread(target=netCheck, args=(text_area,window,countries,))
	loop.start();

	sys.exit(app.exec_())

def netCheck(ta, win, countries):
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
				time.sleep(1)

				#RESET MARKERS
				for c in countries:
					c.setVisible(False)

				#USING API
				response = requests.get("http://ip-api.com/json/"+str(curr)+"?fields=status,country,city,query")
				if 'json' in response.headers.get('Content-Type'):
					details = response.json()
					if details["status"] == "success":
						if details["country"] == "South Africa":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[0].setVisible(True)
							ta.append(text)
						elif details["country"] == "United States": 
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[1].setVisible(True)
							ta.append(text)
						elif details["country"] == "United Kingdom":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[2].setVisible(True)
							ta.append(text)
						elif details["country"] == "France":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[3].setVisible(True)
							ta.append(text)
						elif details["country"] == "Australia":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[4].setVisible(True)
							ta.append(text)
						elif details["country"] == "Brazil":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[5].setVisible(True)
							ta.append(text)
						elif details["country"] == "Canada":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[6].setVisible(True)
							ta.append(text)
						elif details["country"] == "China":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[7].setVisible(True)
							ta.append(text)
						elif details["country"] == "India":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[8].setVisible(True)
							ta.append(text)
						elif details["country"] == "Russia":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							countries[9].setVisible(True)
							ta.append(text)
						else:
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ta.append(text)
						scrollbar.setValue(scrollbar.maximum())

if __name__ == "__main__":
    main()
