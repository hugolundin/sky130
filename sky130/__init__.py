import logging

import skidl
from skidl.pyspice import *
from skidl.tools.spice import *

SKY130_SPICE_LIB = '/opt/pdk/skywater-pdk/libraries/sky130_fd_pr/latest/models/sky130.lib.spice'
SKY130_SPICE_CORNER = 'tt'

logging.disable()
sky130 = SchLib(
    SKY130_SPICE_LIB,
    lib_section=SKY130_SPICE_CORNER,
    recurse=True)

logging.disable(logging.NOTSET)
