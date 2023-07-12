# Database explaination:

## Asexual datasets 
* Asexual_libraries_hits and nonhitsFinal.csv :Contains asexual dataset before cluster-based undersampling with additional details of 
  compounds such as the compound key, CHEMBL ID, SMILES, activity against ABS and from which chemical library the compound was obtained from.
* Merged_asexual_libraries_hits and nonhits_nd.csv :Contains asexual dataset before cluster-based undersampling with minimal details of 
  compounds such as the compound key, SMILES and activity against ABS to allow cluster-based undersampling. This asexual dataset is the 
  merging of multiple chemical libraries screened against ABS. See Asexual_libraries_hits and nonhitsFinal.csv

## Sexual datasets 
* Merged_sexual_libraries_hits and nonhits_nd.csv :Contains sexual dataset before cluster-based undersampling with minimal details of 
  compounds to allow cluster-based undersampling. Details such as the compound key, SMILES and activity against sexual gaemtocyte stages. 
  This sexual dataset is the merging of multiple chemical libraries screened against sexual gaemtocyte stages.
  See Sexual_libraries_hits and nonhitsFinal.csv
* Sexual_libraries_hits and nonhitsFinal.csv :Contains ssexual dataset before cluster-based undersampling with additional details of 
  compounds  such as the compound key, CHEMBL ID, SMILES, activity against sexual gaemtocyte stages and from which chemical library the 
  compound  was obtained from.
