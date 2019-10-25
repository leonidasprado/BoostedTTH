
#cd configs
cd configs_slimmed_ntuples
for f in *.py; do crab submit $f ; done

