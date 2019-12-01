# Yaz_Kizim_XtremeLab_1
 Bilişim Vadisi AçıkHack Projesi 2019
YAZ KIZIM
XtremeLab 1 takımı olarak yaptığımız proje Türkçe Dil işleme tabanlı görüntü ve ses işleme üzerinedir. Farklı durumlarda insanların ihtiyaç duyabileceği özellikleri barındırmaktadır. Özellikler aşağıdaki şekildedir.

Prerequisites:
python 3.7.1
import webbrowser
from tkinter import filedialog
from tkinter import *
import csv
import reac
from gtts import gTTS
import os
from PIL import Image
import pytesseract
from unicode_tr.extras import slugify
import speech_recognition as sr
import pickle
import codecs


Özellikler:

-Görseli metne dönüştürüp bilgisayara kaydetme(.txt)
obj.image_text()

-Alınan görseli sese çevirme(.mp3, .wav, .mp4)
obj.image_sound()

-Girilen metni doğal dil işlemeye göre düzenleme
obj.düzelt()

-Alınan metni düzenleyerek ses dosyasına çevirme
obj.ses()

-Anlık konuşmayı metne çevirme
obj.sound_text()


Versioning:
1.0

Authors:
# Samet Köser
# Salih Kuloğlu
# Reyhan Yürük
# Serkan Helvacıoğlu
# Elif Ünlü

License:
This project is licensed under the MIT License - see the LICENSE.md file for details
