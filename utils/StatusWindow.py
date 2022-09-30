import PySimpleGUI as sg
from utils.var import opsMetrics as om
import utils


class StatWin:

    sg.theme('darkgrey1')

    #@classmethod
    @staticmethod
    def statGui():
        ops = [[sg.Frame('Operational Metrics',
                     [[sg.Text('Status:'), sg.T(om.stat)],
                      [sg.Text('Current Operation: '), sg.T(om.opname)],
                      [sg.T('Current Orders:'),
                       sg.T(om.opsNum)]])
        ], [sg.Submit('Modify'), sg.B('Refresh')]]

        layout = [ops]

        window = sg.Window('AIGCC Operations', layout)
        while True:
            event, values = window.Read()
            #print(event)
            if event == sg.WIN_CLOSED:
                break
            if event == 'Refresh':
                utils.var.cmdRef()
            if event == 'Modify':
                break
        window.close()
