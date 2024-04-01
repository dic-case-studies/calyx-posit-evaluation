F2PConvertor=../../utilities/cpp/build/f2p_convertor
P2FConvertor=../../utilities/cpp/build/p2f_convertor

all: parse run convert-p2f-actual

%.futil: %.fuse
	fuse $< --lower -b calyx -o $@

convert-input:
	$(F2PConvertor) viterbi.in.double.json 32 --1d val,vec,out > viterbi.in.posit.json

convert-p2f-actual:
	$(P2FConvertor) viterbi.out.posit.json 32 --1d out > viterbi.out.double.json

parse: check.data input.data
	node parse.js

run: viterbi.futil convert-input
	fud e --to dat $< -s verilog.data viterbi.in.posit.json --through verilog > viterbi.out.posit.json

clean:
	rm *.json viterbi.futil *.jpg

.PHONY=parse clean convert-input convert-p2f-actual

# plot:
# 	python plot.py
