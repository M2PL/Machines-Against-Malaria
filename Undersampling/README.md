Folder contains code used for cluster-based undersampling of inactive compounds from chemical libraries screened against the asexual blood stages
(ABS) and/or gametocyte stages (dual-active). Clustering was performed on RDKit molecular fingerprints of compounds using Tanimoto dissimilarity
with a distance threshold of 0.4 set to define different clusters. Datasets were divided into multiple sets to allow parallel clustering and avoid
crashing. Undersampling consisted of selecting representatives of each cluster within each set and merging them together. 

If the number of inactive compounds still exceeded that of active compounds another round of clustering and undersampling was performed as above,
however, for the inactive compounds against gametocyte stages complete clustering of the dataset did not balance the dataset between active and
inactive compounds, hence clustering was halted before reaching complete clustering to prevent severly limiting the chemical space.
