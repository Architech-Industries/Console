import sys
import PySimpleGUI as sg
from utils import var
import time

class CommandMenu:

    sg.theme('darkgrey1')

    def collapse(Layout, key):
        return sg.pin(sg.Column(Layout, key=key))


    def CCGUI(self):
        sg.SetOptions(text_justification='right')
        flags = [ 
                  ##__Execution Area__##
                  [sg.Frame('Command Configuration',
                    [[sg.Text('Order:', size=(8, 1)), sg.Spin(values=list(range(0, 6)), initial_value=None, size=(6, 1), key='Order#'),
                      sg.Text('Cat:', size=(8, 1)), sg.Spin(values=list(range(0, 10)), initial_value=0, size=(6, 1), key='Category')],
                    [sg.Text('Edict:', size=(8, 1)), sg.Spin(values=list(range(0, 1000)), initial_value=0, size=(6, 1), key='Edict#'), 
                      sg.Text('Priority:', size=(8, 1)), sg.Spin(values=list(range(0, 1000)), initial_value=0, size=(6, 1), key='Priority')],
                    [sg.Text('Protocol:', size=(8, 1)), sg.Spin(values=list(range(0, 1000)), initial_value=0, size=(6, 1), key='Protocol#'), 
                      sg.Text('Auth:', size=(8, 1)), sg.Spin(values=list(range(0, 10)), initial_value=0, size=(6, 1), key='Auth')],
                    [sg.Text('Stage:', size=(8, 1)), sg.Spin(values=list(range(0, 10)), initial_value=0, size=(6, 1), key='Stage'), 
                      sg.Text('Alarm:', size=(8, 1)), sg.Drop(values=('Yes', 'No', None), default_value='None', auto_size_text=True, key='Alarm Status')]])],

                  [sg.CB('Augmentations', k='-AUGSCheckbox-', default=False, enable_events=True),
                   sg.CB('Options', k='-OPTCheckbox-', default=False, enable_events=True)]]
                  
                  #[sg.Frame('Augmentations',
                    #[[sg.Radio('Emergency', 'loss', size=(12, 1)), 
                      #sg.Radio('Standard', 'loss', default=True, size=(12, 1))],
                      #[sg.Radio('Delay', 'loss', size=(12, 1)), 
                      #sg.Radio('Reset', 'loss', size=(12, 1))],
                      #[sg.Radio('Nuke', 'loss', size=(12, 1)), 
                      #sg.Radio('Other', 'loss', size=(12, 1))]])],

                  
                  ##__Option Area__##
        option_window = [
                  [sg.Checkbox('Select All', size=(12, 1), k='-SALLCheckbox-', default=False, enable_events=True), 
                   sg.Checkbox('Select None', size=(20, 1), k='-CALLCheckbox-', default=False, enable_events=True)],
                  [sg.Checkbox('Orders', k='-ORDCheckbox-', size=(12, 1), default=False, enable_events=True), 
                   sg.Checkbox('Edicts', k='-EDCCheckbox-', enable_events=True, size=(20, 1))],
                  [sg.Checkbox('Protocols', k='-PTLCheckbox-', enable_events=True, size=(12, 1)), 
                   sg.Checkbox('Authorizations', k='OK', size=(20, 1), default=False)],
                  [sg.Checkbox('Exec', k='OEX', size=(12, 1)), 
                   sg.Checkbox('Repeat', k='OR', size=(20, 1))],
                  [sg.Checkbox('Force', k='OF', size=(12, 1), default=False), 
                   sg.Checkbox('Override', k='OOR', size=(20, 1))],
                  [sg.Checkbox('Contain', k='OC', size=(12, 1)), 
                   sg.Checkbox('Flush', k='OFL', size=(20, 1), default=False)],
                  [sg.Checkbox('Re-Seed', k='OS', size=(12, 1)), 
                   sg.Checkbox('Debug', size=(20, 1), key='-DBGCheckbox-', enable_events=True, default=False)]]
                
                  ##__Augmentation Window__##

        aug_window =    [
                          [sg.Radio('Emergency', 'loss', size=(12, 1)), 
                          sg.Radio('Standard', 'loss', default=True, size=(12, 1))],
                          [sg.Radio('Delay', 'loss', size=(12, 1)), 
                          sg.Radio('Reset', 'loss', size=(12, 1))],
                          [sg.Radio('Nuke', 'loss', size=(12, 1)), 
                          sg.Radio('Other', 'loss', size=(12, 1))]
                        ]  
                                
        
        debug_window =  [
                          [sg.Text(time.strftime("%H:%M:%S", time.gmtime(var.commandvals.run_time)))], 
                          [sg.Text('Seed: ', key='SEEDS'), 
                          sg.Text(var.commandvals.rseed)],
                          [sg.Text('RValue: '),
                          sg.Text(var.commandvals.rvalue)]
                        ]

        orders_window = [
                        [sg.Radio('0', 'orders', k='O0', size=(12, 1))], 
                        [sg.Radio('1', 'orders', k='O1', size=(20, 1))],
                        [sg.Radio('2', 'orders', k='O2', size=(12, 1))], 
                        [sg.Radio('3', 'orders', k='O3', size=(20, 1))],
                        [sg.Radio('4', 'orders', k='O4', size=(12, 1))], 
                        [sg.Radio('5', 'orders', k='O5', size=(20, 1))],
                        [sg.Radio('6', 'orders', k='O6', size=(12, 1))], 
                        [sg.Radio('7', 'orders', k='O7', size=(20, 1))],
                        [sg.Button('Confirm', k='Confirm_Order'), sg.Button('Return', k='Close_Orders')]
                        ]

        edict_window =  [
                        [sg.Radio('0', 'edicts', k='E0', size=(12, 1))], 
                        [sg.Radio('1', 'edicts', k='E1', size=(20, 1))],
                        [sg.Radio('2', 'edicts', k='E2', size=(12, 1))], 
                        [sg.Radio('3', 'edicts', k='E3', size=(20, 1))],
                        [sg.Radio('4', 'edicts', k='E4', size=(12, 1))], 
                        [sg.Radio('5', 'edicts', k='E5', size=(20, 1))],
                        [sg.Radio('6', 'edicts', k='E6', size=(12, 1))], 
                        [sg.Radio('7', 'edicts', k='E7', size=(20, 1))],
                        [sg.Button('Confirm', k='Confirm_Edict'), sg.Button('Return', k='Close_Edicts')]
                        ]    

        protocol_window = [
                        [sg.Radio('0', 'protocols', k='P0', size=(12, 1))], 
                        [sg.Radio('1', 'protocols', k='P1', size=(20, 1))],
                        [sg.Radio('2', 'protocols', k='P2', size=(12, 1))], 
                        [sg.Radio('3', 'protocols', k='P3', size=(20, 1))],
                        [sg.Radio('4', 'protocols', k='P4', size=(12, 1))], 
                        [sg.Radio('5', 'protocols', k='P5', size=(20, 1))],
                        [sg.Radio('6', 'protocols', k='P6', size=(12, 1))], 
                        [sg.Radio('7', 'protocols', k='P7', size=(20, 1))],
                        [sg.Button('Confirm', k='Confirm_Protocol'), sg.Button('Return', k='Close_Protocol')]
                        ]
        ## Option Frames
        console   = [[sg.Frame('Console', layout = flags)]]
        debug     = [[sg.Frame('Debug', layout = debug_window)]]
        orders    = [[sg.Frame('Order Selection', layout = orders_window)]]
        edicts    = [[sg.Frame('Edict Selection', layout = edict_window)]]
        protocols = [[sg.Frame('Protocol Selection', layout = protocol_window)]]
        augs      = [[sg.Frame('Augmentations', layout = aug_window)]]
        options   = [[sg.Frame('Options', layout = option_window)]]

        ## Layout for the main Window
        layout = [
                  [
                  sg.Column(console), 
                  ],
                  [
                  CommandMenu.collapse(orders, '-ORDWindow-'), 
                  CommandMenu.collapse(edicts, '-EDCWindow-'), 
                  CommandMenu.collapse(protocols, '-PTLWindow-'), 
                  CommandMenu.collapse(debug, '-DBGWindow-')
                  ],
                  [[CommandMenu.collapse(augs, '-AUGWindow-'), CommandMenu.collapse(options, '-OPTWindow-')]],
                  [sg.Submit('Execute'), sg.Button('Clear Options', k='Clear'), sg.Button('Reset'), sg.Cancel()],
                 ]


        keys = ['Order#', 'Category', 'Edict#', 'Priority', 'Protocol#', 'Auth', 'Alarm Status', '-SALLCheckbox-', '-CALLCheckbox-','-ORDCheckbox-','-EDCCheckbox-','-PTLCheckbox-','OK','OEX','OR','OF','OOR','OC','OFL','OS','-DBGCheckbox-']

        window = sg.Window('Ai Galactic Command Console', layout, finalize=True, font=("Technic", 12))
        
        def selectNone():
          pass

        def closeWinAll():
            closeWinD()
            closeWinO()
            closeWinE()
            closeWinP()
            closeAugs()
            closeOpts()

        def openWinAll():
            openWinD()
            openWinO()
            openWinE()
            openWinP()
        
        def closeAugs():
            window['-AUGSCheckbox-'](False)
            window['-AUGWindow-'](visible=False)

        def openAugs():
            window['-AUGSCheckbox-'](True)
            window['-AUGWindow-'](visible=True)

        def closeOpts():
            window['-OPTCheckbox-'](False)
            window['-OPTWindow-'](visible=False)

        def openOpts():
            window['-OPTCheckbox-'](True)
            window['-OPTWindow-'](visible=True)

        def closeWinD():
            window['-DBGCheckbox-'](False)
            window['-DBGWindow-'](visible=False)

        def openWinD():
            window['-DBGCheckbox-'](True)
            window['-DBGWindow-'](visible=True)

        def closeWinO():
            window['-ORDCheckbox-'](False)
            window['-ORDWindow-'](visible=False)

        def openWinO():
            window['-ORDCheckbox-'](True)
            window['-ORDWindow-'](visible=True)

        def closeWinE():
            window['-EDCCheckbox-'](False)
            window['-EDCWindow-'](visible=False)

        def openWinE():
            window['-EDCCheckbox-'](True)
            window['-EDCWindow-'](visible=True)

        def closeWinP():
            window['-PTLCheckbox-'](False)
            window['-PTLWindow-'](visible=False)

        def openWinP():
            window['-PTLCheckbox-'](True)
            window['-PTLWindow-'](visible=True)

        def resetAll():
            #for key in keys:
                #window[key](None)
            closeWinAll()
            window['-SALLCheckbox-'](False)
            window['-CALLCheckbox-'](False)

        sg.SetOptions(text_justification='left')
        ## Closes all Option Windows at launch
        closeWinAll()
        
        while True:
            event, values = window.Read()
            running_time = (time.time() - var.commandvals.start_time)
            time.strftime("%H:%M:%S", time.gmtime(running_time))
            var.commandvals.run_time = running_time
            print(time.strftime("%H:%M:%S", time.gmtime(var.commandvals.run_time)))
            window.un_hide
            if values['-DBGCheckbox-'] is True:
                 openWinD()

            if values['-DBGCheckbox-'] is False:
                closeWinD()

            if values['-ORDCheckbox-'] is True:
                openWinO()
                if event == 'Confirm_Order':
                    if values['O0'] is True:
                        var.commandvals.OS0 = True
                    else:
                        var.commandvals.OS0 = False
                    var.commandvals.OS1 = values['O1']
                    var.commandvals.OS2 = values['O2']
                    var.commandvals.OS3 = values['O3']
                    var.commandvals.OS4 = values['O4']
                    var.commandvals.OS5 = values['O5']
                    var.commandvals.OS6 = values['O6']
                    var.commandvals.OS7 = values['O7']
                    var.orderselection()
                    print(var.commandvals.V0)
                    values['Order#']=var.commandvals.V0
                    window['Order#'](value=var.commandvals.V0)
                    print('\n')
                    print(values['Order#'])
                if event =='Close_Orders':
                    closeWinO()

            if values['-ORDCheckbox-'] is False:
                 closeWinO()

            if values['-EDCCheckbox-'] is True:
                openWinE()
                if event == 'Confirm_Edict':
                    var.commandvals.E1 = values['E0']
                    var.commandvals.E1 = values['E1']
                    var.commandvals.E2 = values['E2']
                    var.commandvals.E3 = values['E3']
                    var.commandvals.E4 = values['E4']
                    var.commandvals.E5 = values['E5']
                    var.commandvals.E6 = values['E6']
                    var.commandvals.E7 = values['E7']
                    var.edictselection()
                    print(var.commandvals.V3)
                    values['Edict#']=var.commandvals.V3
                    window['Edict#'](value=var.commandvals.V3)
                    print('\n')
                    print(values['Edict#'])
                if event =='Close_Edicts':
                    closeWinE()

            if values['-EDCCheckbox-'] is False:
                 closeWinE()

            if values['-PTLCheckbox-'] is True:
                openWinP()
                if event == 'Confirm_Protocol':
                    var.commandvals.E1 = values['P0']
                    var.commandvals.E1 = values['P1']
                    var.commandvals.E2 = values['P2']
                    var.commandvals.E3 = values['P3']
                    var.commandvals.E4 = values['P4']
                    var.commandvals.E5 = values['P5']
                    var.commandvals.E6 = values['P6']
                    var.commandvals.E7 = values['P7']
                    var.edictselection()
                    print(var.commandvals.V3)
                    values['Protocol#']=var.commandvals.V3
                    window['Protocol#'](value=var.commandvals.V3)
                    print('\n')
                    print(values['Protocol#'])
                if event =='Close_Protocol':
                    closeWinP()

            if values['-PTLCheckbox-'] is False:
                 closeWinP()

            if values['-SALLCheckbox-'] is True:
                 openWinAll()
                 window['-CALLCheckbox-'](False)
                 window['-SALLCheckbox-'](False)

            if values['-CALLCheckbox-'] is True:
                 closeWinAll()
                 window['-SALLCheckbox-'](False)
                 #window['-CALLCheckbox-'](True)

            if event =='Reset':
                resetAll()   

            if event =='Clear':
                closeWinAll()

            if event =='Execute':
                var.commandvals.V0 = values['Order#']
                ## Input Validation - Must be positive Int
                try:
                    var.commandvals.V0 = int(var.commandvals.V0)
                except:
                    sg.Popup('Invalid Order Entered')
                    continue
                if var.commandvals.V0 < 0:
                    sg.Popup('Order must be a positive number')
                    continue

                var.commandvals.V1 = values['Category']
                var.commandvals.V2 = values['Edict#']
                var.commandvals.V3 = values['Priority']
                var.commandvals.V4 = values['Protocol#']
                var.commandvals.V5 = values['Auth']
                var.commandvals.V6 = values['Stage']
                var.commandvals.V7 = values['Alarm Status']
                var.valueprinter()
                var.opsUpdate()
                #Debug Section, Uncomment to print variables
                #print(var.commandvals.V0)
                #print(var.commandvals.order)
                break
								
            if values['-OPTCheckbox-'] is True:
                openOpts()

            if values['-OPTCheckbox-'] is False:
                closeWinAll()

            if values['-AUGSCheckbox-'] is True:
                 openAugs()

            if values['-AUGSCheckbox-'] is False:
                closeAugs()

            if event =='Cancel':
                window.Close()
          
        
        #debug values
        #print(button, values)
        
        #var.valueprinter()

        #sg.Popup('lol')
        window.Hide()
