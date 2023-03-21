from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

sg.theme("Material1")

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'job_track.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Fill out the following fields:')],
    [sg.Text('Employer', size=(15,2)), sg.InputText(key='Employer')],
    [sg.Text('Position', size=(15,1)), sg.InputText(key='Position')],
    [sg.Text('Status', size=(15,1)), sg.Combo(['Applied', 'Waiting for Interview', 'Rejected'], key='Status')],
    [sg.Text('Link', size=(15,1)), sg.InputText(key='Link')],
    [sg.Text('Date Applied', size=(15,1)), sg.InputText(key='Date Applied')],
    [sg.Text('Pay', size=(15,1)), sg.InputText(key='Pay')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Job Tracker', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Saved!')
        clear_input()
window.close()