import sys  # sys нужен для передачи argv в QApplication
try:
    from PyQt5 import QtWidgets
except Exception:
    print('установите PyQt5')
import design5  # Это наш конвертированный файл дизайна
import design_save
import design_enter
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush
try:
    import shutil
except Exception:
    print('установите shutil')
try:
    from PIL import Image
except Exception:
    print('установите PIL')
from random import shuffle

class window_enter_class(QtWidgets.QMainWindow, design_enter.Ui_MainWindow):
    
    def __init__(self,):
        
        super().__init__()    
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ok.clicked.connect(self.close_function)
        
    def close_function(self):
        self.close()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter: 
            self.close_function()
            
            
class window_save_class(QtWidgets.QMainWindow, design_save.Ui_MainWindow):
    
    def __init__(self,):
        
        super().__init__()    
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.image_save_button.clicked.connect(self.save_function)
        self.no.clicked.connect(self.nosave_function)
  
    def input_class(self,class_input):
        self.class_input = class_input
        self.close()
                
    def save_function(self):
        self.class_input.save_or_not_input_from_save_class('save')
        self.close()
        
    def nosave_function(self):
        self.class_input.save_or_not_input_from_save_class('no')
        self.close()
     
        
def main_save(save_class):
    save_class.show()    

def main_enter(save_class):
    save_class.show()   
    
