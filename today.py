import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a random seed for reproducibility
np.random.seed(0)

# Generate random data
data = np.random.randn(100, 2)

# Creating subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Data for the plots
variable1 = data[:, 0]
variable2 = data[:, 1]

# Bar plot for descriptive statistics
axes[0, 0].bar(['Mean', 'Median'], [np.mean(variable1), np.median(variable1)], color='blue', alpha=0.7)
axes[0, 0].bar(['Mean', 'Median'], [np.mean(variable2), np.median(variable2)], color='green', alpha=0.7)
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Heatmap for correlation analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Histogram of the variables
axes[1, 0].hist(variable1, bins=15, color='blue', alpha=0.7, label='Variable 1')
axes[1, 0].hist(variable2, bins=15, color='green', alpha=0.7, label='Variable 2')
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# Scatter plot of the variables
axes[1, 1].scatter(variable1, variable2, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
