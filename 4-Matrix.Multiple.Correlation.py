import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy import stats

# Read the input data containing max diagonal values for all levels
dataframe = pd.read_csv('sheet_path')
print(dataframe.head(10))

# Extract max diagonal values for each level (D1 to D6)
a = dataframe.MD1
b = dataframe.MD2
c = dataframe.MD3
d = dataframe.MD4
e = dataframe.MD5
f = dataframe.MD6

# Calculate Multiple Wavelet Correlation (MWC) for each scale
# Formula: MWC = sqrt(1 - 1/max_diag)
aa = (1 - (1/a))**.5
bb = (1 - (1/b))**.5
cc = (1 - (1/c))**.5
dd = (1 - (1/d))**.5
ee = (1 - (1/e))**.5
ff = (1 - (1/f))**.5

# Store all MWC values in array
MWC_All_D = np.array([aa, bb, cc, dd, ee, ff])

# Convert to dataframe and transpose
df = pd.DataFrame(MWC_All_D).T
print(MWC_All_D)
# Save MWC values to CSV
df.to_csv('Save/To/Your/Path/MWC.csv', index=False)