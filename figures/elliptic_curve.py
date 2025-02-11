import matplotlib.pyplot as plt

def init_subplot(plt, cx, cy, nccol=1, ncrow=1):
  if nccol*ncrow == 1:
    fig, ax = plt.subplots(nccol, ncrow, figsize=(4,4))
    plt.tick_params(labelsize="large")
    ax.set_xlim(cx); ax.set_ylim(cy)
    ax.set_aspect('equal')
    ax.grid()
  else:
    fig, ax = plt.subplots(nccol, ncrow, figsize=(8,8))
    plt.tick_params(labelsize="small")
    plt.rcParams["font.size"] = 5
    plt.tight_layout()
    for c in range(nccol):
      for r in range(ncrow):
        ax[r,c].set_xlim(cx); ax[r,c].set_ylim(cy)
        ax[r,c].set_aspect('equal')
  return ax

sizex = 30
CX, CY = (-sizex, sizex), (-sizex, sizex)
ax = init_subplot(plt, CX, CY)

x, y = sp.symbols("x y")
ax.fill(*plot_fxy(x**3+17-y**2, CX, CY), facecolor='blue')
QP = [(-2,3),(-1,4),(2,5),(4,9),(8,23)]
for (qx,qy) in QP:
  ax.plot(qx,qy, marker='o', ms="2.0", color='red')
  ax.text(qx+1,qy-1, f"({qx},{qy})")
plt.show

