import matplotlib.pyplot as plt
import numpy as np

# k values
k = np.array([1, 5, 10, 15, 20, 30, 40, 50])


gpt52 = np.array([0.2501166667, 0.398375, 0.442625, 0.4644333333, 0.478025, 0.4946583333, 0.5047166667, 0.5113166667])
gemini3pro = np.array([0.3657583333, 0.5306, 0.5850166667, 0.613775, 0.63345, 0.660675, 0.6794833333, 0.6928666667])
gemini25flash = np.array([0.08745833333, 0.1751333333, 0.234675, 0.2758666667, 0.3069833333, 0.351325, 0.3806916667, 0.39995])
gpt5mini = np.array([0.2894, 0.4512833333, 0.508125, 0.5380333333, 0.555575, 0.5739583333, 0.5827416667, 0.5867916667])
kimi_k2 = np.array([0.23205, 0.4296666667, 0.4845833333, 0.50725, 0.520775, 0.5386083333, 0.55245, 0.5648916667])

fig_scale=0.57
plt.figure(figsize=(9 * fig_scale, 4.5 * fig_scale))
ax = plt.gca()

# Background style similar to provided figure
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)

# Plot lines with highlighted dots
plt.plot(k, gpt52, marker='o', markersize=7, linewidth=1.5, label="GPT-5.2", alpha=0.8)
plt.plot(k, gpt5mini, marker='s', markersize=7, linewidth=1.5, label="GPT-5-mini", alpha=0.8)
plt.plot(k, gemini3pro, marker='^', markersize=7, linewidth=1.5, label="Gemini-3-Pro", alpha=0.8)
plt.plot(k, gemini25flash, marker='D', markersize=7, linewidth=1.5, label="Gemini-2.5-Flash", alpha=0.8)
plt.plot(k, kimi_k2, marker='P', markersize=7, linewidth=1.5, label="Kimi-K2", alpha=0.8)

# Labels
plt.xlabel("k", fontsize=12)
plt.ylabel("Pass@k", fontsize=12)

# Ticks
plt.xticks(k, fontsize=11)
plt.xlim(-1, 52)
plt.ylim(0, 0.75)
plt.yticks(np.arange(0, 0.8, 0.1), fontsize=11)

# Legend
plt.legend(frameon=True, fontsize=8)

# Tight layout for minimal margins
plt.margins(0.1)
plt.tight_layout(pad=0.1)

plt.savefig(f"figures/passk.pdf")
