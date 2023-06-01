
import skidl.pyspice
import skidl.tools.spice

from sky130.units import volt, mA
from sky130.devices import nmos
from sky130.sources import GND, IDD

@skidl.pyspice.package
def current_mirror(i_ref, i_mirror):
    m_ref = nmos(1)
    m_mirror = nmos(1)

if __name__ == "__main__":
    gnd = GND()
    idd = IDD(100@mA)

    cm = current_mirror()
    cm.i_ref.n & idd.p
    

    circuit = skidl.pyspice.generate_netlist()
    print(circuit)
