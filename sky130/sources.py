import skidl.pyspice
from skidl.tools.spice import *

def GND():
    return skidl.pyspice.gnd

def VDC(name, voltage):
    return skidl.pyspice.V(ref=name, dc_value=voltage)

def VDD(voltage):
    return VDC("vdd", voltage)

def IDC(name, current):
    return skidl.pyspice.I(ref=name, dc_value=current)

def IDD(current):
    return IDC("idd", current)

if __name__ == "__main__":
    idd = IDC("idd", 5)
    