def execstats():
    layout = [
							[sg.Text('Commands Issued: ')],
              [[sg.Text('Order:     '), sg.Text(var.commandvals.V0)]],
              [sg.Text('Category:'), sg.Text(var.commandvals.V1)],
              [sg.Text('Edict:       '), sg.Text(var.commandvals.V2)],
              [sg.Text('Priority:   '), sg.Text(var.commandvals.V3)],
              [sg.Text('Protocol: '), sg.Text(var.commandvals.V4)],
              [sg.Text('Auth:       '), sg.Text(var.commandvals.V5)],
              [sg.Text('Stage:     '), sg.Text(var.commandvals.V6)],
              [sg.Submit('Confirm'), sg.Cancel()]
             ]

    window = sg.Window('Execution Confirmation').Layout(layout)

    button, values = window.Read()
    if button == 'Cancel':
        window.Close()
        var.mainLoop()

    window.CloseNonBlocking()

def CustomMeter():
    # layout the form
    layout = [[sg.Text('Loading AIGCC...')],
              [sg.ProgressBar(100, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Launch Status').Layout(layout)
    progress_bar = window['progress']
    # loop that would normally do something useful
    for i in range(100):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0, timeout_key='timeout')
        if event == 'Cancel' or event is None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+20)
    # done with loop... need to destroy the window as it's still open
    window.CloseNonBlocking()

#if __name__ == '__main__':
#    CustomMeter()
#    CommandChoiceMenu()


def CommandProcWindow():
    layout = [[sg.Text('Command Accepted, Executing...')],
              [sg.ProgressBar(2000, orientation='h', size=(20,20), key='progress1')],
              [sg.Cancel()]]

    window = sg.Window('Command Status').Layout(layout)
    progress_bar = window['progress1']
    for i in range(var.commandvals.rvalue):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0, timeout_key='timeout')
        if event == 'Cancel' or event is None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+20)
    # done with loop... need to destroy the window as it's still open
    window.Close()
