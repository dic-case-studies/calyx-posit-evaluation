F2PConvertor=../../utilities/cpp/build/f2p_convertor
P2FConvertor=../../utilities/cpp/build/p2f_convertor

all: parse run convert-p2f-actual

%.futil: %.fuse
	fuse $< --lower -b calyx -o $@

convert-input:
	$(F2PConvertor) spmv.in.double.json 32 --2d nzval --1d vec > spmv.in.posit.json

convert-p2f-actual:
	$(P2FConvertor) spmv.out.posit.json 32 --1d out > spmv.out.double.json

parse: check.data input.data
	node parse.js

run: spmv.futil convert-input
	fud e --to dat $< -s verilog.data spmv.in.posit.json --through verilog > spmv.out.posit.json

clean:
	rm *.json spmv.futil *.jpg

.PHONY=parse clean convert-input convert-p2f-actual

# plot:
# 	python plot.py
