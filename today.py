import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_data():
    """Generate random data for plotting."""
    np.random.seed(0)
    return np.random.randn(100, 2)

def plot_descriptive_statistics(axes, data):
    """Plot descriptive statistics as bar plot."""
    axes.bar(['Mean', 'Median'], [np.mean(data), np.median(data)], alpha=0.7)
    axes.set_title('Descriptive Statistics: Mean and Median')

def plot_correlation_analysis(axes, data):
    """Plot correlation analysis as heatmap."""
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes)
    axes.set_title('Correlation Analysis')

def plot_histogram(axes, data, color, label):
    """Plot histogram of the variables."""
    axes.hist(data, bins=15, color=color, alpha=0.7, label=label)
    axes.legend()
    axes.set_title('Histogram of Variables')

def plot_scatter(axes, data1, data2):
    """Plot scatter of the variables."""
    axes.scatter(data1, data2, alpha=0.7)
    axes.set_xlabel('Variable 1')
    axes.set_ylabel('Variable 2')
    axes.set_title('Scatter Plot of Variable 1 vs Variable 2')

# Main script
data = generate_random_data()
variable1, variable2 = data[:, 0], data[:, 1]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Descriptive Statistics
plot_descriptive_statistics(axes[0, 0], variable1)
plot_descriptive_statistics(axes[0, 0], variable2)

# Correlation Analysis
plot_correlation_analysis(axes[0, 1], data)

# Histograms
plot_histogram(axes[1, 0], variable1, 'blue', 'Variable 1')
plot_histogram(axes[1, 0], variable2, 'green', 'Variable 2')

# Scatter Plot
plot_scatter(axes[1, 1], variable1, variable2)

plt.tight_layout()
plt.show()
