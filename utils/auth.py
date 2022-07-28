import PySimpleGUI as sg
import utils

class AuthWin:

    sg.theme('darkgrey1')

    #@classmethod
    def authGui():
        auth = [[sg.Frame('Operational Metrics',
                     [[sg.Text('Host:'), sg.Input(k='url')],
                      [sg.Text('Token: '), sg.Input(k='token')],
                      [sg.T('Org:'), sg.Input(k='org')]])
        ], [sg.Submit('Confirm'), sg.B('Test'), sg.B('Cancel')]]

        keys = ['url', 'token', 'org']

        layout = [auth]

        window = sg.Window('AIGCC Authentication', layout)
        while True:
            event, values = window.Read()
            #print(event)
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Test':
                #utils.var.cmdRef()
                print(utils.var.auth.url)
                values['url']=utils.var.auth.url
                #window['Order#'](value=var.commandvals.V0)                
                break
            if event == 'Modify':
                break
        window.close()
