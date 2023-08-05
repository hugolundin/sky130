import skidl
import skidl.pyspice
import skidl.tools.spice

from sky130.units import volt, kHz
from sky130.devices import nmos
from sky130.sources import GND, VDD

from sky130 import sky130

@skidl.pyspice.subcircuit
def testbench():
    # gnd = GND()
    # vgs = VDD(1@volt)
    # vds = VDD(1@volt)

    # m = nmos(1)
    # m.g & vgs.p
    # m.s & vgs.n & vds.n & gnd
    # m.d & vds.p

    nfet_wl = skidl.pyspice.Parameters(W=0.42, L=0.15)
    nfet = skidl.Part(sky130, "sky130_fd_pr__nfet_01v8", params=nfet_wl)

    return skidl.Interface()

if __name__ == "__main__":
    testbench()
    circuit = skidl.pyspice.generate_netlist()
    print(circuit)
    
    simulator = circuit.simulator()
    simulator.ac(start_frequency=10@kHz, stop_frequency=100@kHz, number_of_points=10, variation='dec')
