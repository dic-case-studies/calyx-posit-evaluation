all: convert-data convert-expect

parse: check.data input.data
	node parse.js

convert-data: spmv.in.double.json
	$(F2PConvertor) spmv.in.double.json val > spmv.in.posit_1.json 
	$(F2PConvertor) spmv.in.posit_1.json vec > spmv.in.posit.json
	$(F2PConvertor) spmv.in.posit.json out > spmv.in.posit_1.json
	mv spmv.in.posit_1.json spmv.in.posit.json

convert-expect: spmv.expect.double.json
	$(F2PConvertor) spmv.expect.double.json out > spmv.expect.posit.json 

convert-p2f-actual: spmv.out.posit.json
	$(P2FConvertor) spmv.out.posit.json val > spmv.out.double_1.json 
	$(P2FConvertor) spmv.out.double_1.json vec > spmv.out.double.json
	$(P2FConvertor) spmv.out.double.json out > spmv.out.double_1.json
	mv spmv.out.double_1.json spmv.out.double.json

run:
	fud e --to dat spmv.fuse -s verilog.data spmv.in.posit.json --through verilog > spmv.out.posit.json

# plot:
# 	python plot.py

benchmark: parse convert-data convert-expect run # plot
