from utils import CommandChoiceMenu as ccm
from utils import var
from utils import functions as fnc
#import os
#import anvil.server

#anvil.server.connect("server_EANVEB6VHCPTLTPQBJEI6GUL-4EBEHDOKMF5YJHGV")

#@anvil.server.callable
#def say_hello(name):
#    print(f"Uplink Online, {name}!")

var.opsClock()
ccm.CustomMeter()
fnc.mainLoop()


#anvil.server.wait_forever()

#sg.Popup(var.commandvals.V0, var.var.commandvals.V1, var.var.commandvals.V2, var.var.commandvals.V3, var.var.commandvals.V4, var.var.commandvals.V5, var.var.commandvals.V6, var.var.commandvals.V7)
