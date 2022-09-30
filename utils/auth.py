from turtle import end_poly
import PySimpleGUI as sg
import utils
from utils import var, authtest
from influxdb_client import InfluxDBClient

class AuthWin:

    sg.theme('darkgrey1')

    #@classmethod
    def authGui(self):
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
            if event in (sg.WIN_CLOSED, 'Cancel'):
                window.close()
            if event == 'Test':
                #utils.var.cmdRef()
                var.auth.url = values['url']
                var.auth.token = values['token']
                var.auth.org = values['org']
                print(var.auth.url, var.auth.token, var.auth.org)
                authtest.authTestLoop()
                #print(authtest.results)
            if event == 'Confirm':
                break
        window.close()
