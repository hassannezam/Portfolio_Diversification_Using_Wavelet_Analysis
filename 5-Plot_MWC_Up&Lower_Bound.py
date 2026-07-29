import numpy as np
import math
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath

# Multiple Wavelet Correlation values per scale
df1 = {
    'Name': ['MWD1','MWD2','MWD3','MWD4','MWD5','MWD6'],
    'MWC':  [0.744383151, 0.746234069, 0.815321875, 0.874707849, 0.929365718, 0.95252499]
}
df1 = pd.DataFrame(df1, columns=['Name','MWC'])
print(df1)

# Fisher z-transformation for correlation coefficients
df1['log_value'] = 0.5 * np.log((1 + df1['MWC']) / (1 - df1['MWC']))
log_val = np.array(df1['log_value'])
print(df1)

# Effective sample size for each wavelet scale
df2 = {
    'Name': ['D1','D2','D3','D4','D5','D6'],
    'TJ':   [128, 64, 32, 16, 8, 4]
}
df2 = pd.DataFrame(df2, columns=['Name','TJ'])

# Convert all values to NumPy arrays to avoid indexing errors
MWC = np.array(df1['MWC'])
TJ = np.array(df2['TJ'])

# Calculate 99.7% confidence intervals
# Formula: standard error = 2.98 / sqrt(n), then transform back with tanh
Lower_Band = np.tanh(log_val - (2.98 / np.sqrt(TJ)))
Upper_Band = np.tanh(log_val + (2.98 / np.sqrt(TJ)))

# Main correlation values for plotting
Main_Value_MWC = MWC

# Prepare horizontal axis
x = np.linspace(1, 6, 6)
y = Lower_Band
z = Upper_Band
w = Main_Value_MWC

# Create plot
fig, ax = plt.subplots()

# Lower confidence band
line1, = ax.plot(x, y, label='Lower_Band')
line1.set_dashes([2, 2, 14, 2])

# Upper confidence band
line2, = ax.plot(x, z, label='Upper_Band')
line2.set_dashes([2, 2, 14, 2])

# Multiple Wavelet Correlation line
line3, = ax.plot(x, w, label='Multiple Wavelet Correlation', lw=2, color='green')

ax.legend()
plt.show()