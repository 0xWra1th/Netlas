#Network Connection IP LookUp
#Author: Scragg
#Date: 24/03/2021
import psutil as ps
import time, requests, json, sys
import threading
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
	ZA.setVisible(False)

	US = QLabel(window)
	US.setPixmap(QPixmap('assets/US.png'))
	US.setVisible(False)

	UK = QLabel(window)
	UK.setPixmap(QPixmap('assets/UK.png'))
	UK.setVisible(False)

	FR = QLabel(window)
	FR.setPixmap(QPixmap('assets/FR.png'))
	FR.setVisible(False)

	AU = QLabel(window)
	AU.setPixmap(QPixmap('assets/AU.png'))
	AU.setVisible(False)

	BR = QLabel(window)
	BR.setPixmap(QPixmap('assets/BR.png'))
	BR.setVisible(False)

	CA = QLabel(window)
	CA.setPixmap(QPixmap('assets/CA.png'))
	CA.setVisible(False)

	CN = QLabel(window)
	CN.setPixmap(QPixmap('assets/CN.png'))
	CN.setVisible(False)

	IN = QLabel(window)
	IN.setPixmap(QPixmap('assets/IN.png'))
	IN.setVisible(False)

	RU = QLabel(window)
	RU.setPixmap(QPixmap('assets/RU.png'))
	RU.setVisible(False)

	GR = QLabel(window)
	GR.setPixmap(QPixmap('assets/GR.png'))
	GR.setVisible(False)
	GR.move(0,-64)

	IR = QLabel(window)
	IR.setPixmap(QPixmap('assets/IR.png'))
	IR.setVisible(False)
	IR.move(0,-64)

	SG = QLabel(window)
	SG.setPixmap(QPixmap('assets/SG.png'))
	SG.setVisible(False)
	SG.move(0,0)

	IT = QLabel(window)
	IT.setPixmap(QPixmap('assets/IT.png'))
	IT.setVisible(False)
	IT.move(0,0)

	IS = QLabel(window)
	IS.setPixmap(QPixmap('assets/IS.png'))
	IS.setVisible(False)
	IS.move(0,0)

	NZ = QLabel(window)
	NZ.setPixmap(QPixmap('assets/NZ.png'))
	NZ.setVisible(False)
	NZ.move(0,0)

	PE = QLabel(window)
	PE.setPixmap(QPixmap('assets/PE.png'))
	PE.setVisible(False)
	PE.move(0,0)

	SE = QLabel(window)
	SE.setPixmap(QPixmap('assets/SE.png'))
	SE.setVisible(False)
	SE.move(0,0)

	JP = QLabel(window)
	JP.setPixmap(QPixmap('assets/JP.png'))
	JP.setVisible(False)
	JP.move(0,0)

	IRAN = QLabel(window)
	IRAN.setPixmap(QPixmap('assets/IRAN.png'))
	IRAN.setVisible(False)
	IRAN.move(0,0)

	MX = QLabel(window)
	MX.setPixmap(QPixmap('assets/MX.png'))
	MX.setVisible(False)
	MX.move(0,0)

	countries = [ZA, US, UK, FR, AU, BR, CA, CN, IN, RU, GR, IR, SG, IT, IS, NZ, PE, SE, JP, IRAN, MX]

	window.show()

	#Threading
	loop = threading.Thread(target=netCheck, args=(text_area,window,countries,))
	loop.start();

	sys.exit(app.exec_())

def atlasLight(country):
	country.setVisible(True)
	time.sleep(3)
	country.setVisible(False)

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

				#Auto-Scroll
				time.sleep(0.01)
				ta.update()
				scrollbar.update()
				scrollbar.setValue(scrollbar.maximum())
				time.sleep(1)
				ta.update()
				scrollbar.update()
				scrollbar.setValue(scrollbar.maximum())

				#USING API
				response = requests.get("http://ip-api.com/json/"+str(curr)+"?fields=status,country,city,query")
				if 'json' in response.headers.get('Content-Type'):
					details = response.json()
					if details["status"] == "success":
						if details["country"] == "South Africa":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ZAThread = threading.Thread(target=atlasLight, args=(countries[0],))
							ZAThread.start();
							ta.append(text)
						elif details["country"] == "United States": 
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							USThread = threading.Thread(target=atlasLight, args=(countries[1],))
							USThread.start();
							ta.append(text)
						elif details["country"] == "United Kingdom":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							UKThread = threading.Thread(target=atlasLight, args=(countries[2],))
							UKThread.start();
							ta.append(text)
						elif details["country"] == "France":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							FRThread = threading.Thread(target=atlasLight, args=(countries[3],))
							FRThread.start();
							ta.append(text)
						elif details["country"] == "Australia":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							AUThread = threading.Thread(target=atlasLight, args=(countries[4],))
							AUThread.start();
							ta.append(text)
						elif details["country"] == "Brazil":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							BRThread = threading.Thread(target=atlasLight, args=(countries[5],))
							BRThread.start();
							ta.append(text)
						elif details["country"] == "Canada":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							CAThread = threading.Thread(target=atlasLight, args=(countries[6],))
							CAThread.start();
							ta.append(text)
						elif details["country"] == "China":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							CNThread = threading.Thread(target=atlasLight, args=(countries[7],))
							CNThread.start();
							ta.append(text)
						elif details["country"] == "India":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							INThread = threading.Thread(target=atlasLight, args=(countries[8],))
							INThread.start();
							ta.append(text)
						elif details["country"] == "Russia":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							RUThread = threading.Thread(target=atlasLight, args=(countries[9],))
							RUThread.start();
							ta.append(text)
						elif details["country"] == "Germany":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							GRThread = threading.Thread(target=atlasLight, args=(countries[10],))
							GRThread.start();
							ta.append(text)
						elif details["country"] == "Ireland":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							IRThread = threading.Thread(target=atlasLight, args=(countries[11],))
							IRThread.start();
							ta.append(text)
						elif details["country"] == "Singapore":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							SGThread = threading.Thread(target=atlasLight, args=(countries[12],))
							SGThread.start();
							ta.append(text)
						elif details["country"] == "Italy":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ITThread = threading.Thread(target=atlasLight, args=(countries[13],))
							ITThread.start();
							ta.append(text)
						elif details["country"] == "Iceland":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ISThread = threading.Thread(target=atlasLight, args=(countries[14],))
							ISThread.start();
							ta.append(text)
						elif details["country"] == "New Zealand":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							NZThread = threading.Thread(target=atlasLight, args=(countries[15],))
							NZThread.start();
							ta.append(text)
						elif details["country"] == "Peru":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							PEThread = threading.Thread(target=atlasLight, args=(countries[16],))
							PEThread.start();
							ta.append(text)
						elif details["country"] == "Sweden":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							SEThread = threading.Thread(target=atlasLight, args=(countries[17],))
							SEThread.start();
							ta.append(text)
						elif details["country"] == "Japan":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							JPThread = threading.Thread(target=atlasLight, args=(countries[18],))
							JPThread.start();
							ta.append(text)
						elif details["country"] == "Iran":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							IRANThread = threading.Thread(target=atlasLight, args=(countries[19],))
							IRANThread.start();
							ta.append(text)
						elif details["country"] == "Mexico":
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							MXThread = threading.Thread(target=atlasLight, args=(countries[20],))
							MXThread.start();
							ta.append(text)
						else:
							text = "<span style=\" font-size:11pt; font-weight:200; color:white;\" >"+details["country"]+", "+details["city"]+" - "+str(curr)+" : "+str(ip[4][1])+"</span>"
							ta.append(text)

if __name__ == "__main__":
    main()

