import sys
import thread
import json
import pygame
import time
from PyQt4 import QtCore,QtGui,uic
from PyQt4.QtGui import QSound

import bluetooth
qtCreatorFile = "score_board.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
        
                                                				    
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
            
		self.setupUi(self)
		self.labelHomeTeamName.setText("a Team")
		self.labelAwayTeamName.setText("b Team")
		self.labelGameClock.setText("01:54")
		self.labelShotClock.setText("24")

		thread.start_new_thread(self.process_bluetooth, ())
		
		
		
	def process_bluetooth(self):

		while True:
			server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
			port = 1
			server_sock.bind(("", port))
			server_sock.listen(1)
			
			client_sock, address = server_sock.accept()
			print("Accepted connection")
			
			while True:
				try:
					data = client_sock.recv(10*1024)
					print(data)

					state = json.loads(data)

					teamHome = state["teamHome"]
					teamAway = state["teamAway"]
					remainingTime = state["remainingTime"]
					scoreHome = state["scoreHome"]
					scoreAway = state["scoreAway"]
					foulsHome = state["foulsHome"]
					foulsAway = state["foulsAway"]
					shotclock = state["shotclock"]
					
				    

					if teamHome != "":
						self.labelHomeTeamName.setText(teamHome)
					if teamAway != "":
						self.labelAwayTeamName.setText(teamAway)
					
					if remainingTime != "":
						self.labelGameClock.setText(remainingTime)
						
					if shotclock != "":
                                                self.labelShotClock.setText(shotclock)
                                        if shotclock == "10":
                                                self.labelShotClock.setText(shotclock)
                                                pygame.init()
                                                pygame.mixer.init()
                                                clock = pygame.time.Clock()
                                                pygame.mixer.music.load("nbasound.mp3")
                                                pygame.mixer.music.play()
                                        if shotclock > "10" :
                                                self.labelShotClock.setText(shotclock)
                                                pygame.init()
                                                pygame.mixer.init()
                                                clock = pygame.time.Clock()
                                                pygame.mixer.music.load("nbasound.mp3")
                                                pygame.mixer.music.stop()
                                                                                                                                      
					if scoreHome != "":
						self.labelHomeTeamScore.setText(scoreHome)

					if scoreAway != "":
						self.labelAwayTeamScore.setText(scoreAway)

					if foulsHome != "":
						self.labelHomeTeamFoul.setText(foulsHome)

					if foulsAway != "":
						self.labelAwayTeamFoul.setText(foulsAway)	
				
					if (data == ""):
						break;
				
				except Exception, e:
					print(e)
					break

			client_sock.close()
			server_sock.close()			


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.showFullScreen()
	sys.exit(app.exec_())
