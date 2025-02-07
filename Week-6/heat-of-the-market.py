import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Given
N = 50  
T = 75 
alpha = 0.2  # diffusion coeff (spread rate)
beta = 0.05  # dev factor (growth)
baseline_growth = 500  # small constant increase in all prices per year

# central high-price district
P0 = np.zeros((N, N))
P0[20:30, 20:30] = 1_000_000  # Million-dollar properties in center
P0[0:10, 0:10] = 500_000      # Another wealthy area

P = P0.copy()

# compute thee laplacian (neighbour influence)
def laplacian(P):
    lap = np.zeros_like(P)
    lap[1:-1, 1:-1] = (
        0.25 * (P[:-2, 1:-1] + P[2:, 1:-1] + P[1:-1, :-2] + P[1:-1, 2:]) - P[1:-1, 1:-1]
    )
    return lap

def update_prices(P, alpha, beta, baseline_growth):
    return P + alpha * laplacian(P) + beta * P + baseline_growth

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(P, cmap="coolwarm", interpolation="nearest", vmin=0, vmax=np.max(P0))
plt.colorbar(im, label="Price ($)")

year_text = ax.text(2, 48, "Year 0", fontsize=12, color="white", bbox=dict(facecolor="black", alpha=0.6))

def animate(t):
    global P
    P = update_prices(P, alpha, beta, baseline_growth)
    
    avg_price = np.mean(P)
    max_price = np.max(P)
    min_price = np.min(P)
    
    im.set_array(P)
    year_text.set_text(f"Year {t+1}")
    ax.set_title(f"Avg: ${avg_price:,.0f} | Max: ${max_price:,.0f} | Min: ${min_price:,.0f}")

    if t + 1 == T:
        ani.event_source.stop()

    return im, year_text

ani = FuncAnimation(fig, animate, frames=T, interval=200, blit=True)
plt.show()
