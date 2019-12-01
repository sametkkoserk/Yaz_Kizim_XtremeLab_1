# XTREMELAB 1

# Samet Köser
# Salih Kuloğlu
# Reyhan Yürük
# Serkan Helvacıoğlu
# Elif Ünlü

# References:
# https://gist.github.com/mertyildiran/957b8c9f7631f6ab7f21 : sound to text
# https://realpython.com/python-encodings-guide/ : unicode
# https://www.8bitavenue.com/python-convert-unicode-to-string/ : unicode
# https://github.com/UB-Mannheim/tesseract/wiki : tesseract
# https://developer.ibm.com/tutorials/document-scanner/ : image to text
# https://www.linkedin.com/pulse/pythonda-sesli-asistan-olu%C5%9Fturmak-yunus-emre-g%C3%BCndo%C4%9Fmu%C5%9F/ : text to sound
# https://medium.com/nerd-stuff/python-script-to-turn-text-message-abbreviations-into-actual-phrases-d5db6f489222 : translator


import webbrowser

from tkinter import filedialog
from tkinter import *
import csv
import re
from gtts import gTTS
import os
from PIL import Image
import pytesseract
from unicode_tr.extras import slugify
import speech_recognition as sr
import pickle
import codecs



class Gui(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self,parent)
        self.initUI()

    def initUI(self):

        self.frame=Frame(bg="orange")
        self.frame.grid()

        self.caption = Label(self.frame, text="YAZ KIZIM", bg="purple", fg="white", font=("", "25", "bold"))
        self.caption.grid(row=0, column=0, columnspan=6, sticky=EW)

        self.textbox=Text(self.frame, width=50)
        self.textbox.grid(row=1, rowspan=2, column=0, padx=20, pady=20)

        self.dosya_ekle = Button(self.frame, text="Dosya Ekle", width=20, height=3, command = obj.select_file)
        self.dosya_ekle.grid(row=1, column=2, sticky=N, pady=30)

        self.duzelt_buton = Button(self.frame, text="Düzelt", width=20, height=3, command=obj.düzelt)
        self.duzelt_buton.grid(row=1, column=2, sticky=S, pady=25)

        self.ozet = Label(self.frame, text="XTREMELAB 1", width=20, height=3, font=("", "12", "bold"))
        self.ozet.grid(row=2, column=2, sticky=N, pady=25)

        self.m_s_cevir = Button(self.frame, text="Metni Sese Çevir", width=20, height=3, command=obj.ses)
        self.m_s_cevir.grid(row=2, column=2, sticky=S, pady=30)

        self.r_m_cevir = Button(self.frame, text="Resimden Metine Çevir", width=20, height=3, command=obj.image_text)
        self.r_m_cevir.grid(row=3, column=0, pady=20)

        self.r_s_cevir = Button(self.frame, text="Resimden Sese Çevir", width=20, height=3, command=obj.image_sound)
        self.r_s_cevir.grid(row=4, column=0, pady=10)

        self.s_m_cevir = Button(self.frame, text="Sesi Metine Çevir", width=20, height=3, command=obj.sound_text)
        self.s_m_cevir.grid(row=3, column=2, pady=20)

        self.xtreme = Button(self.frame, text="XtremeLab", width=20, height=3, font=("", "8", "bold"), command=obj.link_button)
        self.xtreme.grid(row=4, column=2)

        self.textbox2=Text(self.frame, width=50)
        self.textbox2.grid(row=1, rowspan=2, column=3, padx=30, pady=20,sticky=E)


class AcikHack():
    def __init__(self):
        self.str = ''

    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        f = open(self.filename, 'r')
        str = ''
        for i in f:
            str += i
        app.textbox.insert(END, str)
        obj.str += str

    def düzelt(self):
        def translator(user_string):
            user_string = user_string.split(" ")
            j = 0
            for _str in user_string:
                _str = _str.strip()
                fileName = "C:\\Users\\reyhanyuruk\\Desktop\\data.txt"

                accessMode = "r"
                with codecs.open(fileName, accessMode, encoding='utf-8') as myCSVfile:

                    dataFromFile = csv.reader(myCSVfile, delimiter="=")

                    str = re.sub('[^a-zA-Z0-9-.]', '', _str)
                    for row in dataFromFile:

                        if _str.upper() == row[0]:
                            user_string[j] = row[1]
                    myCSVfile.close()
                j = j + 1

            app.textbox2.insert(END, ' '.join(user_string))
        if obj.str != '':
            translator(obj.str)
        elif obj.str == '':
            translator(app.textbox.get("1.0", END))

    def ses(self):
        tts = gTTS(text=app.textbox2.get("1.0", END), lang='tr')

        tts.save('ses.mp3')

        os.system('ses.mp3')


    def image_text(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpg files", "*.jpg"),("png files", "*.png"), ("all files", "*.*")))
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        self.text = slugify(pytesseract.image_to_string(Image.open(self.filename)))
        for i in self.text.split('-'):
            app.textbox.insert(END, i+' ')

    def image_sound(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
                                                              ("all files", "*.*")))
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        self.text = pytesseract.image_to_string(Image.open(self.filename))

        tts = gTTS(self.text, lang='tr')

        tts.save('image.mp3')

        os.system('image.mp3')

    def sound_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Dinliyorum..")

            audio = r.listen(source)
            audio_file = open('audio.pkl', 'wb')
            pickle.dump(audio, audio_file)

            audio_file = open('audio.pkl', 'rb')
            audio = pickle.load(audio_file)

            f = codecs.open('text.txt', 'w', encoding='utf-8')
        try:
            print("You said:  " + r.recognize_google(audio, language="tr-TR"))
            sr_output = r.recognize_google(audio, language="tr-TR")
            kelimeler = slugify(sr_output)
            for kelime in kelimeler.split('-'):
                f.write(kelime)
                f.write(' ')
                app.textbox.insert(END, kelime+' ')
        except sr.UnknownValueError as  e:
            print("Google Speech Recognition could not understand audio", str(e))
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def link_button(self):
        webbrowser.open("https://www.instagram.com/sehirxtreme/")



obj = AcikHack()
window = Tk()
window.title("YAZ KIZIM")
window.geometry("1100x643+100+30")
app = Gui(window)
window.mainloop()
