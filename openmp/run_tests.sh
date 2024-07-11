#!/bin/bash

# Verificação e limpeza de arquivos anteriores
rm -f strong_scaling.txt weak_scaling.txt

# Strong scaling
echo "Strong Scaling" > strong_scaling.txt
for threads in 1 2 4 6 8 10 12; do
  export OMP_NUM_THREADS=$threads
  echo "Running with $threads threads" >> strong_scaling.txt
  ./jacobi -n 3000 | tee -a strong_scaling.txt
  if [ $? -ne 0 ]; then
    echo "Error running jacobi with $threads threads" >> strong_scaling.txt
  fi
done

# Weak scaling
echo "Weak Scaling" > weak_scaling.txt
for scale in 1 2 4 6 8 10 12; do
  export OMP_NUM_THREADS=$scale
  N=$(($scale * 250))
  echo "Running with $scale threads and N=$N" >> weak_scaling.txt
  ./jacobi -n $N| tee -a weak_scaling.txt
  if [ $? -ne 0 ]; then
    echo "Error running jacobi with $scale threads and N=$N" >> weak_scaling.txt
  fi
done