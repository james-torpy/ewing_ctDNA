
#!/bin/bash

home_dir="/share/ScratchGeneral/jamtor"
project_dir="$home_dir/projects/ewing_ctDNA"
script_dir="$project_dir/scripts"
in_path="$project_dir/raw_files"

sample_names=( "409_016_DBV4V_TAGGCATG-CTCTCTAT_L001" "409_018_DBV4V_AAGAGGCA-CTCTCTAT_L001" \
  "409_031_DCB8V_GTAGAGGA-CTCTCTAT_L001" "409_014_DBV4V_TCCTGAGC-CTCTCTAT_L001" \
  "409_021_DBV4V_CTCTCTAC-CTCTCTAT_L001" "409_005_D9YWF_ATCTCAGG-CTCTCTAT_L001" \
  "409_019_DBV4V_GCTCATGA-CTCTCTAT_L001" "409_025_DCB8V_TCCTGAGC-CTCTCTAT_L001" \
  "409_007_DB62M_TAGGCATG-CTCTCTAT_L001" "409_006_DB62M_GGACTCCT-CTCTCTAT_L001" \
  "409_012_DBV4V_CGTACTAG-CTCTCTAT_L001" "409_013_DBV4V_AGGCAGAA-CTCTCTAT_L001" \
  "409_008_DB62M_GTAGAGGA-CTCTCTAT_L001" "409_063_DCCT9_TCCTGAGC-CTCTCTAT_L001" \
  "409_061_DCCT9_AGGCAGAA-CTCTCTAT_L001" "409_020_DBV4V_GTAGAGGA-CTCTCTAT_L001" \
  "409_015_DBV4V_GGACTCCT-CTCTCTAT_L001" )

for s in ${sample_names[@]}; do


  cmd="$script_dir/qiagen_dna_pipeline.sh $s"

  qsub -pe smp 7 -N ewfus.smk -wd \
    $in_path/$s \
    -b y -j y -V -P DSGClinicalGenomics $cmd

done