from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtGui import QPixmap
import os



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "watermark_front.ui"), self)

        #Connection aux widgets du front-end
     
        self.browse_button.clicked.connect(self.browser_image)
   
    # Fonction pour parcourir les fichiers 
    def browser_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, 'Selectionne une image', '', 'All Files (*)')
        print(self.image_path)