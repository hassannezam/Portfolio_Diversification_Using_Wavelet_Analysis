import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats

# Read the input data
dataframe1 = pd.read_csv( 'Your_InPut_Path/Modwt And Return Companies.csv')

# Display first 10 rows to verify data
print(dataframe1.head(10))

# Extract D6 wavelet coefficients for all 11 companies
a = dataframe1.DO6
b = dataframe1.DI6
c = dataframe1.DP6
d = dataframe1.DG6
e = dataframe1.DF6
f = dataframe1.DC6
g = dataframe1.DD6
h = dataframe1.DK6
i = dataframe1.DM6
j = dataframe1.DS6
k = dataframe1.DH6

# Extract original return series for all 11 companies
m = dataframe1.Return_BehranOil_Mav_Interpolation
n = dataframe1.Return_Infor_service_Mav_Interpolation
p = dataframe1.Return_BPrsian_Mav_Interpolation
q = dataframe1.Return_Ghadir_Mav_Interpolation
r = dataframe1.Return_Folad_Mobarkeh_Mav_Interpolation
s = dataframe1.Return_FK_Cement_Mav_Interpolation
t = dataframe1.Return_Dro_Jaber_Mav_Interpolation
u = dataframe1.Return_ParsKhodro_Mav_Interpolation
x = dataframe1.Return_MAPNA_Mav_Interpolation
y = dataframe1.Return_In_Mine_Mav_Interpolation
z = dataframe1.Return_Chador_Mav_Interpolation

# Create 22x22 array combining D6 coefficients and original returns
abcdefghijkmnpqrstuxyz = np.array([a,b,c,d,e,f,g,h,i,j,k,m,n,p,q,r,s,t,u,x,y,z])

# Calculate 22x22 correlation matrix
corr_matrix = np.corrcoef(abcdefghijkmnpqrstuxyz).round(decimals=2)
print(corr_matrix)

# Create heatmap for 22x22 correlation matrix
fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)

# Set x-axis labels (D6 coefficients + returns)
ax.xaxis.set(ticks=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21), 
             ticklabels=('D6O','D6I','D6P','D6G','D6F','D6C','D6D','D6K','D6M','D6S','D6H','BOil','Inf','BP','Gha','FMo','FKC','Dr','PK','Map','SM','Cha'))

# Set y-axis labels (full names)
ax.yaxis.set(ticks=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21), 
             ticklabels=('D6.Behran.Oil','D6.Informatic.Iran','D6.BParsian','D6.Ghadir.Invesment','D6.Folad.Mobarkeh','D6.FK.Cement','D6.Daro.Jaber','D6.ParsKhodro',
'D6.Mapna','D6.Sanat&Madan','D6.Chadormalu','Behran.Oil','Informatic.Iran','B.Parsian','Ghadir.Invesment','Folad.Mobarkeh','FK.Cement','Daro.Jaber','ParsKhodro','Mapna','Sanat&Madan','Chadormalu'))

# Add correlation values as text on the heatmap
for i in range(22):
    for j in range(22):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center', color='r')

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f', label='Correlation Returns')
plt.show()

# Calculate inverse of the full 22x22 correlation matrix
INV = np.linalg.inv(corr_matrix)
print(INV)

# Extract diagonal elements from the inverse matrix
max = (INV[0,0], INV[1,1], INV[2,2], INV[3,3], INV[4,4], INV[5,5], INV[6,6], INV[7,7], INV[8,8], INV[9,9], INV[10,10], INV[11,11],
INV[12,12], INV[13,13], INV[14,14], INV[15,15], INV[16,16], INV[17,17], INV[18,18], INV[19,19], INV[20,20], INV[21,21])

# Extract submatrix: Returns (rows 11-21) vs D6 coefficients (columns 0-11)
selectionCorrD_R = (corr_matrix[11:22, 0:11])

# Extract submatrix: D6 coefficients vs D6 coefficients
selectionCorrD_D = (corr_matrix[0:11, 0:11])

# Convert submatrices to dataframes
df0 = pd.DataFrame(corr_matrix)          # Full 22x22 correlation matrix
df = pd.DataFrame(selectionCorrD_R)      # 11x11 correlation: Returns vs D6 coefficients
df1 = pd.DataFrame(selectionCorrD_D)     # 11x11 correlation: D6 vs D6 coefficients

# Calculate inverse of the Returns-D6 correlation matrix (11x11)
INV1 = np.linalg.inv(df)

# Extract diagonal elements from the inverse of Returns-D6 matrix
max2 = (INV1[0,0], INV1[1,1], INV1[2,2], INV1[3,3], INV1[4,4], INV1[5,5], INV1[6,6], INV1[7,7], INV1[8,8], INV1[9,9], INV1[10,10])

# Verify: multiply inverse by original matrix (should approximate identity)
A = INV1.dot(selectionCorrD_R)

# Transpose the inverse matrix for proper formatting
dfi = pd.DataFrame(INV1).T              # Transposed inverse of Returns-D6 correlation matrix

# Sort diagonal values
sor = sorted(max2)

# Create dataframe of sorted diagonal values
df2 = pd.DataFrame(sor).T               # Sorted diagonal values from inverse matrix

# Save all results to CSV files
df0.to_csv('corr_22x22_output_path', index=False)          # Full 22x22 correlation matrix
df1.to_csv('corr_d6_d6_output_path', index=False)          # D6 vs D6 correlation (11x11)
df.to_csv('corr_d6_returns_output_path', index=False)      # D6 vs Returns correlation (11x11)
dfi.to_csv('inverse_corr_output_path', index=False)        # Inverse of D6-Returns matrix
df2.to_csv('diag_inverse_output_path', index=False)        # Sorted diagonal values

# Convert diagonal values to array and round to 3 decimals
l = np.array(max2)
k = l.round(3)

# Verify: multiply full inverse by full correlation matrix (should approximate identity)
A = INV.dot(corr_matrix)

# Create dataframe of diagonal values and save
df3 = pd.DataFrame([k], columns=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11'])
df3.to_csv('max_diag_output_path', index=False)            # Diagonal values from inverse matrix for level D6
print(k)

# Find maximum diagonal value from inverse of Returns-D6 matrix
ArrMax_k = np.max(k)
print(ArrMax_k)

# Save the maximum diagonal value for MWC calculation
df4 = pd.DataFrame([ArrMax_k], columns=['Max_ValueDiag'])
df4.to_csv('max_level_output_path', index=False)           # Maximum diagonal value