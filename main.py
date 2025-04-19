import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for plt and sns
try:
    plt.style.use("Solarize_Light2")
    sns.set_style("darkgrid")
except Exception as e:
    print(f"Error setting style: {e}")

# Load the dataset
penguin_data = pd.read_csv("/Users/frankie/Projects/Python/Penguin Analysis/ExaGEO exercise - penguin dataset.csv")
"""
Example of the dataset:
"rowid","species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex","year"
"1","Adelie","Torgersen",39.1,18.7,181,3750,"male",2007
"2","Adelie","Torgersen",39.5,17.4,186,3800,"female",2007
"3","Adelie","Torgersen",40.3,18,195,3250,"female",2007
"4","Adelie","Torgersen",NA,NA,NA,NA,NA,2007
"5","Adelie","Torgersen",36.7,19.3,193,3450,"female",2007
"6","Adelie","Torgersen",39.3,20.6,190,3650,"male",2007
...
"""

# Get the directory of the current Python script
script_directory = os.path.dirname(os.path.realpath(__file__))

# 1. Visualising Culmen Length Across Species

mean_culmen_length = penguin_data.groupby("species")["bill_length_mm"].mean()
var_culmen_length = penguin_data.groupby("species")["bill_length_mm"].var()
species = mean_culmen_length.index

# Create figure using matplotlib
plt.figure(figsize=(8, 6))
# Set yerr to square root of variance for error bars
plt.bar(species, mean_culmen_length, yerr=np.sqrt(var_culmen_length), capsize=5)
plt.xlabel("Species", fontsize=16)
plt.ylabel("Culmen Length (mm)", fontsize=16)
plt.title("Mean and Variance of Culmen Length Across Species", fontsize=20)
# Save plot in the same directory as the Python script
plot_path = os.path.join(script_directory, "Culmen length across species.png")
plt.savefig(os.path.join(script_directory, "Culmen length across species.png"))


# 2. Correlation Analysis

species_groups = penguin_data.groupby("species")
num_species = len(species)

# Create figure using matplotlib so we can display multiple correlation matrices
fig, axes = plt.subplots(nrows=num_species, figsize=(8, 6 * num_species))

# Plot correlation matrices for each species using seaborn heatmap
for ax, (species, group) in zip(axes, species_groups):
    correlation_matrix = group[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].corr()
    
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax, annot_kws={"fontsize": 16})
    ax.set_title(f"Correlation Matrix for {species}", fontsize=20)

    x_labels = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (mm)"]
    y_labels = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (mm)"]
    ax.set_xticklabels(x_labels, rotation=30, horizontalalignment='right', fontsize=16)
    ax.set_yticklabels(y_labels, rotation=0, horizontalalignment='right', fontsize=16)

plt.tight_layout()
plt.subplots_adjust(hspace=0.5)  # Adjust spacing between subplots
plt.savefig(os.path.join(script_directory, "Correlation matrices of all species.png"))