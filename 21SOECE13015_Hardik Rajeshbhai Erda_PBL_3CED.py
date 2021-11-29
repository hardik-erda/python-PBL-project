import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ErrorElement   
import os

def is_extnation(value):
    str=''
    #this will return a tuple of root and extension
    split_tup = os.path.splitext(str.join(value))
    print(split_tup)

    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]

    return file_extension

def re(count,sub_dir,f,source,destination):
        try:
            os.rename(source+'/' + f, destination+'/'+sub_dir+'/'+str(count)+'_' + f)
            count +=1
        except:
            count+=1
            re(count,sub_dir,f,source,destination)

def file_mover_e(source,destination):
    # count for add same file name with number like hi.txt then 2_hi.txt 
    count=2
    
    allfiles = os.listdir(source)
    for f in allfiles:
        #skip if f is folder
        if is_extnation(f) == '':
            continue
        try:
            sub_dir = is_extnation(f)
            if sub_dir == '':
                print("sub_dir: ",sub_dir)
                continue
            path = os.path.join(destination,sub_dir)
            os.mkdir(path)
            print("dir created.")
            os.rename(source+'/' + f, destination+'/'+sub_dir+'/' + f)
        except :
                try:
                    os.rename(source+'/' + f, destination+'/'+sub_dir+'/' + f)
                except:
                    print("same name file exiested..")
                    try:
                        os.rename(source+'/' + f, destination+'/'+sub_dir+'/'+str(count)+'_' + f)
                        count +=1
                    except FileExistsError:
                        print(re)
                        re(count,sub_dir,f,source,destination)

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