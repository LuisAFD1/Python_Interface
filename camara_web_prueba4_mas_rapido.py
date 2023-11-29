import PySimpleGUI as sg
import cv2
import numpy as np

sg.theme('LightGreen')

layout = [
    [sg.Image(filename='', key='image')],
    [sg.Radio('None', 'Radio', True, size=(10, 1))],
    [sg.Radio('threshold', 'Radio', size=(10, 1), key='thresh'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(40, 15), key='thresh_slider', tooltip='Threshold Value')],
    [sg.Radio('canny', 'Radio', size=(10, 1), key='canny'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='canny_slider_a', tooltip='Canny Lower Threshold'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='canny_slider_b', tooltip='Canny Upper Threshold')],
    [sg.Radio('contour', 'Radio', size=(10, 1), key='contour'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='contour_slider', tooltip='Contour Value'),
     sg.Slider((0, 255), 80, 1, orientation='h', size=(20, 15), key='base_slider', tooltip='Base Value')],
    [sg.Radio('blur', 'Radio', size=(10, 1), key='blur'),
     sg.Slider((1, 11), 1, 1, orientation='h', size=(40, 15), key='blur_slider', tooltip='Blur Kernel Size')],
    [sg.Radio('hue', 'Radio', size=(10, 1), key='hue'),
     sg.Slider((0, 225), 0, 1, orientation='h', size=(40, 15), key='hue_slider', tooltip='Hue Shift')],
    [sg.Radio('enhance', 'Radio', size=(10, 1), key='enhance'),
     sg.Slider((1, 255), 128, 1, orientation='h', size=(40, 15), key='enhance_slider', tooltip='Enhance Value')],
    [sg.Button('Exit', size=(10, 1))],
    [sg.Button('i', button_color=('black', 'white'), font=('Helvetica', 12, 'italic'), size=(2, 1), key='info_button')],
]

window = sg.Window('Procesamiento de imágenes en tiempo real OpenCV',
                   layout,
                   location=(800, 400),
                   finalize=True)

cap = cv2.VideoCapture(0)
desired_width = 300
desired_height = 300
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

while True:
    event, values = window.read(timeout=0, timeout_key='timeout')
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    
    ret, frame = cap.read()
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['image'].update(data=imgbytes)
    
    if values['thresh']:
        frame_processed = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[:, :, 0]
        frame_processed = cv2.threshold(frame_processed, values['thresh_slider'], 255, cv2.THRESH_BINARY)[1]
    
    elif values['canny']:
        frame_processed = cv2.Canny(frame, values['canny_slider_a'], values['canny_slider_b'])
    
    elif values['contour']:
        hue = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hue = cv2.GaussianBlur(hue, (21, 21), 1)
        hue = cv2.inRange(hue, np.array([values['contour_slider'], values['base_slider'], 40]),
                          np.array([values['contour_slider'] + 30, 255, 220]))
        cnts = cv2.findContours(hue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        frame_processed = frame.copy()
        cv2.drawContours(frame_processed, cnts, -1, (0, 0, 255), 2)
    
    elif values['blur']:
        frame_processed = cv2.GaussianBlur(frame, (21, 21), values['blur_slider'])
    
    elif values['hue']:
        frame_processed = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_processed[:, :, 0] += int(values['hue_slider'])
        frame_processed = cv2.cvtColor(frame_processed, cv2.COLOR_HSV2BGR)
    
    elif values['enhance']:
        enh_val = values['enhance_slider'] / 40
        clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        frame_processed = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    else:
        frame_processed = frame  # No processing
    
    imgbytes_processed = cv2.imencode('.png', frame_processed)[1].tobytes()
    window['image'].update(data=imgbytes_processed)

window.close()
cap.release()
cv2.destroyAllWindows()

