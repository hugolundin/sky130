
from skidl.pyspice import * 
from skidl.tools.spice import *

from sky130.devices import nmos
from sky130.sources import VDD, GND

@subcircuit
def current_mirror(vdd, gnd):
    m1 = nmos(1)

    gnd & m1.g
    vdd & m1.d
    gnd & m1.s

if __name__ == "__main__":
    vdd = VDD(5)
    gnd = GND()
    cm = current_mirror(vdd, gnd)

    circuit = generate_netlist()
    