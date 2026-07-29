The codes in this repository are based on the Fernández (2012) wavelet approach and were originally developed in 2020, but uploaded to GitHub at a later date. The wavelet decomposition script uses MODWT with the LA8 filter. This project has been forked from the MODWT-MARS repository by 0zean and extended to include multiple wavelet correlation (MWC) analysis for 11 companies listed on the Tehran Stock Exchange.

📁 Portfolio_Diversification_Using_Wavelet_Analysis/

    📁 scripts/
        📁 R/
            📄 01_MODWT_Decompositions.R
        📁 Python/
            📄 02_correlation_Pairs_Modwt_WithOutPut.py
            📄 03_Max_diagonal_InversMatrix.py
            📄 04_Matrix.Multiple.Correlation.py
            📄 05_Plot_MWC_Up&Lower_Bound.py

    📁 data/
        📁 raw/
            📄 Returns.csv
        📁 processed/
            📄 Modwt_Companies.csv

    📁 results/
        📁 correlation/
            📄 Pair_One_Company_With_Other_Companies.csv
        📁 matrices/
            📄 corr_22x22.csv
            📄 corr_d6_d6.csv
            📄 corr_d6_returns.csv
            📄 inverse_corr.csv
            📄 diag_inverse.csv
        📁 max_diag/
            📄 max_diag.csv
            📄 max_level.csv
        📁 mwc/
            📄 MWC.csv
        📁 figures/
            📄 correlation_heatmap_D4.png
            📄 correlation_heatmap_22x22.png
            📄 MWC_plot.png

    📄 README.md
    📄 requirements.txt
