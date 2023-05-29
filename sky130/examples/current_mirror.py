
from skidl.pyspice import * 
from skidl.tools.spice import *
from sky130.devices import nmos, pmos


m1 = nmos(1)
m2 = nmos(1)

m1.g & m2.g

generate_netlist()
