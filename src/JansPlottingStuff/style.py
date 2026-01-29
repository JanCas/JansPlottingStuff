from __future__ import annotations

from importlib.resources import files
import matplotlib.pyplot as plt
from matplotlib import colormaps

def apply(style_filename: str = "natcomm_paper.mplstyle",
          register_batlow: bool = True) -> None:

    if register_batlow and "batlow" not in colormaps:
        import cmcrameri.cm as cm
        colormaps.register(cm.batlow, name="batlow")

    style_path = files("JansPlottingStuff") / style_filename
    plt.style.use(str(style_path))
