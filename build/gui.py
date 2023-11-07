from cProfile import label
from logging import PlaceHolder
import sys
import math
import os
import tkinter.messagebox as tmsg
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Jakub\Desktop\design\build\assets\frame0")


    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x1000")
window.configure(bg = "#F7EFE5")

def CesarEncrypt():
    string = entry_3.get()
    string = string.upper()
    k = int(entry_2.get())
    
    encrypted_text = ""
    if k > 26 or k == 0:
        warning="Klucz moze zawierac wartosci od 1 do 26"
        tmsg.showwarning("Popraw klucz", warning)
    else: 
        for i in range(len(string)):
            ch = string[i]
            if ch==" ":
                encrypted_text+=" "
            elif (ch.isupper()):
                encrypted_text += chr((ord(ch) + k-65) % 26 + 65)
            else:
                encrypted_text += chr((ord(ch) + k-97) % 26 + 97)
            
    canvas.itemconfig(tagOrId=wynik, text=encrypted_text)
    return encrypted_text

def CesarDecypher():
    decrypted_text = ""
    string = entry_1.get().strip()
    
    letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = int(entry_2.get())
    if k > 26 or k == 0:
        warning="Klucz moze zawierac wartosci od 1 do 26"
        tmsg.showwarning("Popraw klucz", warning)
    else:
        for ch in string:

            if ch in letters:
                position = letters.find(ch)
                new_pos = (position - k) % 26
                new_char = letters[new_pos]
                decrypted_text += new_char
            else:
                decrypted_text += ch
    canvas.itemconfig(tagOrId=wynik, text=decrypted_text)
    return decrypted_text

def vigenere_encrypt():
    string = entry_3.get()
    string = string.upper()
    k = entry_2.get()
    encrypted_text = ""
    key_length = len(k)

    for i in range(len(string)):
        char = string[i]
        if char.isalpha():
            key_char = k[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    canvas.itemconfig(tagOrId=wynik, text=encrypted_text)
    return encrypted_text

def vigenere_decrypt():
    string = entry_1.get()
    string = string.upper()
    k = entry_2.get()
    decrypted_text = ""
    key_length = len(k)

    for i in range(len(string)):
        char = string[i]
        if char.isalpha():
            key_char = k[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    canvas.itemconfig(tagOrId=wynik, text=decrypted_text)
    return decrypted_text

def Transpozycja_encrypt():

    try:
        key = int(float(entry_2.get()))
        message = entry_3.get()
        ciphertext = [''] * key
        if key > 26 or key == 0:
            warning="Klucz moze zawierac wartosci od 1 do 26"
            tmsg.showwarning("Popraw klucz", warning)
        else:
            for column in range(key):
                currentIndex = column
                while currentIndex < len(message):
                    ciphertext[column] += message[currentIndex]
                    currentIndex += key
                    canvas.itemconfig(tagOrId=wynik, text= ''.join(ciphertext))
        return ''.join(ciphertext)
                    
    except ValueError:
        warning="Klucz moze zawierac wartosci od 1 do 26"
        tmsg.showwarning("Popraw klucz", warning)  
            
        

    
def Transpozycja_decrypt():
    try:
        key = int(float(entry_2.get()))
        message = entry_1.get()
        if key > 26 or key == 0:
            warning="Klucz moze zawierac wartosci od 1 do 26"
            tmsg.showwarning("Popraw klucz", warning)
        else:
                numOfColumns = int(math.ceil(len(message) / float(key)))
                numOfRows = key
                numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
                plaintext = [''] * numOfColumns
                column = 0
                row = 0

                for symbol in message:
                    plaintext[column] += symbol
                    column += 1
                    if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                        column = 0
                        row += 1
                canvas.itemconfig(tagOrId=wynik, text= ''.join(plaintext))
        return ''.join(plaintext)

    except ValueError:
        warning="Klucz moze zawierac wartosci od 1 do 26"
        tmsg.showwarning("Popraw klucz", warning)  
        
canvas = Canvas(
    window,
    bg = "#F7EFE5",
    height = 1000,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=CesarDecypher,
    relief="flat"
)
button_1.place(
    x=100.0,
    y=765.0,
    width=180.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=vigenere_decrypt,
    relief="flat"
)
button_2.place(
    x=300.0,
    y=763.0,
    width=180.0,
    height=52.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Transpozycja_decrypt,
    relief="flat"
)
button_3.place(
    x=500.0,
    y=765.0,
    width=180.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=700.0,
    y=764.0,
    width=180.0,
    height=51.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=900.0,
    y=765.0,
    width=180.0,
    height=50.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=CesarEncrypt,
    relief="flat"
)
button_6.place(
    x=110.0,
    y=501.0,
    width=180.0,
    height=50.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=vigenere_encrypt,
    relief="flat"
)
button_7.place(
    x=310.0,
    y=499.0,
    width=180.0,
    height=52.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=Transpozycja_encrypt,
    relief="flat"
)
button_8.place(
    x=510.0,
    y=501.0,
    width=180.0,
    height=50.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=710.0,
    y=500.0,
    width=180.0,
    height=51.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=910.0,
    y=501.0,
    width=180.0,
    height=50.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    600.0,
    682.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C3ACD0",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=124.0,
    y=637.0,
    width=952.0,
    height=88.0
)

canvas.create_text(
    469.0,
    604.0,
    anchor="nw",
    text="Tekst do odkodowania",
    fill="#7743DB",
    font=("Inter Bold", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    600.0,
    401.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C3ACD0",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=124.0,
    y=356.0,
    width=952.0,
    height=88.0
)

canvas.create_text(
    567.0,
    323.0,
    anchor="nw",
    text="Klucz",
    fill="#7743DB",
    font=("Inter Bold", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    600.0,
    251.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C3ACD0",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=124.0,
    y=206.0,
    width=952.0,
    height=88.0
)

canvas.create_text(
    469.0,
    173.0,
    anchor="nw",
    text="Tekst do zakodowania",
    fill="#7743DB",
    font=("Inter Bold", 24 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1200.0,
    120.0,
    fill="#7743DB",
    outline="")

canvas.create_text(
    100.0,
    10.0,
    anchor="nw",
    text="Aplikacja na Kryptografie",
    fill="#C3ACD0",
    font=("Inter 64 bold")
)
canvas.create_text(
    565.0,
    840.0,
    anchor="nw",
    text="Wynik:",
    fill="#7743DB",
    font=("Inter Bold", 24 * -1)
)
wynik = canvas.create_text(
    0.0,
    880.0,
    anchor="nw",
    text="",
    fill="#7743DB",
    font=("Inter Bold", 24 * -1)
)


window.resizable(False, False)
window.mainloop()
