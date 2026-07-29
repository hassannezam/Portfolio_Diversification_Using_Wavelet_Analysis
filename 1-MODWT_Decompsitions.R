# Load required libraries for wavelet analysis
library(waveslim)
library(ggplot2)
library(quantmod)
library(wavemulcor)

# Read input data
input_path <- "Your_InPut_Path/Returns.csv"
df.name <- read.csv(input_path, header=TRUE, as.is=TRUE, strip.white=FALSE)

# Extract specific column (Company's returns)
df.name = df.name$Return_Ghadir_Mav_Interpolation

# Convert to time series object
returns <- data.frame(df.name, stringsAsFactors=default.stringsAsFactors())
returns <- as.ts(returns)

# Perform MODWT decomposition to 6 levels using LA8 wavelet filter
# boundary = "reflection" prevents edge effects
MRA <- mra(returns, "la8", method = 'modwt', 6, boundary = "reflection")

# Extract detail coefficients at each scale
D1 <- MRA[["D1"]]
D2 <- MRA[["D2"]]
D3 <- MRA[["D3"]]
D4 <- MRA[["D4"]]
D5 <- MRA[["D5"]]
D6 <- MRA[["D6"]]

# Extract smooth coefficients at scale 6
S6 <- MRA[["S6"]]

# Convert all components to data frames
D1 <- data.frame(D1)
D2 <- data.frame(D2)
D3 <- data.frame(D3)
D4 <- data.frame(D4)
D5 <- data.frame(D5)
D6 <- data.frame(D6)
S6 <- data.frame(S6)

# Combine all components into final data frame
dffinal <- data.frame(D1,D2,D3,D4,D5,D6,S6)

# Save results to CSV
output_path <- Your_OutPut_Path File.csv"
write.csv(dffinal, file = output_path)