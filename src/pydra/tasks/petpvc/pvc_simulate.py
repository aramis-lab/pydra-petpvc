"""
PVCSimulate
===========

Examples
--------

>>> task = PVCSimulate(input_image="input.nii", fwhm=(4.0, 4.0, 4.0))
>>> task.cmdline    # doctest: +ELLIPSIS
'pvc_simulate input.nii ...input_pvcsim.nii -x 4.0 -y 4.0 -z 4.0'
"""

__all__ = ["PVCSimulate"]

from os import PathLike
from typing import Tuple

from attrs import define, field
from pydra.engine.specs import ShellSpec, SpecInfo
from pydra.engine.task import ShellCommandTask


@define(kw_only=True)
class PVCSimulateSpec(ShellSpec):
    """Specifications for pvc_simulate."""

    input_image: PathLike = field(metadata={"help_string": "input image", "mandatory": True, "argstr": ""})

    output_image: str = field(
        metadata={"help_string": "output image", "argstr": "", "output_file_template": "{input_image}_pvcsim"}
    )

    fwhm: Tuple[float, float, float] = field(
        metadata={
            "help_string": "FWHM of the PSF along x, y and z",
            "mandatory": True,
            "formatter": lambda fwhm: f"-x {str(fwhm[0])} -y {str(fwhm[1])} -z {str(fwhm[2])}",
        }
    )


class PVCSimulate(ShellCommandTask):
    """Task definition for pvc_simulate."""

    executable = "pvc_simulate"

    input_spec = SpecInfo(name="Inputs", bases=(PVCSimulateSpec,))
