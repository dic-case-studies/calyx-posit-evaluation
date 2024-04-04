# Evaluation of Calyx Posit Bindings

## Dependencies

### Tools for hardware development

- Dahlia
- Calyx
- Verilator
- firtool

### Software tools

- node
- Python

## Instructions to run the benchmarks

- Install python utilities `cd utilities/python; pip3 install -e .; cd ../..`
- Build cpp utilities `cd utilities/cpp; cmake -B ./build/ -S .; make -C build; cd ../../`
- For running the benchmarks, do `make`
