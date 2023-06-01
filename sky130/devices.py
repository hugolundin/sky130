from skidl.pyspice import *
from skidl.tools.spice import *

from . import sky130

def nmos(W, L=0.15) -> Part:
    return Part(sky130, "sky130_fd_pr__nfet_01v8", params=Parameters(W=W, L=L))

def pmos(W, L=0.15) -> Part:
    return Part(sky130, "sky130_fd_pr__pfet_01v8", params=Parameters(W=W, L=L))

def mosfet_set_width(t, W):
    t.params["w"] = W
