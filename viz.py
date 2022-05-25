import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np

def plot_time_series(y, x=None, sp=1.0, unit="s", title=None, ylabel=None, ax=None):
    if ax is None:
        _, ax = plt.subplots()
    if x is None:
        ax.plot(
                np.arange(y.shape[0]) * sp,
                y,
        )
    else:
        ax.plot(
                x,
                y,
        )


    ax.set_xlabel(f"time [{unit}]")
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_title(title)

    return ax

def plot_fcd(FCD, window_step, unit="s", title=None, ax=None, labels=None, colorbar=True):
    """
    FCD:            square FCD matrix
    window_step:    sliding window increment 
    unit:           time unit of the increment
    """

    t = FCD.shape[0] * window_step 
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = plt.gcf()

    im = ax.matshow(FCD, extent=[0,t,t,0])

    divider = make_axes_locatable(ax)


    if labels is not None:
        lax = divider.append_axes('right', size='8%', pad=0.05)
        lax.pcolormesh(labels[:,np.newaxis], cmap="tab20")
        lax.invert_yaxis()
        lax.set_title("state")
        lax.tick_params(
            axis='both',
            which='both',
            bottom=False,
            labelbottom=False,
            left=False,
            labelleft=False,
        )
        lax.set_title=("cluster")
    if colorbar:
        cax = divider.append_axes('right', size='5%', pad=0.05)
        cbar = fig.colorbar(im, cax=cax)
        cbar.set_label('$CC[FC(t_1), FC(t_2)]$')

    if title is not None:
        ax.set_title(title)
    ax.set_xlabel("time [%s]" % unit)
    ax.set_ylabel("time [%s]" % unit)

def plot_connectivity(connectivity, title=None, figsize=(6,4)):
    fig, (ax_w, ax_trl) = plt.subplots(nrows=1,ncols=2, figsize=figsize)

    im = ax_w.imshow(connectivity.weights)
    cbar = fig.colorbar(im, ax=ax_w, fraction=0.046, pad=0.04)
    ax_w.set_title('weights')

    im = ax_trl.imshow(connectivity.tract_lengths)
    cbar = fig.colorbar(im, ax=ax_trl, fraction=0.046, pad=0.04)
    ax_trl.set_title('tract lengths')

    if title is not None:
        fig.suptitle(title)

    fig.tight_layout()
