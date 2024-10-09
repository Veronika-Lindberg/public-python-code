import matplotlib.pyplot as plt
import numpy as np
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Data
characteristics = [
    'TNM Stage 4B',
    'Sex: Male',
    'TKI-TT',
    'Moxa 1-4 times',
    'Moxa > 4 times'
]
hazard_ratios = [1.43, 1.36, 0.79, 0.72, 0.52]
ci_lower = [1.14, 1.09, 0.63, 0.56, 0.37]
ci_upper = [1.79, 1.70, 0.99, 0.92, 0.73]

# Convert data to numpy arrays for easier manipulation
y_pos = np.arange(len(characteristics))

# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(hazard_ratios, y_pos, xerr=[np.array(hazard_ratios) - np.array(ci_lower), np.array(ci_upper) - np.array(hazard_ratios)], fmt='ko', ecolor='black')
plt.yticks(y_pos, characteristics)
plt.axvline(x=1, color='grey', linestyle='--')

# Expand x-axis limits
plt.xlim(0, 2.5)

# Labels and title
plt.xlabel('Hazard Ratio')
plt.title('Hazard Ratios for Various Characteristics in Stage IV Metastatic NSCLC')

# Add HR and CI annotations
for i in range(len(characteristics)):
    hr_text = f'HR {hazard_ratios[i]:.2f} ({ci_lower[i]:.2f}-{ci_upper[i]:.2f})'
    plt.text(1.9, i, hr_text, verticalalignment='center', fontsize=10)

# Remove y-axis ticks and lines
plt.tick_params(axis='y', which='both', left=False)

# Remove the top line of the graph
plt.gca().spines['top'].set_visible(False)

# Save plot as an image file
plt.savefig('hazard_ratio_plot.png', format='png')

# Show plot
plt.gca().invert_yaxis()  # Invert y-axis to have the first characteristic on top
plt.show()