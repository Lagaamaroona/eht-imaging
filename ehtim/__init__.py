"""
.. module:: ehtim
    :platform: Unix
    :synopsis: EHT Imaging Utilities

.. moduleauthor:: Andrew Chael (achael@cfa.harvard.edu)

"""
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed, may indicate binary incompatibility.")

import ehtim.obsdata
import ehtim.imager

import ehtim.array
import ehtim.movie
import ehtim.image
import ehtim.vex
import ehtim.closure
import ehtim.caltable

from ehtim.imaging.imager_utils import imager_func
from ehtim.calibrating import self_cal
from ehtim.calibrating import network_cal
from ehtim.plotting    import comp_plots
from ehtim.plotting    import comparisons

from ehtim.calibrating.network_cal import *
from ehtim.plotting.comp_plots import *
from ehtim.plotting.comparisons import *

from ehtim.calibrating.self_cal import self_cal as selfcal
from ehtim.calibrating.self_cal import self_cal as netcal

from ehtim.const_def import *

print("Welcome to eht-imaging v 1.0.0")

def logo():
    for line in BHIMAGE:    
        print(line)
