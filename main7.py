#https://tproger.ru/translations/python-gui-pyqt/
#https://ru.stackoverflow.com/questions/697148/Виджет-для-отображения-картинки-в-pyqt-Как-показать-картинку-из-файла

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design5  # Это наш конвертированный файл дизайна
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush

    
class ExampleApp(QtWidgets.QMainWindow, design5.Ui_MainWindow):
    def __init__(self,canvas_class):
        
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('имя окошка')
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.pokas.clicked.connect(self.load_image)
        self.canvas_class = canvas_class
        self.listt, self.chetchik = [], 0
        
        
    def browse_folder(self):
        
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.listt.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")# открыть диалог выбора директории и установить значение переменной равной пути к выбранной директории
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            dirway_file = (list(os.walk(directory))[0][0])
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listt.append(dirway_file + '/' + file_name)   # добавить файл в listWidget
                self.listWidget.addItem(file_name)
            self.listt = list(filter(lambda i: i[-4::] in ['.png', '.jpg', '.gif', '.bmp'], self.listt))
                
    def load_image(self):
        if len(self.listt) != 0:
            self.canvas_class.otobragenie(self.listt[self.chetchik])#"speedometr.png")
        print(self.listt)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F: 
            print(self.chetchik, self.listt[self.chetchik])
            self.chetchik = (self.chetchik+1)%(len(self.listt))
            self.canvas_class.otobragenie(self.listt[self.chetchik])
         
    

class ImageViewer(QWidget):
    
    def __init__(self, image_path, parent=None):
        
        super().__init__(parent)
        self.setGeometry(10, 10, 500, 500)        
        self.label = QLabel(self)
        self.pixmap = QPixmap(image_path)
        self.label.setPixmap(self.pixmap)
        self.setWindowTitle('PyQt5 Image Viewer')


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, qp):

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d41')#'#d4d4d4'
        qp.setPen(col)
        qp.setBrush(QColor(50, 50, 50))
        qp.drawRect(-10, -10, 520, 520)
      
        
    def otobragenie(self, image_path1):
        
        self.pixmap1 = QPixmap(image_path1)
        self.pixmap1 = self.pixmap1.scaled(500, 500, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap1)
        self.resize(500, 500)  # fit window to the image
      
        
def main(canvas_class):
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp(canvas_class)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение 
        
            
if __name__ == '__main__':
            
    app = QApplication(sys.argv)
    image_viewer = ImageViewer("for_size_convas_window.jpg")
    app1 = QApplication(sys.argv)
    image_viewer.show()
    main(image_viewer) 
    sys.exit(app1.exec_())    
  

