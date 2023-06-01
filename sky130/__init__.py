import logging, os

import skidl
from skidl.pyspice import *
from skidl.tools.spice import *

SKY130_SPICE_LIB = '/opt/pdk/skywater-pdk/libraries/sky130_fd_pr/latest/models/sky130.lib.spice'
SKY130_SPICE_CORNER = 'tt'

# Prevent skidl from generating files when run. 
skidl.no_files()

# Ngspice looks for spinit here.
os.environ["SPICE_SCRIPTS"] = os.path.dirname(os.path.abspath(__file__))

# Disable warning about footprints not being found.
skidl.empty_footprint_handler = lambda _: _

logging.disable()
sky130 = SchLib(
    SKY130_SPICE_LIB,
    lib_section=SKY130_SPICE_CORNER,
    recurse=True)
logging.disable(logging.NOTSET)
