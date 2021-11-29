
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ErrorElement   
from Code import *                     

sg.theme('LightBlue1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Source :')],
            [sg.Input(), sg.FolderBrowse()],
            [sg.Text('Destinetion :')],
            [sg.Input(), sg.FolderBrowse()],
            [sg.Button('Ok',key='ok')]
            ]

# Create the Window
window = sg.Window('Python project', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    s = values[0]
    d = values[1]
    print(event)
    print(values)
    if event == sg.WIN_CLOSED : # if user closes window 
        break
    elif event == 'ok':
        file_mover_e(s,d)


window.close()