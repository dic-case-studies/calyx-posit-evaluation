# Calyx Posit Evaluation

This repository contains the code for evaluating the Calyx binding of the [Chisel HardPosit](https://github.com/thoughtworks/hardposit-chisel3) units from [Dahlia](https://github.com/cucapra/dahlia).

The following benchmarks from the [Machsuite](https://github.com/breagen/MachSuite) are used

1. FFT Strided
2. SPMV CRS
3. SPMV ELLPACK
4. Viterbi

## Instructions to run the benchmarks

- Install python utilities `cd utilities/python; pip3 install -e .; cd ../..`
- Build cpp utilities `cd utilities/cpp; cmake -B ./build/ -S .; make -C build; cd ../../`
- For running the benchmarks, do `make`

## Acknowledgement

This work was done by

1. [M. Nimalan](https://github.com/Mark1626)
2. Swethaa. A
3. Addhanki Venkata Sai Veera Manikanta
4. Maneesh Sutar

The benchmarks are from [MachSuite](https://github.com/breagen/MachSuite). The following paper describes the MachSuite benchmarks:

> Brandon Reagen, Robert Adolf, Sophia Yakun Shao, Gu-Yeon Wei, and David Brooks.
> *"MachSuite: Benchmarks for Accelerator Design and Customized Architectures."*
  2014 IEEE International Symposium on Workload Characterization.