class grand_class(QtWidgets.QMainWindow, design5.Ui_MainWindow):
    
    def __init__(self, save_clas, enter_class):
        
        super().__init__()
        self.seve_or_not_otvet_window = '--' # сохранение фото после изменения
        self.massiv_image_formats = ['.png', '.jpg', '.gif', '.bmp', '.JPG']
        self.setupUi(self)  # Это нужно для инициализации дизайна
        self.setWindowTitle('РедСмот_N.0')
        self.save_clas = save_clas # класс окна сохранения
        self.enter_class = enter_class # класс окна предупреждения
        """выбор директории для просмотра фоток"""
        self.choice_dir_button_wath.clicked.connect( self.browse_folder)
        self.pokas.setEnabled(False)# делаем кнопку не кликабельной
        self.question_seve_or_not = False 
        self.otvet_got = True 
        self.izmenit = True # для одновременного изменения x и y  у картинки
        self.izmenit1 = True # для изменения формата файла
        """при нажатии отобразить ихображение"""
        self.pokas.clicked.connect(self.load_image)  
        """при выборе одной картинки из списка отобразить ее"""
        self.list_file_in_dir.currentTextChanged['QString'].connect(
            self.print_image_from_list)
        self.listt = []  # список картинок
        self.chetchik = 0 # какую картинку выбрал пользователь
        self.past_chetchik = 0 # предыдущее значение счетчика
        self.draw_image("fire.png") # залитие фона
        self.dirway_file = "" # папка файла
        """галочка для сохранения пропорций"""
        self.save_proportions_1.clicked[bool].connect(self.proportion)
        self.save_proportions1 = False  
        """бегунки с размерами изображений"""
        self.size_x_2.valueChanged[int].connect(self.size_x2_image_function)
        self.size_y_2.valueChanged[int].connect(self.size_y2_image_function)
        self.size_x_1.valueChanged[int].connect(self.size_x1_image_function)
        self.size_y_1.valueChanged[int].connect(self.size_y1_image_function)
        self.save_parametr_kachestvo.valueChanged[int].connect(
            self.save_parametr_kachestvo_function) # качество сохр. картинки
        self.size_x2_image_int = 300 # Начальные значения бегунков
        self.size_y2_image_int = 300
        self.size_x1_image_int = 300
        self.size_y1_image_int = 300
        self.save_parametr_kachestvo_int = 85 # начальное качество
        
        self.format_file_wath_program.textChanged['QString'].connect(# формат
            self.get_format_save_function)# открыт. картинки, введённый польз.
        self.save_format_str = '.jpg'
        """формат и имя файла для копирования"""
        self.format_file_for_lot_cutting.textChanged['QString'].connect(
            self.copy_format_function)
        self.copy_format_string = ".jpg"
        self.filename_a_lot_copy.textChanged['QString'].connect(
            self.copy_filename_function)
        self.copy_filename_str = "cat"
        """значения галочек которые нужны для копирования файлов"""
        self.save_proportions_2.toggled[bool].connect(
            self.cutting_in_good_function)
        self.save_proportions2 = False
        self.cutting__in_good.toggled[bool].connect(
            self.cutting_in_good_function)
        self.cutting_in_good_for_if = False
        self.get_ramka_for_save.toggled[bool].connect(
            self.cutting_in_good_function)
        self.get_ramka_for_save_bool = False
        """ начальная и конечная директории для копирования """
        self.choice_dir_button_from_copy.clicked.connect(
            self.choice_dir_for_lot_copy_from)
        self.directory_from = ''
        self.choice_dir_button_to_copy.clicked.connect(
            self.choice_dir_for_lot_copy)
        self.directory_for = ''
        self.statr_copt_button.clicked.connect( # начать копирование
            self.start_copy)
        self.comand_copy_for = False
        self.comand_copy_from = False
        """ вывод процесса копирования и созранения файлов """
        self.out_print_list_copy_file_text = ''
        
    def save_or_not_input_from_save_class(self, otvet):
        self.otvet_got = True
        self.question_seve_or_not = False
        print('true')
        self.seve_or_not_otvet_window = otvet
        self.draw_image(self.listt[self.chetchik]) 
        
    def cutting_in_good_function(self, status):
        if self.sender().text() == 'Обрезать для сохранения пропорций':
            self.cutting_in_good_for_if = status
        if self.sender().text() == "Сохранять пропорции":
            self.save_proportions2 = status
        if self.sender().text() == "Добавить рамку для сохранения пропорций":
            self.get_ramka_for_save_bool = status

    def size_x2_image_function(self, by_returned_integer):
        self.size_x2_image_int = by_returned_integer
        print(self.size_x2_image_int)
        if self.izmenit:
            print('>>><<<<')
            if  self.save_proportions1:
                size = self.size_x2_image_int * self.pixmap1.height()
                self.size_y2_image_int = size / self.pixmap1.width()
                self.size_y2_image_int = int(self.size_y2_image_int + 0.5)        
                self.izmenenie_sixe(False, int(self.size_y2_image_int))
            self.save_or_not_function()
        
    def size_y2_image_function(self, by_returned_integer):
        self.size_y2_image_int = by_returned_integer
        if self.izmenit:
            print('0=0=0=')
            if  self.save_proportions1:
                size = self.size_y2_image_int * self.pixmap1.width()
                self.size_x2_image_int = size / self.pixmap1.height()
                self.size_x2_image_int = int(self.size_x2_image_int + 0.5)
                self.izmenenie_sixe(True, int(self.size_x2_image_int))
            self.save_or_not_function()
        
    def izmenenie_sixe(self, x_or_y, value):
        self.izmenit = False
        if x_or_y:
            self.size_x_2.setValue(int(value))
        else:
            self.size_y_2.setValue(int(value))
        print('end_izmene')
        self.izmenit = True
        
    def izmenenie_format_file_save(self, value):
        self.izmenit1 = False
        self.format_file_wath_program.setText(value)
        print('end_izmene1')
        self.izmenit1 = True
        
    def get_format_save_function(self, string):
        self.save_format_str = string
        if self.izmenit1:
            self.save_or_not_function() 
        
    def size_x1_image_function(self, by_returned_integer):
        self.size_x1_image_int = by_returned_integer
        
    def size_y1_image_function(self, by_returned_integer):
        self.size_y1_image_int = by_returned_integer
        
    def save_parametr_kachestvo_function(self, by_returned_integer):
        self.save_parametr_kachestvo_int = by_returned_integer
        
    def proportion(self, status):
        self.save_proportions1 = status
        
    def copy_format_function(self, string):
        self.copy_format_string = string

    def copy_filename_function(self, string):
        self.copy_filename_str = string
        
    def save_or_not_function(self):  
        self.question_seve_or_not = True
        print("+++")
        
    def print_image_from_list(self, currentText):
        self.past_chetchik = self.chetchik
        if len(self.listt) != 0:
            if currentText[-4::] in self.massiv_image_formats:
                self.chetchik = self.listt.index(
                    self.dirway_file + '/' + currentText)
                self.draw_image(self.listt[self.chetchik])        
            
    def draw_image(self, image):
        if self.question_seve_or_not: # показываем окно сохранения если нужно        
            self.otvet_got = False
            main_save(self.save_clas)
            logika = self.listt[self.past_chetchik][-4::] == '.png' 
            if logika and self.save_format_str != '.png':
                main_enter(self.enter_class) # показать предупреждение             
            print('.........', self.otvet_got)
        if self.otvet_got: # если ответ получен
            print('pppppp')
            if self.seve_or_not_otvet_window == 'save':
                save_image_function(self.listt[self.past_chetchik],
                                    self.listt[self.past_chetchik],
                                    self.save_format_str, 
                                    self.size_x2_image_int,
                                    self.size_y2_image_int,
                                    self.save_proportions1, 85, self)  
                self.seve_or_not_otvet_window = '--'
                self.question_seve_or_not = False
                self.list_file_in_dir.clear()
                for file_name in os.listdir(self.directory):
                    ''' для каждого файла в директории'''
                    self.listt.append(self.dirway_file + '/' + file_name)
                    ''' добавить файл в отображаемый списк'''
                    self.list_file_in_dir.addItem(file_name)
                self.listt = list(filter( #отбор файлов с нужным разрешением
                    lambda i: i[-4::] in self.massiv_image_formats, self.listt))                
            self.new_image_function(image)
            
    def new_image_function(self, image):
        self.question_seve_or_not = False
        print('new image')
        self.save_filename_str = image[-4::]
        self.izmenenie_format_file_save(self.save_filename_str)  
        self.format_file_for_lot_cutting.setText(image[-4::])
        self.copy_format_string = image[-4::]
        self.pixmap1 = QPixmap(image)
        self.size_x2_image_int = int(self.pixmap1.width())
        self.size_y2_image_int = int(self.pixmap1.height())
        self.size_x1_image_int = int(self.pixmap1.width())
        self.size_y1_image_int = int(self.pixmap1.height()) 
        print(self.size_x2_image_int, self.size_y2_image_int)
        self.izmenit = False
        self.size_x_3.setText(str(self.pixmap1.width()))
        self.size_y_3.setText(str(self.pixmap1.height()))  
        
        self.izmenenie_sixe(False, int(self.size_y2_image_int))
        self.izmenenie_sixe(True, int(self.size_x2_image_int))
        self.size_x_1.setValue(int(self.size_x1_image_int))
        self.size_y_1.setValue(int(self.size_y1_image_int))
  
        self.pixmap1 = self.pixmap1.scaled(500, 500, Qt.KeepAspectRatio)
        print('======', self.pixmap1.width(), self.pixmap1.height())
        self.label_2.setPixmap(self.pixmap1)
        self.izmenit = True
        
    def browse_folder(self):
        
        self.list_file_in_dir.clear() # при смене директории очищаем списк
        self.listt.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Выберите папку")
        ''' открыть диалог выбора директории и установить значение переменной
            равной пути к выбранной директории'''
        if directory:
            '''не продолжать выполнение,
               если пользователь не выбрал директорию'''
            self.pokas.setEnabled(True)
            self.dirway_file = (list(os.walk(directory))[0][0])
            self.directory = directory
            for file_name in os.listdir(directory): 
                ''' для каждого файла в директории'''
                self.listt.append(self.dirway_file + '/' + file_name)
                self.list_file_in_dir.addItem(file_name)
            self.listt = list(filter(
                lambda i: i[-4::] in self.massiv_image_formats, self.listt))

    def choice_dir_for_lot_copy_from(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Выберите папку")
        if directory:
            if len(directory)>33:
                print_directory = directory[:30:] + '...'
            else:
                print_directory = directory
            self.choice_dir_button_from_copy.setText(str(print_directory))
            self.comand_copy_from = True
            print(self.comand_copy_from)
            self.directory_from = directory
            
    def choice_dir_for_lot_copy(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Выберите папку")
        if directory:
            if len(directory)>33:
                print_directory = directory[:30:] + '...'
            else:
                print_directory = directory
            self.choice_dir_button_to_copy.setText(str(print_directory))  
            self.comand_copy_for = True
            print(self.comand_copy_for)
            self.directory_for = directory
            
    def out_print_list_copy_file_function(self, text):
        self.out_print_list_copy_file_text = text
        self.out_print_list_copy_file.addItem(
            str(self.out_print_list_copy_file_text))
            
    def load_image(self):
        
        if len(self.listt) != 0:
            self.draw_image(self.listt[self.chetchik])
        print(self.listt)
        
    def keyPressEvent(self, event): # возможность листать фотографии клавой
        
        if event.key() == Qt.Key_Right: 
            print(self.chetchik, self.listt[self.chetchik])
            self.chetchik = (self.chetchik+1)%(len(self.listt))
            self.draw_image(self.listt[self.chetchik])
            
        if event.key() == Qt.Key_Left: 
            print(self.chetchik, self.listt[self.chetchik])
            self.chetchik = (self.chetchik-1)%(len(self.listt))
            self.draw_image(self.listt[self.chetchik])   
    
    def start_copy(self): # копирование из одной папуи в другую
        print([self.comand_copy_for, self.comand_copy_from])
        
        if self.comand_copy_for and self.comand_copy_from:
            print(self.cutting_in_good_for_if,self.get_ramka_for_save_bool,
                  self.save_parametr_kachestvo_int)
            start_copy_function(self.directory_from, #начальная директория
                                self.directory_for, #конечная директория
                                self.copy_filename_str, #выходное имя файла
                                self.copy_format_string, #формат выходного файла
                                self.size_x1_image_int, # какого размера фото
                                self.size_y1_image_int, #
                                self.save_proportions2, # галочка на пропорциях
                                self.cutting_in_good_for_if, #обрезка
                                self.get_ramka_for_save_bool, #добавить рамку
                                self.save_parametr_kachestvo_int, # качество
                                self) # передаём класс для вывода информации
            
def save_image_function(inp, out_filename, formafile, w_need, h_need,
                        save_proportional, kachestvo, classname):  
    try:
        img = Image.open(inp)
        w, h = img.size
        out = out_filename[:-4:] + formafile
        classname.out_print_list_copy_file_function(str(inp) + '\n - ' + out)
        if save_proportional:   
            img = img.resize((w_need, h_need), Image.ANTIALIAS)
        else:
            img = img.resize((w_need, h_need), Image.ANTIALIAS)
        try:
            img.save(out, optimize=True, quality=kachestvo)
            print(out)
        except Exception as e:
            print('Непредвиденная ошибка при сохранении %s '% e, inp )
            word += '-------------Попытка исправить' + inp 
            word += '\n-------------Попытка исправить'+str(e)+ '\n'
            classname.out_print_list_copy_file_function(
                'Непредвиденная ошибка при сохранении ')
            classname.out_print_list_copy_file_function(
                str(e) + ' ' + inp + '\n')
            out = out[:-4:]+inp[-4::]
            classname.out_print_list_copy_file_function(
                'Попытка исправить на ' + out + '\n')                     
            print('Попытка исправить на',out)
            img.save(out, optimize=True, quality=kachestvo)                
    except Exception as e:
        try:
            print('Непредвиденная ошибка %s '% e, [inp] ,[out])
            print('Идём дальше')
            word += inp+'\n'+str(e)+ '\n'
            classname.out_print_list_copy_file_function(
                'не удалось исправить ошибку ' + e + ' ' + inp + "\n")                
            classname.out_print_list_copy_file_function('Идем дальше\n')
        except Exception:
            pass

def start_copy_function(inp_dir, out_dir, out_filename, formafile, 
                        w_need, h_need, save_proportional, cut_bool, 
                        give_ramka, kachestvo,classname):
    papka = inp_dir
    end_papka = out_dir
    ch = 0    
    word  = '' # сообщение об ошибке в файле
    print([papka])
    files111 = list(os.walk(papka))[0]
    print('-----', *files111, sep='\n')
    files = files111[2]
    ch+=1
    for i in files:
        print(i)
        a = '/'.join(files111[0].split('\\'))
        inp = a+'/'+ i
        if inp[-4::] not in self.massiv_image_formats: # если разрешения нет
            continue # в списке, то пропускаем этот файл
        out = end_papka+'/'+ out_filename + str(ch) + formafile 
        '''имя  нового файла'''
        try:
            img = Image.open(inp)
            w, h = img.size
            classname.out_print_list_copy_file_function(
                str(inp) + '\n - ' + out)
            if save_proportional:   
                if cut_bool:
                    img = scale_image(img, '', '', True, True,
                                      width=w_need, height=h_need)
                    img = obrezka_do_razmer(img, '', '', w_need, h_need)
                    '''обрезка изображения до указанных размеров'''
                    if give_ramka:
                        img = cutting_in_good_working(img, w_need, h_need)
                elif give_ramka:  
                    if save_proportional:
                        if h > w: # приведение к нужному размеру большей стороны
                            img = scale_image(img,'','',False, False, 
                                              height=h_need, width=w_need)
                        elif h < w:
                            img = scale_image(img,'','',False, False, 
                                              width=w_need, height=h_need)
                        else:
                            img = scale_image(img,'','',False, False, 
                                              width=w_need, height=h_need)    
                    img = cutting_in_good_working(img, w_need, h_need)
                    '''добавление черной рамки недостающим краям'''
                elif save_proportional:
                    if h > w: # приведение к нужному размеру большей стороны
                        img = scale_image(img,'','',False, False,
                                          width=w_need, height=h_need)
                    elif h < w:
                        img = scale_image(img,'','',False, False,
                                          width=w_need, height=h_need)
                    else:
                        img = scale_image(img,'','',False, False,
                                          width=w_need, height=h_need)      
            else:
                print('resize')
                img = img.resize((w_need, h_need), Image.ANTIALIAS)
            try:
                img.save(out, optimize=True, quality=kachestvo)
            except Exception as e:
                print('Непредвиденная ошибка при сохранении %s '% e, inp )
                word += '-------------Попытка исправить' + inp 
                word += '\n-------------Попытка исправить'+str(e)+ '\n'
                classname.out_print_list_copy_file_function(
                    'Непредвиденная ошибка при сохранении ')
                classname.out_print_list_copy_file_function(
                    str(e) + ' ' + inp + '\n')
                out = out[:-4:]+inp[-4::]
                classname.out_print_list_copy_file_function(
                    'Попытка исправить на ' + out + '\n')                     
                print('Попытка исправить на',out)
                img.save(out, optimize=True, quality=kachestvo)                
            
        except Exception as e:
            try:
                print('Непредвиденная ошибка %s '% e, [inp] ,[out])
                print('Идём дальше')
                word += inp+'\n'+str(e)+ '\n'
                classname.out_print_list_copy_file_function(
                    'не удалось исправить ошибку ' + e + ' ' + inp + "\n")                
                classname.out_print_list_copy_file_function('Идем дальше\n')
            except Exception:
                pass
        ch+=1
    
    f = open("exept.txt", 'w')
    f.write(word)
    f.close()    
    classname.out_print_list_copy_file_function(
        'Отчет об ошибках в файле exept.txt\n')
    
def obrezka_do_razmer(image,inp,out,w,h):
    im = image
    w_old, h_old = im.size
    if w_old > w:
        plus = (w_old - w)/2
        if plus%1!=0:
            w1 = int(plus)
            w2 = w_old - int(plus)-1
        else:
            w1 = int(plus)
            w2 = w_old - int(plus)
    else:
        w1 = 0
        w2  = w_old
    if h_old > h:
        plus = (h_old - h)/2
        if plus%1!=0:
            h1 = int(plus)
            h2 = h_old- int(plus)-1
        else:
            h1 = int(plus)
            h2 = h_old-int(plus)
    else:
        h1,h2 = 0,h_old
    im = im.crop((w1, h1, w2, h2))
    return im

def cutting_in_good_working(im,w,h):# для "обрезка для сохранения пропорций"
    w_old,h_old = im.size
    if w_old < w: 
        plus = (w_old - w)/2
        if plus%1!=0:
            w1 = int(plus)
            w2 = w_old - int(plus)+1
        else:
            w1 = int(plus)
            w2 = w_old - int(plus)
        print(w1,w2)
    else:
        w1,w2 = 0,w_old
    if h_old < h:
        plus = (abs(h_old - h))/2
        if plus%1!=0:
            h1 = -int(plus)
            h2 = h_old + int(plus)+1
        else:
            h1 = -int(plus)
            h2 = h_old + int(plus)
        print(h1,h2)
    else:
        h1,h2 = 0,h_old
    im = im.crop((w1, h1, w2, h2))
    return im

def scale_image(img,
                input_image_path, # Функция для сжатия
                output_image_path,
                sgatie, # для "сохранять пропорции"
                big_or_small_stor, # по боьшей или по меньшей сокращать
                width=None,
                height=None
                ):  
    original_image = img
    w, h = original_image.size
    wid = width
    hei = height     
    if big_or_small_stor:  #сокращение по большей стороне 
        print(100)
        if w < h:
            height = None
        elif w > h:
            width = None
        if width and height:
            max_size = (width, height)
        elif height:
            max_size = (int(height * w / h + 1), height)
        elif width:
            max_size = (width, int(width * h / w + 1))        
    else: #сокращение по меньшей стороне
        if w > h:
            height = None
        elif w < h:
            width = None
            
        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)  
        else:
            max_size = (wid, hei)
        print('---', max_size, '----')
        for i in range(10):
            original_image.thumbnail(max_size, Image.ANTIALIAS)#max_size
            w_n1, h_n1 = original_image.size
            if w_n1 < h_n1:
                if w_n1 < wid:
                    h_n1 += i
                elif w_n1 > wid:
                    h_n1 -= 1
                else:
                    break
            elif w_n1 > h_n1:
                if h_n1 < hei:
                    w_n1 += i  
                elif h_n1 > hei:
                    w_n1 -= 1
                else:
                    break
            else:
                break
            max_size = (w_n1, h_n1)
    original_image.thumbnail(max_size, Image.ANTIALIAS)#max_size
    return original_image
   
def main():
    
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window_save = window_save_class()
    ok_class = window_enter_class()
    window = grand_class(window_save, ok_class) # Создаём объект класса grand_class
    window_save.input_class(window)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение 
            
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    app1 = QApplication(sys.argv)
    main()
    sys.exit(app1.exec_())    