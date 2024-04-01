all:
	make -C machsuite-posit-rewrite/machsuite-fft-strided
	make -C machsuite-posit-rewrite/machsuite-spmv-crs
	make -C machsuite-posit-rewrite/machsuite-spmv-ellpack
	make -C machsuite-posit-rewrite/machsuite-viterbi
