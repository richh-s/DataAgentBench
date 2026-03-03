import matplotlib.pyplot as plt

models = [
    "GPT-5.2",
    "GPT-5-mini",
    "Gemini-3-Pro",
    "Gemini-2.5-Flash",
    "Kimi-K2"
]

cost = [282.0879, 67.294, 1357.8962, 137.4397, 1303.6072]      # USD
accuracy = [0.2501166667, 0.2894, 0.3657583333, 0.08745833333, 0.23205] # 0~1


markers = ['o', 's', '^', 'D', 'P']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig_scale = 0.56
fig, ax = plt.subplots(figsize=(6 * fig_scale, 4 * fig_scale))

# Scatter
for i in range(len(models)):
    ax.scatter(
        cost[i],
        accuracy[i],
        s=100,
        alpha=0.85,
        marker=markers[i],
        color=colors[i],
        edgecolor='black',      # black edge is clearer on log plots
        linewidth=0.8,
        label=models[i],
        zorder=3
    )
    if models[i] not in ["Gemini-3-Pro", "Kimi-K2"]:
        # Special case: place label to the right for better visibility
        y_off = 0.025 if models[i] == "Gemini-2.5-Flash" else 0.02
        ax.text( 
            cost[i] * 0.95, # small x offset to the left
            accuracy[i] + y_off, # small y offset 
            models[i], 
            fontsize=9, 
            ha='left',           # left-align text to anchor at right of marker
            va='bottom',
            clip_on=False
        )
    else:
        y_off = 0.015 if models[i] == "Gemini-3-Pro" else 0.02
        ax.text( 
            cost[i]* 1.18, # small x offset 
            accuracy[i] + y_off, # small y offset 
            models[i], 
            fontsize=9, 
            # verticalalignment='left' 
            ha='right',            # right-align text to anchor at left of marker
            va='bottom',
            clip_on=False
        )

# ---- Log scale ----
ax.set_xscale("log")

# Clean log limits
ax.set_xlim(50, 2000)
ax.set_ylim(0, 0.42)

# Optional: cleaner log ticks
ax.set_xticks([50, 100, 200, 500, 1000, 2000])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
ax.ticklabel_format(style='plain', axis='x')
# set tick fontsize of x and y
ax.tick_params(axis='x', labelsize=9)
ax.tick_params(axis='y', labelsize=10)


# Labels
ax.set_xlabel("Cost (USD, log scale)", fontsize=11)
ax.set_ylabel("Pass@1", fontsize=11)

# Grid (log-friendly)
ax.grid(True, which="both", linestyle='--', linewidth=0.7, alpha=0.6)


plt.margins(0.1)
plt.tight_layout(pad=0.1)

plt.savefig(f"figures/cost_acc.pdf")