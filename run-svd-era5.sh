#!/bin/bash

#SBATCH --account vjgo8416-climate
#SBATCH --qos turing
#SBATCH --time 2:0:0
#SBATCH --mem 128G
#SBATCH --ntasks 18
#SBATCH --nodes 1-1

module purge
module load baskerville
source load_modules.sh

source .venv/bin/activate

mpiexec -n 10 python Examples/run_on_era5.py