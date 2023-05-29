
from skidl.pyspice import * 
from skidl.tools.spice import *

from sky130.devices import nmos
from sky130.sources import VDD, GND

@subcircuit
def current_mirror():
    m1 = nmos(1)


if __name__ == "__main__":
    cm = current_mirror()


    #gnd = GND()
    #vdd = VDD(5)

    circuit = generate_netlist()
    simulator = circuit.simulator()
    
