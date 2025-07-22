from typing import TYPE_CHECKING, Callable, NamedTuple
import torch
from functools import partial
import collections
import math
import logging
import numpy

def smooth_scheduler(model_sampling, steps, power=1.5, sgm_compatible=False):
    s = model_sampling
    sigma_max = float(s.sigma_max)
    sigma_min = float(s.sigma_min)
    if sigma_min < 1e-6:
        sigma_min = 1e-6
    t = torch.linspace(0, 1, steps)

    if sgm_compatible:
        sigmas = sigma_max * (sigma_min / sigma_max) ** (t ** power)
    else:
        sigmas = sigma_min + (sigma_max - sigma_min) * (1 - t **power)
    
    if math.isclose(sigma_min, 0, abs_tol=1e-5) and not sgm_compatible:
        sigmas = torch.cat([sigmas, torch.tensor([0.0])])
    
    return sigmas
#############################################
from comfy.samplers import SCHEDULER_HANDLERS, SchedulerHandler

SCHEDULER_HANDLERS["smooth"] = SchedulerHandler(smooth_scheduler, use_ms=False)
