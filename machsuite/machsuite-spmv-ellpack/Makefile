spmv.futil:
	fuse ./spmv.fuse --lower -b calyx -o spmv.futil

parse:
	node parse.js

convert-data: parse
	$(F2P_CONVERTOR) ./spmv.in.double.json nzval 2 > spmv.in.posit_1.json
	$(F2P_CONVERTOR) ./spmv.in.posit_1.json vec 1 > spmv.in.posit.json

run: spmv.futil convert-data
	fud e --to dat spmv.futil -s verilog.data spmv.in.posit.json > spmv.output.posit.json

convert-output: run
	$(P2F_CONVERTOR) ./spmv.output.posit.json out 1 > spmv.output.double.json

benchmark: convert-output
	python3 plot.py

clean:
	rm *.json spmv.futil *.jpg

.PHONY=clean