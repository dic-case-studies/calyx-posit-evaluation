F2PConvertor=../../utilities/cpp/build/f2p_convertor
P2FConvertor=../../utilities/cpp/build/p2f_convertor

all: parse run

%.futil: %.fuse
	fuse $< --lower -b calyx -o $@

convert-input:
	$(F2PConvertor) viterbi.in.double.json 32 --1d init --2d transition,emission > viterbi.in.posit.json

parse: check.data input.data
	node parse.js

run: viterbi.futil convert-input
	fud e --to dat $< -s verilog.data viterbi.in.posit.json --through verilog > viterbi.out.posit.json

# plot:
# 	python plot.py

clean:
	rm *.json viterbi.futil *.jpg

.PHONY=parse clean convert-input
