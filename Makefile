run_exp:
	make -C machsuite-posit-rewrite/machsuite-fft-strided
	make -C machsuite-posit-rewrite/machsuite-spmv-crs
	make -C machsuite-posit-rewrite/machsuite-spmv-ellpack
	make -C machsuite-posit-rewrite/machsuite-viterbi

extract_results:
	cp machsuite-posit-rewrite/machsuite-fft-strided/machsuite-fft-strided-imag.png results/
	cp machsuite-posit-rewrite/machsuite-fft-strided/machsuite-fft-strided-real.png results/
	cp machsuite-posit-rewrite/machsuite-spmv-crs/machsuite-spmv-crs.png results/
	cp machsuite-posit-rewrite/machsuite-spmv-ellpack/machsuite-spmv-ellpack.png results/

all: run_exp extract_results

.PHONY: all run_exp extract_results
