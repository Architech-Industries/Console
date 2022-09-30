#from influxdb import InfluxDBClient
from random import seed
from random import randint
from random import sample
from random import choice
#from random import random
#from datetime import datetime
#import PySimpleGUI as sg
from utils import CommandChoiceMenu as ccm
import time

class commandvals:
    V0 = 0
    V1 = 0
    V2 = 0
    V3 = 0
    V4 = 0
    V5 = 0
    V6 = 0
    V7 = None
    #OPTIONS
    V8 = False
    V9 = False
    V10 = False
    V11 = False
    V12 = False
    V13 = False
    V14 = False
    V15 = False
    V16 = False
    V17 = False
    V18 = False
    #AUGMENTATIONS
    V19 = False
    V20 = False
    V21 = False
    V22 = False
    V23 = False
    V24 = False
    V25 = False
    V26 = False
    V27 = False

    rvalue = 100
    rseed = 0

    order = 0
    category = 0
    edict = 0
    priority = 0
    protocol = 0
    auth = 0
    stage = 0
    alarm = None

    run_time = 0
    start_time = None
    
    OS0 = False
    OS1 = False
    OS2 = False
    OS3 = False
    OS4 = False
    OS5 = False
    OS6 = False
    OS7 = False

    E0 = False
    E1 = False
    E2 = False
    E3 = False
    E4 = False
    E5 = False
    E6 = False
    E7 = False

    

def mainLoop():

    while True:
        running_time = (time.time() - commandvals.start_time)
        commandvals.run_time = running_time
        rngSeed()
        rng()
        ccm.CommandMenu.CCGUI()
        #print('Commands Issued')
        ccm.execstats()
        ccm.CommandProcWindow()

def valueprinter():
    if commandvals.V0 is not None or 0:
      commandvals.order = commandvals.V0
      print('Order: ', commandvals.V0) 
    if commandvals.V1 is not None or 0:
      commandvals.category = commandvals.V1
      print('Category: ', commandvals.V1) 
    if commandvals.V2 > 0:
      commandvals.edict = commandvals.V2
      print('Edict: ', commandvals.V2)
    if commandvals.V3 > 0:
      commandvals.priority = commandvals.V3
      print('Priority: ', commandvals.V3)
    if commandvals.V4 > 0:
      commandvals.protocol = commandvals.V4
      print('Protocol: ', commandvals.V4)
    if commandvals.V5 != 0:
      commandvals.auth = commandvals.V5
      print('Auth: ', commandvals.V5)
    if commandvals.V6 != 0:
      commandvals.stage = commandvals.V6
      print('Stage: ', commandvals.V6)
    if commandvals.V7 is not None:
      commandvals.alarm = commandvals.V7
      print('Alarm Status: ', commandvals.V7)
    #else:
      #print('No Commands Executed')



#def ComExec():
    #ComExecVal = commandvals.V0, commandvals.V1, commandvals.V2, commandvals.V3, commandvals.V4, commandvals.V5, commandvals.V6, commandvals.V7
    #print(ComExecVal) 

def rng():
    seed(commandvals.rseed)
    for _ in range(1):
        rvalue = randint(100, 2000)
        commandvals.rvalue = rvalue
        #print('RValue: ', commandvals.rvalue)

def rngSeed():
    seed()
    sequence = list(range(100000))
    subset = sample(sequence, 100)
    for _ in range(1):
        selection = choice(subset)

    commandvals.rseed = commandvals.rseed + selection
    #print('\nSeed: ', selection)

def opsClock():
    start_time = time.time()
    commandvals.start_time = start_time
    #mainLoop()
    print("--- %s seconds ---" % (time.time() - start_time))
    running_time = (time.time() - start_time)
    time.strftime("%H:%M:%S", time.gmtime(running_time))
    commandvals.run_time = running_time
    print(time.strftime("%H:%M:%S", time.gmtime(running_time)))

def ClockPrint():
    time.strftime("%H:%M:%S", time.gmtime(commandvals.run_time))

def orderselection():
    if commandvals.OS0 is True:
        commandvals.V0 = 0
    if commandvals.OS1 is True:
        commandvals.V0 = 1
    if commandvals.OS2 is True:
        commandvals.V0 = 2
    if commandvals.OS3 is True:
        commandvals.V0 = 3
    if commandvals.OS4 is True:
        commandvals.V0 = 4
    if commandvals.OS5 is True:
        commandvals.V0 = 5
    if commandvals.OS6 is True:
        commandvals.V0 = 6
    if commandvals.OS7 is True:
        commandvals.V0 = 7
    #else:
        #commandvals.V0 = None

def edictselection():
    if commandvals.E0 is True:
        commandvals.V3 = 0
    if commandvals.E1 is True:
        commandvals.V3 = 1
    if commandvals.E2 is True:
        commandvals.V3 = 2
    if commandvals.E3 is True:
        commandvals.V3 = 3
    if commandvals.E4 is True:
        commandvals.V3 = 4
    if commandvals.E5 is True:
        commandvals.V3 = 5
    if commandvals.E6 is True:
        commandvals.V3 = 6
    if commandvals.E7 is True:
        commandvals.V3 = 7

def orderentry():
    ccm.CommandMenu.values['Order#'] = commandvals.V0


class opsMetrics:
    stat = "Online"
    
    opsNum = None
    cmdsq = 0
    cmdValid = False
    OVC = 0
    orders = [1, 46]
    opname = "Unknown"

def opsUpdate():
    opvar = commandvals.V0, commandvals.V1, commandvals.V2, commandvals.V3, commandvals.V4, commandvals.V5, commandvals.V6, commandvals.V7
    opsMetrics.opsNum = opvar
    opsMetrics.cmdsq = opvar
    print('Command Sequence: ', opvar)

    opvarcalc = (commandvals.V0 + commandvals.V1 + commandvals.V2 + commandvals.V3 + commandvals.V4 + commandvals.V5 + commandvals.V6)
    print('cmdcalc:', opvarcalc)
    opsMetrics.OVC = opvarcalc


def cmdRef():
    print('OPSCONFIG: ', opsMetrics.cmdsq)
    
    while True:
        print('\n')
        print('------cmd ref section-------')
        print('CM0:: ', opsMetrics.OVC)
        print('-------------')
        orderSelector()
        if opsMetrics.cmdValid == True:
            print('\n')
            print('-----Executing Order: ', opsMetrics.OVC)
            ordName()
            break
            ##else:
            #print('NOPE')
        else:
            print('Invalid Command')
            break
        #except:
            #print('ERROR')
            #continue

def orderSelector():
    print('\n')
    print('--Order Def Section--')
    print('inital OVC: ', opsMetrics.OVC)
    print('inital cmdvalid: ', opsMetrics.cmdValid)
    for number in opsMetrics.orders:
        if opsMetrics.OVC == number:
            opsMetrics.cmdValid = True
            print('Order Exists: ', number)
            break
        else:
            break


def ordName():
    CM0 = 46



class auth():
    url = ''
    token = ''
    org = ''

#def authtest():