from collections import namedtuple

import skidl.pyspice
import skidl.tools.spice

Source = namedtuple('Supply', 'source p n')

def GND():
    return skidl.pyspice.gnd

def VDC(name, voltage) -> Source:
    source = skidl.pyspice.V(ref=name, dc_value=voltage)
    return Source(source, source['p'], source['n'])

def VDD(voltage)  -> Source:
    return VDC("vdd", voltage)

def IDC(name, current)  -> Source:
    source = skidl.pyspice.I(ref=name, dc_value=current)
    return Source(source, source['p'], source['n'])

def IDD(current)  -> Source:
    return IDC("idd", current)

if __name__ == "__main__":
    idd = IDC("idd", 5)
    
