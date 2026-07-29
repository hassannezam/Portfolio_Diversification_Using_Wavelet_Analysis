import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats
sheet_path1 ='Your_InPut_Path/Modwt_Companies.csv'
dataframe1= pd.read_csv(sheet_path1)


# Display first 10 rows to verify data
print(dataframe1.head(10))

# Extract D4 wavelet coefficients for all 11 companies
# Each variable represents one company's D4 coefficients
a = dataframe1.DO4  # Behran Oil
b = dataframe1.DI4  # Informatic Iran
c = dataframe1.DP4  # BParsian
d = dataframe1.DG4  # Ghadir Investment
e = dataframe1.DF4  # Folad Mobarkeh
f = dataframe1.DC4  # Chadormalu
g = dataframe1.DD4  # Daro Jaber
h = dataframe1.DK4  # FK Cement
i = dataframe1.DM4  # Mapna
j = dataframe1.DS4  # Sanat & Madan
k = dataframe1.DH4  # ParsKhodro

# Create array of all D4 coefficients
abcdefghijk = np.array([a,b,c,d,e,f,g,h,i,j,k])

# Calculate correlation matrix (11x11) and round to 2 decimals
corr_matrix = np.corrcoef(abcdefghijk).round(decimals=2)
print(corr_matrix)

# Create figure for correlation matrix visualization
fig, ax = plt.subplots(figsize=(10,8))

# Display correlation matrix as heatmap
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)  # Set color scale limits
ax.grid(False)

# Set x-axis labels (company codes)
ax.xaxis.set(ticks=(0, 1, 2,3,4,5,6,7,8,9,10), 
             ticklabels=('D4O','D4I','D4BP','D4G','D4F','D4Ch','D4D','D4FKC','D4M','D4S','D4PKh'))

# Set y-axis labels (full company names)
ax.yaxis.set(ticks=(0, 1, 2,3,4,5,6,7,8,9,10), 
             ticklabels=('D4Oil','D4Infor','D4BPars','D4Ghadir','D4Fold','D4Chador','D4Daro','D4FKCement','D4Mapna','D4Sant','D4PKhodr'))

# Extract Ghadir's correlations with all other companies (row 3)
selectionCorr = (corr_matrix[3:4, 0:11])
df = pd.DataFrame(selectionCorr)
df.to_csv('Your_OutPut_Path/Pair_One Company with Other Companies.csv', index=False)
# Add correlation values as text on the heatmap
for i in range(11):
    for j in range(11):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center',
                color='r', fontsize=10)

# Add colorbar with label
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f', label='Correlation Whole D4')

# Display the plot
plt.show()





