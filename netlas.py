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

	#Adding Image
	label = QLabel(window)
	label.setPixmap(QPixmap('assets/world_map_1080.jpg'))

	window.show()

	#Threading
	loop = threading.Thread(target=netCheck, args=(text_area,))
	loop.start();

	sys.exit(app.exec_())


def netCheck(ta):
	results = ps.net_connections()
	count = 0
	scrollbar = ta.verticalScrollBar();

	while (True):
		new = ps.net_connections()
		if results != new:
			results = new
		for ip in results:
			if ip[4] != () and ip[4][0] != "::1" and ip[4][0] != "127.0.0.1":
				count+=1
				curr = str(ip[4][0])
				time.sleep(2)
				#USING API
				response = requests.get("http://ip-api.com/json/"+str(curr)+"?fields=status,country,city,query")
				if 'json' in response.headers.get('Content-Type'):
					details = response.json()
					if details["status"] == "success":
						if details["country"] == "South Africa":
							text = "<span style=\" font-size:12pt; font-weight:600; color:#000000;\" >"+details["country"]+", "+details["city"]+" -> "+str(curr)+":"+str(ip[4][1])+"</span>"
							ta.append(text)
						elif details["country"] == "United States": 
							text = "<span style=\" font-size:12pt; font-weight:600; color:#0000ff;\" >"+details["country"]+", "+details["city"]+" -> "+str(curr)+":"+str(ip[4][1])+"</span>"
							ta.append(text)
						elif details["country"] == "France":
							text = "<span style=\" font-size:12pt; font-weight:600; color:#00ff00;\" >"+details["country"]+", "+details["city"]+" -> "+str(curr)+":"+str(ip[4][1])+"</span>"
							ta.append(text)
						else:
							text = "<span style=\" font-size:12pt; font-weight:600; color:#ff0000;\" >"+details["country"]+", "+details["city"]+" -> "+str(curr)+":"+str(ip[4][1])+"</span>"
							ta.append(text)
						scrollbar.setValue(scrollbar.maximum())

if __name__ == "__main__":
    main()
