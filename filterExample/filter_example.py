"""
Exponential Low-Pass Filter (a.k.a. Exponential Moving Average) Demo
---------------------------------------------------------------------

Update rule:
    s = x * r + s * (1 - r)

where:
    x = raw (noisy) signal sample just observed
    s = smoothed output (state carried between samples)
    r = "gain" / weighting for the new sample, e.g. r = 0.05 means each
        update blends in 5% of the new reading and keeps 95% of the
        previous smoothed value.

This is the discrete-time equivalent of an analog RC low-pass filter,
and is extremely cheap to compute (one multiply-add per sample), which
is why it's a favorite in embedded systems, sensor processing, and
real-time dashboards.

The script below:
  1. Generates a synthetic noisy signal (a slowly varying "true" trend
     plus random noise plus a couple of sudden spikes).
  2. Applies the exponential filter for a few different values of r so
     you can see the smoothing/lag trade-off.
  3. Plots raw vs. filtered signals and saves the figure to disk.
  4. Prints the first several iterations step-by-step so you can trace
     the math by hand.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def exponential_low_pass(x_values, r, s0=None):
    """
    Apply an exponential (single-pole IIR) low-pass filter to a sequence.

    Parameters
    ----------
    x_values : sequence of float
        The raw signal samples, in time order.
    r : float
        Smoothing factor in (0, 1]. Larger r -> less smoothing, faster
        response. Smaller r -> more smoothing, slower response (more lag).
    s0 : float, optional
        Initial value for the smoothed state. Defaults to the first raw
        sample (a common convention that avoids start-up transients).

    Returns
    -------
    np.ndarray
        The smoothed signal, same length as x_values.
    """
    x_values = np.asarray(x_values, dtype=float)
    s = x_values[0] if s0 is None else s0

    smoothed = np.empty_like(x_values)
    for i, x in enumerate(x_values):
        s = x * r + s * (1 - r)   # <-- the exponential low-pass update
        smoothed[i] = s

    return smoothed


def build_demo_signal(n_samples=300, seed=42):
    """Create a synthetic noisy signal with a drifting trend and two spikes."""
    rng = np.random.default_rng(seed)
    t = np.arange(n_samples)

    # Slowly varying "true" underlying trend
    true_trend = 10 + 3 * np.sin(t / 40.0) + 0.01 * t

    # Add measurement noise
    noise = rng.normal(loc=0.0, scale=1.2, size=n_samples)

    x = true_trend + noise

    # Inject a couple of sudden spikes/outliers to show filter response
    x[80] += 8
    x[81] += 4
    x[200] -= 7

    return t, x, true_trend


def main():
    t, x, true_trend = build_demo_signal()

    # Try a few different weightings r to show the smoothing/lag trade-off
    r_values = [0.05, 0.15, 0.4]
    filtered = {r: exponential_low_pass(x, r) for r in r_values}

    # --- Step-by-step trace of the first 10 samples for r = 0.05 ---------
    r_demo = 0.05
    print(f"Step-by-step trace of s = x*r + s*(1-r), r = {r_demo}\n")
    print(f"{'i':>3} | {'x (raw)':>10} | {'s (smoothed)':>14}")
    print("-" * 34)
    s = x[0]
    for i in range(10):
        if i == 0:
            print(f"{i:>3} | {x[i]:>10.4f} | {s:>14.4f}  (initial: s0 = x0)")
        else:
            s_prev = s
            s = x[i] * r_demo + s * (1 - r_demo)
            print(
                f"{i:>3} | {x[i]:>10.4f} | {s:>14.4f}  "
                f"(= {x[i]:.3f}*{r_demo} + {s_prev:.3f}*{1 - r_demo})"
            )
    print()

    # --- Plot ------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 6))

    ax.plot(t, x, color="lightgray", linewidth=1.0, label="Raw signal (x)", zorder=1)
    ax.plot(t, true_trend, color="black", linewidth=1.2, linestyle="--",
             label="Underlying true trend", zorder=2)

    colors = {0.05: "#1f77b4", 0.15: "#ff7f0e", 0.4: "#2ca02c"}
    for r in r_values:
        ax.plot(t, filtered[r], color=colors[r], linewidth=2.0,
                 label=f"Filtered, r = {r:.2f}", zorder=3)

    ax.set_title("Exponential Low-Pass Filter Demo\n"
                  "s = x·r + s·(1−r)", fontsize=13)
    ax.set_xlabel("Sample index (time)")
    ax.set_ylabel("Signal value")
    ax.legend(loc="upper left", frameon=True)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    output_path = Path(__file__).resolve().parent / "ema_lowpass_demo.png"
    fig.savefig(output_path, dpi=150)
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    main()