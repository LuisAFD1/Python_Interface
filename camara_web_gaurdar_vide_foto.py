import PySimpleGUI as sg
import cv2
import numpy as np
import os

sg.theme('LightGreen')

layout = [
    [sg.Image(filename='', key='image')],
    [sg.Radio('None', 'Radio', True, size=(10, 1))],
    # ... (otros elementos)
    [sg.Button('Take Photo', size=(10, 1), key='take_photo')],
    [sg.Button('Record Video', size=(10, 1), key='record_video')],
    [sg.Button('Exit', size=(10, 1))],
    [sg.Button('i', button_color=('black', 'white'), font=('Helvetica', 12, 'italic'), size=(2, 1), key='info_button')],
]

window = sg.Window('Procesamiento de imágenes en tiempo real OpenCV',
                   layout,
                   location=(800, 400),
                   finalize=True)

cap = cv2.VideoCapture(0)
desired_width = 1300
desired_height = 1200
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

recording = False
out = None
save_path = ''

while True:
    event, values = window.read(timeout=0, timeout_key='timeout')
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    
    if event == 'take_photo':
        save_path = sg.popup_get_file('Choose a location to save the photo', save_as=True, default_extension='.png')
        if save_path:
            cv2.imwrite(save_path, frame)
            sg.popup(f'Photo saved as "{os.path.basename(save_path)}"')
    
    elif event == 'record_video':
        if not recording:
            recording = True
            save_path = sg.popup_get_file('Choose a location to save the video', save_as=True, default_extension='.avi')
            if save_path:
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(save_path, fourcc, 20, (int(cap.get(3)), int(cap.get(4))))
                window['record_video'].update(text='Stop Recording')
        else:
            recording = False
            window['record_video'].update(text='Record Video')
            if out:
                out.release()
                sg.popup(f'Video recording saved as "{os.path.basename(save_path)}"')
                out = None

    ret, frame = cap.read()
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['image'].update(data=imgbytes)
    
    # ... (resto de tu código para el procesamiento de imágenes)

    if recording and out is not None:
        out.write(frame)

window.close()
cap.release()
cv2.destroyAllWindows()
