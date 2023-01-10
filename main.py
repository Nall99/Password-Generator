import PySimpleGUI as sg
import string
import secrets
import pyperclip

sg.theme('DarkBlue')

layout = [
    [sg.Text('Size: '), sg.Input(key='len')],
    [sg.Button('Generator', key="generator"), sg.Text('', key='password')],
    [sg.Button('Copy', key='copy'), sg.Text('',key='copy_menssage')]
]

window = sg.Window('Password Generator', layout=layout, size= (290,100))

def password(pwd_length):
    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    speial_chars = string.punctuation

    alphabet = letters + digits + speial_chars

    # generate a password string
    pwd = ''
    for _ in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

text = ''

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'generator':
        pwd_length = 0
        if values['len'].isnumeric():
            pwd_length = int(values['len'])
            text = password(pwd_length)
            window['password'].update(text)
            window['copy_menssage'].update('')
        else:
            window['password'].update("[ERRO] Please write just numbers")
    elif event == 'copy':
        pyperclip.copy(text)
        window['copy_menssage'].update('Successy copied')

window.close()
